from sqlalchemy import select, distinct, and_, or_, func, case, cast, Integer
from sqlalchemy.orm import Session, aliased
from sqlalchemy.sql import func
import math

import sys
sys.path.append('~/app')

from crud.common import getCurrentDatetime, ItemType, ItemState, TaskType, WorkloadType

from model.item import Item
from model.tree import Tree
from model.story import Story
from model.task import Task
from model.bug import Bug
from model.user import User
from model.summary_item import SummaryItem


import jpholiday
import datetime


RISK_ITEM = {
    'BUFFER_LOW':      (100, 0b00000001),
    'BUFFER_NONE':     (200, 0b00000010),
    'DEADLINE_OVER':   (500, 0b00000100),
    'WORKLOAD_2':      ( 50, 0b00001000),
    'WORKLOAD_3':      (100, 0b00010000),
    'WORKLOAD_5':      (200, 0b00100000),
    'NUMBER_OVER_LV1': ( 50, 0b00100000),
    'NUMBER_OVER_LV2': (100, 0b01000000),
    'NUMBER_OVER_LV3': (200, 0b10000000)

}

NUMBER_OVER_LV1 =  500
NUMBER_OVER_LV2 = 1000
NUMBER_OVER_LV3 = 2000


def _getDateLimit(db: Session, rid_item: int):
    try:
        story = db.query(
            Story.datetime_end
        )\
        .join(Tree, Story.rid_items == Tree.rid_ancestor)\
        .where(
            Tree.rid_descendant == rid_item,
            Tree.type == ItemType.STORY.value
        )\
        .one()

        return story.datetime_end

    except Exception as e:
        raise e


def _getTargetItem(db: Session, rid_item: int):
    try:
        query = db.query(
            Item.rid,
            Task.type.label('task_type'),
            Task.workload.label('task_workload'),
            Task.number_total.label('task_number_total'),
            Bug.workload.label('bug_workload'))\
        .outerjoin(Task, Task.rid_items == Item.rid)\
        .outerjoin(Bug, Bug.rid_items == Item.rid)\
        .filter(Item.rid == rid_item)\

        result = query.one()
        return result

    except Exception as e:
        raise e


def _getRiskDeadline(datetime_limit: str, datetime_current: str, item):
    try:
        date_format  = "%Y-%m-%d"
        date_current = datetime.datetime.strptime(datetime_current.split(' ')[0], date_format).date()
        date_limit   = datetime.datetime.strptime(datetime_limit.split(' ')[0], date_format).date()

        if date_limit < date_current:
            risk         = RISK_ITEM['BUFFER_LOW'][0] + RISK_ITEM['BUFFER_NONE'][0] + RISK_ITEM['DEADLINE_OVER'][0]
            risk_factors = RISK_ITEM['BUFFER_LOW'][1] | RISK_ITEM['BUFFER_NONE'][1] | RISK_ITEM['DEADLINE_OVER'][1]
            return risk, risk_factors

        day_active = 0
        delta      = datetime.timedelta(days=1)
        date       = date_current

        while date <= date_limit:
            if date.weekday() < 5 and not jpholiday.is_holiday(date):
                day_active += 1
            date += delta

        workload = 0
        if item.task_workload is not None:
            workload = item.task_workload
        else:
            workload = item.bug_workload

        risk         = 0
        risk_factors = 0

        if (day_active - workload + math.ceil(workload / 2)) <= 0:
            risk         += RISK_ITEM['BUFFER_LOW'][0]
            risk_factors |= RISK_ITEM['BUFFER_LOW'][1]

        if (day_active - workload) <= 0:
            risk         += RISK_ITEM['BUFFER_NONE'][0]
            risk_factors |= RISK_ITEM['BUFFER_NONE'][1]

        return risk, risk_factors

    except Exception as e:
        raise e


def _checkRiskWorkload(item):
    workload = 0
    if item.task_workload is not None:
        workload = item.task_workload
    else:
        workload = item.bug_workload

    risk         = 0
    risk_factors = 0

    if workload == WorkloadType.WITHIN_2_DAYS.value:
        risk         += RISK_ITEM['WORKLOAD_2'][0]
        risk_factors |= RISK_ITEM['WORKLOAD_2'][1]

    if workload == WorkloadType.WITHIN_3_DAYS.value:
        risk         += RISK_ITEM['WORKLOAD_3'][0]
        risk_factors |= RISK_ITEM['WORKLOAD_3'][1]

    if workload == WorkloadType.WITHIN_A_WEEK.value:
        risk         += RISK_ITEM['WORKLOAD_5'][0]
        risk_factors |= RISK_ITEM['WORKLOAD_5'][1]

    return risk, risk_factors


def _checkRiskNumber(item):
    number_total = 0
    if item.task_number_total is not None:
        number_total = item.task_number_total

    risk         = 0
    risk_factors = 0

    if NUMBER_OVER_LV1 < number_total:
        risk         += RISK_ITEM['NUMBER_OVER_LV1'][0]
        risk_factors |= RISK_ITEM['NUMBER_OVER_LV1'][1]

    if NUMBER_OVER_LV1 < number_total:
        risk         += RISK_ITEM['NUMBER_OVER_LV2'][0]
        risk_factors |= RISK_ITEM['NUMBER_OVER_LV2'][1]

    if NUMBER_OVER_LV1 < number_total:
        risk         += RISK_ITEM['NUMBER_OVER_LV3'][0]
        risk_factors |= RISK_ITEM['NUMBER_OVER_LV3'][1]

    return risk, risk_factors


def _setRiskItem(db: Session, rid_item: int, datetime_limit: str, datetime_current: str):
    try:
        item = _getTargetItem(db, rid_item)

        risk         = 0
        risk_factors = 0

        tmp_risk, tmp_risk_factors = _getRiskDeadline(datetime_limit, datetime_current, item)
        risk         += tmp_risk
        risk_factors |= tmp_risk_factors

        tmp_risk, tmp_risk_factors = _checkRiskWorkload(item)
        risk         += tmp_risk
        risk_factors |= tmp_risk_factors

        tmp_risk, tmp_risk_factors = _checkRiskNumber(item)
        risk         += tmp_risk
        risk_factors |= tmp_risk_factors

        # TODO:delete
        print(risk)
        print(bin(risk_factors))


        target_item = db.query(
            Item
        )\
        .filter(Item.rid == item.rid)

        target_item.update({
            Item.risk: risk,
            Item.risk_factors: risk_factors
        })

    except Exception as e:
        raise e

def _setRiskParent(db: Session, rid_item: int):
    try:
        db.query(
            Item
        )\
        .filter(Item.rid == rid_item)\
        .update({
            Item.risk: func.coalesce(
                db.query(
                    cast(func.avg(Item.risk), Integer)
                )
                .join(Tree, Tree.rid_descendant == Item.rid)
                .filter(
                    Item.rid != rid_item,
                    Tree.rid_ancestor == rid_item
                )
                .scalar_subquery(), 0
            )
        }, synchronize_session = False)

    except Exception as e:
        raise e


def _setRiskStory(db: Session, rid_item: int):
    pass


def _setRiskFeature(db: Session, rid_item: int):
    try:
        print(rid_item)

    except Exception as e:
        raise e


def _setRiskEvent(db: Session, rid_item: int):
    try:
        print(rid_item)

    except Exception as e:
        raise e


def _setRiskProject(db: Session, rid_item: int):
    try:
        print(rid_item)

    except Exception as e:
        raise e


def _setRiskParents(db: Session, rid_item: int):
    try:
        result = db.query(
            Tree.rid_ancestor.label('rid')
        )\
        .filter(
            Tree.rid_ancestor   != rid_item,
            Tree.rid_descendant == rid_item
        )\
        .order_by(Tree.type.desc())\
        .all()

        if len(result) != 4:
            raise

        _setRiskParent(db,   result[0].rid)
        _setRiskParent(db, result[1].rid)
        _setRiskParent(db,   result[2].rid)
        _setRiskParent(db, result[3].rid)

    except Exception as e:
        raise e


def analyzeItem(db: Session, rid_item: int):
    try:
        print('----------------- analyze start')

        datetime_limit   = _getDateLimit(db, rid_item)
        datetime_current = getCurrentDatetime()

        _setRiskItem(db, rid_item, datetime_limit, datetime_current)

        _setRiskParents(db, rid_item)

        print('----------------- analyze end')

    except Exception as e:
        raise e

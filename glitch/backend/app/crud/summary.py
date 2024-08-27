from sqlalchemy import select, distinct, desc   # type: ignore
from sqlalchemy.orm import Session, aliased     # type: ignore
from sqlalchemy.sql import func                 # type: ignore

import pytz                                     # type: ignore
from datetime import datetime
from enum import Enum

import sys
sys.path.append('~/app')

from model.summary_item import SummaryItem
from model.summary_user import SummaryUser
from model.user import User


def getSummariesItem(db: Session, rid: int):
    try:
        result = db.query(SummaryItem).filter(SummaryItem.rid == rid).order_by(SummaryItem.date_entry).all()
        return result

    except Exception as e:
        raise e


def getSummariesUser(db: Session, rid: int):
    try:
        UserAlias = aliased(User)

        query = db.query(
            SummaryUser.rid,
            SummaryUser.id_project,
            UserAlias.rid.label('rid_users'),
            UserAlias.name.label('name'),
            SummaryUser.task_count_idle,
            SummaryUser.task_count_run,
            SummaryUser.task_count_alert,
            SummaryUser.task_count_review,
            SummaryUser.task_count_complete,
            SummaryUser.task_count_total,
            SummaryUser.task_workload_total,
            SummaryUser.task_number_completed,
            SummaryUser.task_number_total,
            SummaryUser.bug_count_idle,
            SummaryUser.bug_count_run,
            SummaryUser.bug_count_alert,
            SummaryUser.bug_count_review,
            SummaryUser.bug_count_complete,
            SummaryUser.bug_count_total,
            SummaryUser.bug_workload_total,
            SummaryUser.date_entry
        )\
        .join(UserAlias,  UserAlias.rid == SummaryUser.rid_users)\
        .filter(SummaryUser.rid_users == rid)\
        .order_by(SummaryUser.date_entry)

        result = query.all()
        return result

    except Exception as e:
        raise e

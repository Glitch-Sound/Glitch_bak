from sqlalchemy import select, distinct, desc   # type: ignore
from sqlalchemy.orm import Session, aliased     # type: ignore
from sqlalchemy.sql import func                 # type: ignore

import pytz                                     # type: ignore
from datetime import datetime
from enum import Enum

import sys
sys.path.append('~/app')

from schema import item as schema_item
from model.item import Item
from model.tree import Tree
from model.summary_item import SummaryItem
from model.summary_user import SummaryUser

from model.project import Project
from model.event import Event
from model.feature import Feature
from model.story import Story
from model.task import Task
from model.bug import Bug
from model.user import User


RISK_1 = 0b00000001
RISK_2 = 0b00000010
RISK_3 = 0b00000100
RISK_4 = 0b00001000
RISK_5 = 0b00010000
RISK_6 = 0b00100000
RISK_7 = 0b01000000
RISK_8 = 0b10000000


class ItemType(Enum):
    PROJECT = 1
    EVENT   = 2
    FEATURE = 3
    STORY   = 4
    TASK    = 5
    BUG     = 6

class ItemState(Enum):
    IDLE     = 1
    RUN      = 2
    ALERT    = 3
    REVIEW   = 4
    COMPLETE = 5

class ExtractType(Enum):
    ALL        = 1
    INCOMPLETE = 2
    HIGH_RISK  = 3
    ALERT      = 4
    ASSIGNMENT = 5

class ItemParam():
    def __init__(self, id_project: int, type_extract: ExtractType, rid_users: int):
        self.id_project = id_project
        self.type_extract = type_extract
        self.rid_users = rid_users

class ItemUpdateCommon():
    def __init__(self, rid: int, state: int, rid_users: int, title: str, detail: str, result: str):
        self.rid       = rid
        self.state     = state
        self.rid_users = rid_users
        self.title     = title
        self.detail    = detail
        self.result    = result


def _getCurrentDate():
    current_utc_time = datetime.now(pytz.timezone('Asia/Tokyo'))
    current_date = current_utc_time.strftime('%Y-%m-%d')
    return current_date


def _getCurrentDatetime():
    current_utc_time = datetime.now(pytz.timezone('Asia/Tokyo'))
    current_datetime = current_utc_time.strftime('%Y-%m-%d %H:%M:%S')
    return current_datetime


def _createTree(db: Session, type_create: ItemType, rid_parent: int, rid: int):
    try:
        trees = db.query(Tree.rid_ancestor).filter(Tree.rid_descendant == rid_parent).order_by(Tree.rid_ancestor).all()
        if not trees:
            raise

        list_rid_ancestor = [r[0] for r in trees]
        list_rid_ancestor.append(rid)

        for index, rid_ancestor in enumerate(list_rid_ancestor):
            type = index + 1
            if rid_ancestor == rid:
                type = type_create.value

            tree = Tree(
                rid_ancestor=rid_ancestor,
                rid_descendant=rid,
                type=type
            )
            db.add(tree)

    except Exception as e:
        raise e


def _getSummaryCount(list_sum: any, list_count: any):
    result_sum = {
        'task_workload'         : 0,
        'task_number_completed' : 0,
        'task_number_total'     : 0,
        'bug_workload'          : 0
    }

    if list_sum[0].task_workload:
        result_sum['task_workload'] = list_sum[0].task_workload

    if list_sum[0].task_number_completed:
        result_sum['task_number_completed'] = list_sum[0].task_number_completed

    if list_sum[0].task_number_total:
        result_sum['task_number_total'] = list_sum[0].task_number_total

    if list_sum[0].bug_workload:
        result_sum['bug_workload'] = list_sum[0].bug_workload

    result_count = {
        'task_count_idle'     : 0,
        'task_count_run'      : 0,
        'task_count_alert'    : 0,
        'task_count_review'   : 0,
        'task_count_complete' : 0,
        'task_count_total'    : 0,
        'bug_count_idle'      : 0,
        'bug_count_run'       : 0,
        'bug_count_alert'     : 0,
        'bug_count_review'    : 0,
        'bug_count_complete'  : 0,
        'bug_count_total'     : 0
    }

    sum_task = 0
    sum_bug  = 0
    for target in list_count:
        if   target.type == ItemType.TASK.value:
            match target.state:
                case ItemState.IDLE.value:
                    result_count['task_count_idle'] = target.count
                    sum_task += target.count
                case ItemState.RUN.value:
                    result_count['task_count_run'] = target.count
                    sum_task += target.count
                case ItemState.ALERT.value:
                    result_count['task_count_alert'] = target.count
                    sum_task += target.count
                case ItemState.REVIEW.value:
                    result_count['task_count_review'] = target.count
                    sum_task += target.count
                case ItemState.COMPLETE.value:
                    result_count['task_count_complete'] = target.count
                    sum_task += target.count

        elif target.type == ItemType.BUG.value:
            match target.state:
                case ItemState.IDLE.value:
                    result_count['bug_count_idle'] = target.count
                    sum_bug += target.count
                case ItemState.RUN.value:
                    result_count['bug_count_run'] = target.count
                    sum_bug += target.count
                case ItemState.ALERT.value:
                    result_count['bug_count_alert'] = target.count
                    sum_bug += target.count
                case ItemState.REVIEW.value:
                    result_count['bug_count_review'] = target.count
                    sum_bug += target.count
                case ItemState.COMPLETE.value:
                    result_count['bug_count_complete'] = target.count
                    sum_bug += target.count

    result_count['task_count_total'] = sum_task
    result_count['bug_count_total']  = sum_bug

    return result_sum, result_count


def _createSummaryItem(db: Session, rid_target: int):
    try:
        trees = db.query(Tree).filter(Tree.rid_descendant == rid_target).order_by(desc(Tree.rid_ancestor)).all()
        if not trees:
            raise

        for tree in trees:
            if tree.rid_ancestor == tree.rid_descendant:
                continue

            list_sum = db.query(
                func.sum(Task.workload).label('task_workload'),
                func.sum(Task.number_completed).label('task_number_completed'),
                func.sum(Task.number_total).label('task_number_total'),
                func.sum(Bug.workload).label('bug_workload')
            )\
            .select_from(Tree)\
            .outerjoin(Task, Tree.rid_descendant == Task.rid_items)\
            .outerjoin(Bug,  Tree.rid_descendant == Bug.rid_items)\
            .filter(Tree.rid_ancestor   == tree.rid_ancestor)\
            .filter(Tree.rid_descendant != tree.rid_ancestor)\
            .all()
 
            list_count = db.query(
                Item.type,
                Item.state,
                func.count(Item.rid).label('count')
            )\
            .select_from(Tree)\
            .join(Item, Tree.rid_descendant == Item.rid)\
            .filter(Tree.rid_ancestor   == tree.rid_ancestor)\
            .filter(Tree.rid_descendant != tree.rid_ancestor)\
            .group_by(Item.type, Item.state)\
            .all()

            result_sum, result_count = _getSummaryCount(list_sum, list_count)

            current_date = _getCurrentDate()
            summary_item = db.query(SummaryItem).filter(
                SummaryItem.rid_items  == tree.rid_ancestor,
                SummaryItem.date_entry == current_date
            ).all()

            if not summary_item:
                summary = SummaryItem(
                    rid_items=tree.rid_ancestor,
                    task_count_idle=result_count['task_count_idle'],
                    task_count_run=result_count['task_count_run'],
                    task_count_alert=result_count['task_count_alert'],
                    task_count_review=result_count['task_count_review'],
                    task_count_complete=result_count['task_count_complete'],
                    task_count_total=result_count['task_count_total'],
                    task_workload_total=result_sum['task_workload'],
                    task_number_completed=result_sum['task_number_completed'],
                    task_number_total=result_sum['task_number_total'],
                    bug_count_idle=result_count['bug_count_idle'],
                    bug_count_run=result_count['bug_count_run'],
                    bug_count_alert=result_count['bug_count_alert'],
                    bug_count_review=result_count['bug_count_review'],
                    bug_count_complete=result_count['bug_count_complete'],
                    bug_count_total=result_count['bug_count_total'],
                    bug_workload_total=result_sum['bug_workload'],
                    date_entry=current_date
                )
                db.add(summary)

            else:
                summary = db.query(SummaryItem).filter(SummaryItem.rid_items == tree.rid_ancestor)
                summary.update({
                    SummaryItem.task_count_idle: result_count['task_count_idle'],
                    SummaryItem.task_count_run: result_count['task_count_run'],
                    SummaryItem.task_count_alert: result_count['task_count_alert'],
                    SummaryItem.task_count_review: result_count['task_count_review'],
                    SummaryItem.task_count_complete: result_count['task_count_complete'],
                    SummaryItem.task_count_total: result_count['task_count_total'],
                    SummaryItem.task_workload_total: result_sum['task_workload'],
                    SummaryItem.task_number_completed: result_sum['task_number_completed'],
                    SummaryItem.task_number_total: result_sum['task_number_total'],
                    SummaryItem.bug_count_idle: result_count['bug_count_idle'],
                    SummaryItem.bug_count_run: result_count['bug_count_run'],
                    SummaryItem.bug_count_alert: result_count['bug_count_alert'],
                    SummaryItem.bug_count_review: result_count['bug_count_review'],
                    SummaryItem.bug_count_complete: result_count['bug_count_complete'],
                    SummaryItem.bug_count_total: result_count['bug_count_total'],
                    SummaryItem.bug_workload_total: result_sum['bug_workload']
                })

    except Exception as e:
        raise e


def _createSummaryUser(db: Session, id_project: int, rid_users: int):
    try:
        list_sum = db.query(
            func.sum(Task.workload).label('task_workload'),
            func.sum(Task.number_completed).label('task_number_completed'),
            func.sum(Task.number_total).label('task_number_total'),
            func.sum(Bug.workload).label('bug_workload')
        )\
        .select_from(Item)\
        .outerjoin(Task, Item.rid == Task.rid_items)\
        .outerjoin(Bug,  Item.rid == Bug.rid_items)\
        .filter(Item.id_project == id_project)\
        .filter(Item.rid_users  == rid_users)\
        .filter(Item.type.in_([ItemType.TASK.value, ItemType.BUG.value]))\
        .all()

        list_count = db.query(
            Item.type,
            Item.state,
            func.count(Item.rid).label('count')
        )\
        .select_from(Item)\
        .filter(Item.id_project == id_project)\
        .filter(Item.rid_users  == rid_users)\
        .filter(Item.type.in_([ItemType.TASK.value, ItemType.BUG.value]))\
        .group_by(Item.type, Item.state)\
        .all()

        result_sum, result_count = _getSummaryCount(list_sum, list_count)

        current_date = _getCurrentDate()
        summary_user = db.query(SummaryUser).filter(
            SummaryUser.rid_users  == rid_users,
            SummaryUser.id_project == id_project,
            SummaryUser.date_entry == current_date
        ).all()

        if not summary_user:
            summary = SummaryUser(
                rid_users=rid_users,
                id_project=id_project,
                task_count_idle=result_count['task_count_idle'],
                task_count_run=result_count['task_count_run'],
                task_count_alert=result_count['task_count_alert'],
                task_count_review=result_count['task_count_review'],
                task_count_complete=result_count['task_count_complete'],
                task_count_total=result_count['task_count_total'],
                task_workload_total=result_sum['task_workload'],
                task_number_completed=result_sum['task_number_completed'],
                task_number_total=result_sum['task_number_total'],
                bug_count_idle=result_count['bug_count_idle'],
                bug_count_run=result_count['bug_count_run'],
                bug_count_alert=result_count['bug_count_alert'],
                bug_count_review=result_count['bug_count_review'],
                bug_count_complete=result_count['bug_count_complete'],
                bug_count_total=result_count['bug_count_total'],
                bug_workload_total=result_sum['bug_workload'],
                date_entry=current_date
            )
            db.add(summary)

        else:
            summary = db.query(SummaryUser).filter(
                SummaryUser.rid_users  == rid_users,
                SummaryUser.id_project == id_project,
                SummaryUser.date_entry == current_date
            )
            summary.update({
                SummaryUser.task_count_idle: result_count['task_count_idle'],
                SummaryUser.task_count_run: result_count['task_count_run'],
                SummaryUser.task_count_alert: result_count['task_count_alert'],
                SummaryUser.task_count_review: result_count['task_count_review'],
                SummaryUser.task_count_complete: result_count['task_count_complete'],
                SummaryUser.task_count_total: result_count['task_count_total'],
                SummaryUser.task_workload_total: result_sum['task_workload'],
                SummaryUser.task_number_completed: result_sum['task_number_completed'],
                SummaryUser.task_number_total: result_sum['task_number_total'],
                SummaryUser.bug_count_idle: result_count['bug_count_idle'],
                SummaryUser.bug_count_run: result_count['bug_count_run'],
                SummaryUser.bug_count_alert: result_count['bug_count_alert'],
                SummaryUser.bug_count_review: result_count['bug_count_review'],
                SummaryUser.bug_count_complete: result_count['bug_count_complete'],
                SummaryUser.bug_count_total: result_count['bug_count_total'],
                SummaryUser.bug_workload_total: result_sum['bug_workload']
            })

    except Exception as e:
        raise e



def _createSortPathRoot(id_project: int):
    return id_project * 10000000000000


def _createSortPath(db: Session, type: ItemType, rid_parent: int):
    try:
        path_sort_parent      = db.query(Item.path_sort).filter(Item.rid == rid_parent).scalar()
        count_rid_descendants = db.query(Tree.rid_descendant).filter(Tree.rid_ancestor == rid_parent).count()

        path_sort = path_sort_parent
        match type:
            case ItemType.EVENT:
                path_sort += (count_rid_descendants * 1000000000)

            case ItemType.FEATURE:
                path_sort += (count_rid_descendants * 100000)

            case ItemType.STORY:
                path_sort += (count_rid_descendants * 10)

            case ItemType.TASK | ItemType.BUG:
                path_sort += (type.value)

        return path_sort

    except Exception as e:
        raise e


def _updateItem(db: Session, target: ItemUpdateCommon):
    try:
        current_datetime = _getCurrentDatetime()

        item = db.query(Item).filter(Item.rid == target.rid)
        item.update({
            Item.state: target.state,
            Item.rid_users: target.rid_users,
            Item.title: target.title,
            Item.detail: target.detail,
            Item.result: target.result,
            Item.datetime_update: current_datetime
        })

        item_updated = item.first()
        return item_updated

    except Exception as e:
        raise e


def _deleteItem(db: Session, rid: int):
    try:
        current_datetime = _getCurrentDatetime()

        db.begin()
        item = db.query(Item).filter(Item.rid == rid)
        item.update({
            Item.is_deleted: 1,
            Item.datetime_update: current_datetime
        })
        db.commit()

    except Exception as e:
        db.rollback()
        raise e


def _extructItem(db: Session, params: ItemParam):
    try:
        cte_extruct = None
        match params.type_extract:
            case ExtractType.ALL.value:
                cte_extruct = db.query(
                    Tree.rid_descendant.label('rid')
                )\
                .filter(Tree.rid_ancestor == params.id_project)

            case ExtractType.INCOMPLETE.value:
                subquery_target = (
                    select(Item.rid)
                    .where(Item.state != ItemState.COMPLETE.value)
                ).subquery()

                cte_extruct = db.query(
                    distinct(Tree.rid_descendant).label('rid')
                )\
                .where(Tree.rid_descendant.in_(subquery_target))

            case ExtractType.HIGH_RISK.value:
                pass

            case ExtractType.ALERT.value:
                subquery_target = (
                    select(Item.rid)
                    .where(Item.state == ItemState.ALERT.value)
                ).subquery()

                cte_extruct = db.query(
                    distinct(Tree.rid_ancestor).label('rid')

                )\
                .where(Tree.rid_descendant.in_(subquery_target))

            case ExtractType.ASSIGNMENT.value:
                subquery_target = (
                    select(Item.rid)
                    .where(Item.rid_users == params.rid_users)
                ).subquery()

                cte_extruct = db.query(
                    distinct(Tree.rid_ancestor).label('rid')
                )\
                .where(Tree.rid_descendant.in_(subquery_target))

        return cte_extruct.cte(name='targets')

    except Exception as e:
        raise e


def getItems(db: Session, params: ItemParam):
    try:
        UserAlias1 = aliased(User)
        UserAlias2 = aliased(User)

        cte_extruct = _extructItem(db, params)

        query = db.query(
            Item.rid,
            Item.id_project,
            Item.type,
            Item.state,
            Item.risk,
            Item.risk_factors,
            Item.priority,
            Item.title,
            Item.detail,
            Item.result,
            Item.datetime_entry,
            Item.datetime_update,
            UserAlias1.rid.label('rid_users'),
            UserAlias1.name.label('name'),
            UserAlias2.rid.label('rid_users_review'),
            UserAlias2.name.label('name_review'),
            Project.datetime_start.label('project_datetime_start'),
            Project.datetime_end.label('project_datetime_end'),
            Event.datetime_end.label('event_datetime_end'),
            Story.datetime_start.label('story_datetime_start'),
            Story.datetime_end.label('story_datetime_end'),
            Task.type.label('task_type'),
            Task.workload.label('task_workload'),
            Task.number_completed.label('task_number_completed'),
            Task.number_total.label('task_number_total'),
            Bug.workload.label('bug_workload'))\
        .select_from(cte_extruct)\
        .join(Item, Item.rid == cte_extruct.c.rid)\
        .outerjoin(UserAlias1,  UserAlias1.rid == Item.rid_users)\
        .outerjoin(UserAlias2,  UserAlias2.rid == Item.rid_users_review)\
        .outerjoin(Project, Project.rid_items == Item.rid)\
        .outerjoin(Event, Event.rid_items == Item.rid)\
        .outerjoin(Feature, Feature.rid_items == Item.rid)\
        .outerjoin(Story, Story.rid_items == Item.rid)\
        .outerjoin(Task, Task.rid_items == Item.rid)\
        .outerjoin(Bug, Bug.rid_items == Item.rid)\
        .order_by(Item.path_sort)

        result = query.all()
        return result

    except Exception as e:
        raise e


def getProjects(db: Session):
    try:
        UserAlias = aliased(User)

        query = db.query(
            Item.rid,
            Item.id_project,
            Item.state,
            Item.risk,
            Item.risk_factors,
            Item.title,
            Item.detail,
            Item.result,
            Item.datetime_entry,
            Item.datetime_update,
            UserAlias.rid.label('rid_users'),
            UserAlias.name.label('name'),
            Project.datetime_start.label('project_datetime_start'),
            Project.datetime_end.label('project_datetime_end'))\
        .outerjoin(UserAlias,  UserAlias.rid == Item.rid_users)\
        .outerjoin(Project, Project.rid_items == Item.rid)\
        .filter(Item.type == ItemType.PROJECT.value)\
        .order_by(Item.rid)
         
        result = query.all()
        return result

    except Exception as e:
        raise e


def createProject(db: Session, target: schema_item.ProjectCreate):
    try:
        current_datetime = _getCurrentDatetime()

        db.begin()
        max_id_project = db.query(func.max(Item.id_project)).scalar()
        if max_id_project is None:
            max_id_project = 0
        max_id_project += 1

        item = Item(
            path_sort=_createSortPathRoot(max_id_project),
            rid_users=target.rid_users,
            rid_users_review=None,
            id_project=max_id_project,
            type=ItemType.PROJECT.value,
            title=target.title,
            detail=target.detail,
            datetime_entry=current_datetime,
            datetime_update=current_datetime
        )
        db.add(item)
        db.flush()

        addition = Project(
            rid_items=item.rid,
            datetime_start=target.datetime_start,
            datetime_end=target.datetime_end
        )
        db.add(addition)

        tree = Tree(
            rid_ancestor=max_id_project,
            rid_descendant=max_id_project,
            type=ItemType.PROJECT.value
        )
        db.add(tree)
        db.commit()

        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def updateProject(db: Session, target:schema_item.ProjectUpdate):
    try:
        param_item = ItemUpdateCommon(
            rid=target.rid,
            state=target.state,
            rid_users=target.rid_users,
            title=target.title,
            detail=target.detail,
            result=target.result
        )

        db.begin()
        item = _updateItem(db, param_item)

        addition = db.query(Project).filter(Project.rid_items == target.rid)
        addition.update({
            Project.datetime_start: target.datetime_start,
            Project.datetime_end: target.datetime_end
        })
        db.commit()
        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def deleteProject(db: Session, rid: int):
    try:
        _deleteItem(db, rid)

    except Exception as e:
        raise e


def createEvent(db: Session, target:schema_item.EventCreate):
    try:
        current_datetime = _getCurrentDatetime()

        db.begin()
        item = Item(
            path_sort=_createSortPath(db, ItemType.EVENT, target.rid_items),
            id_project=target.id_project,
            rid_users=target.rid_users,
            rid_users_review=None,
            type=ItemType.EVENT.value,
            title=target.title,
            detail=target.detail,
            datetime_entry=current_datetime,
            datetime_update=current_datetime
        )

        db.add(item)
        db.flush()

        addition = Event(
            rid_items=item.rid,
            datetime_end=target.datetime_end
        )
        db.add(addition)

        _createTree(db, ItemType.EVENT, target.rid_items, item.rid)
        db.flush()
        db.commit()

        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def updateEvent(db: Session, target:schema_item.EventUpdate):
    try:
        param_item = ItemUpdateCommon(
            rid=target.rid,
            state=target.state,
            rid_users=target.rid_users,
            title=target.title,
            detail=target.detail,
            result=target.result
        )

        db.begin()
        item = _updateItem(db, param_item)

        addition = db.query(Event).filter(Event.rid_items == target.rid)
        addition.update({
            Event.datetime_end: target.datetime_end
        })
        db.commit()
        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def deleteEvent(db: Session, rid: int):
    try:
        _deleteItem(db, rid)

    except Exception as e:
        raise e


def createFeature(db: Session, target:schema_item.FeatureCreate):
    try:
        current_datetime = _getCurrentDatetime()

        db.begin()
        item = Item(
            path_sort=_createSortPath(db, ItemType.FEATURE, target.rid_items),
            id_project=target.id_project,
            rid_users=target.rid_users,
            rid_users_review=None,
            type=ItemType.FEATURE.value,
            title=target.title,
            detail=target.detail,
            datetime_entry=current_datetime,
            datetime_update=current_datetime
        )

        db.add(item)
        db.flush()

        addition = Feature(
            rid_items=item.rid
        )
        db.add(addition)

        _createTree(db, ItemType.FEATURE, target.rid_items, item.rid)
        db.flush()
        db.commit()

        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def updateFeature(db: Session, target:schema_item.FeatureUpdate):
    try:
        param_item = ItemUpdateCommon(
            rid=target.rid,
            state=target.state,
            rid_users=target.rid_users,
            title=target.title,
            detail=target.detail,
            result=target.result
        )

        db.begin()
        item = _updateItem(db, param_item)
        db.commit()
        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def deleteFeature(db: Session, rid: int):
    try:
        _deleteItem(db, rid)

    except Exception as e:
        raise e


def createStory(db: Session, target:schema_item.StoryCreate):
    try:
        current_datetime = _getCurrentDatetime()

        db.begin()
        item = Item(
            path_sort=_createSortPath(db, ItemType.STORY, target.rid_items),
            id_project=target.id_project,
            rid_users=target.rid_users,
            rid_users_review=None,
            type=ItemType.STORY.value,
            title=target.title,
            detail=target.detail,
            datetime_entry=current_datetime,
            datetime_update=current_datetime
        )

        db.add(item)
        db.flush()

        addition = Story(
            rid_items=item.rid,
            datetime_start=target.datetime_start,
            datetime_end=target.datetime_end
        )
        db.add(addition)

        _createTree(db, ItemType.STORY, target.rid_items, item.rid)
        db.flush()
        db.commit()

        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def updateStory(db: Session, target:schema_item.StoryUpdate):
    try:
        param_item = ItemUpdateCommon(
            rid=target.rid,
            state=target.state,
            rid_users=target.rid_users,
            title=target.title,
            detail=target.detail,
            result=target.result
        )

        db.begin()
        item = _updateItem(db, param_item)

        addition = db.query(Story).filter(Story.rid_items == target.rid)
        addition.update({
            Story.datetime_start: target.datetime_start,
            Story.datetime_end: target.datetime_end

        })
        db.commit()
        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def deleteStory(db: Session, rid: int):
    try:
        _deleteItem(db, rid)

    except Exception as e:
        raise e


def createTask(db: Session, target:schema_item.TaskCreate):
    try:
        current_datetime = _getCurrentDatetime()

        db.begin()
        item = Item(
            path_sort=_createSortPath(db, ItemType.TASK, target.rid_items),
            id_project=target.id_project,
            rid_users=target.rid_users,
            rid_users_review=None,
            type=ItemType.TASK.value,
            title=target.title,
            detail=target.detail,
            datetime_entry=current_datetime,
            datetime_update=current_datetime
        )

        db.add(item)
        db.flush()

        addition = Task(
            rid_items=item.rid,
            type=target.type,
            workload=target.workload,
            number_completed=target.number_completed,
            number_total=target.number_total
        )
        db.add(addition)

        _createTree(db, ItemType.TASK, target.rid_items, item.rid)
        db.flush()

        _createSummaryItem(db, item.rid)
        _createSummaryUser(db, target.id_project, target.rid_users)
        db.commit()

        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def updateTask(db: Session, target:schema_item.TaskUpdate):
    try:
        param_item = ItemUpdateCommon(
            rid=target.rid,
            state=target.state,
            rid_users=target.rid_users,
            title=target.title,
            detail=target.detail,
            result=target.result
        )

        db.begin()
        item = _updateItem(db, param_item)

        addition = db.query(Task).filter(Task.rid_items == target.rid)
        addition.update({
            Task.type: target.type,
            Task.workload: target.workload,
            Task.number_completed: target.number_completed,
            Task.number_total: target.number_total
        })

        id_project = db.query(Item.id_project).filter(Item.rid == target.rid)

        _createSummaryItem(db, item.rid)
        _createSummaryUser(db, id_project, target.rid_users)
        db.commit()

        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def deleteTask(db: Session, rid: int):
    try:
        _deleteItem(db, rid)

    except Exception as e:
        raise e


def updateTaskPriority(db: Session, target:schema_item.TaskPriorityUpdate):
    try:
        db.begin()
        item = db.query(Item).filter(Item.rid == target.rid)
        item.update({
            Item.priority: target.priority
        })
        db.commit()

        item_updated = item.first()
        db.refresh(item_updated)
        return item_updated

    except Exception as e:
        db.rollback()
        raise e


def createBug(db: Session, target:schema_item.BugCreate):
    try:
        current_datetime = _getCurrentDatetime()

        db.begin()
        item = Item(
            path_sort=_createSortPath(db, ItemType.BUG, target.rid_items),
            id_project=target.id_project,
            rid_users=target.rid_users,
            rid_users_review=None,
            type=ItemType.BUG.value,
            title=target.title,
            detail=target.detail,
            datetime_entry=current_datetime,
            datetime_update=current_datetime
        )

        db.add(item)
        db.flush()

        addition = Bug(
            rid_items=item.rid,
            workload=target.workload
        )
        db.add(addition)

        _createTree(db, ItemType.BUG, target.rid_items, item.rid)
        db.flush()

        _createSummaryItem(db, item.rid)
        _createSummaryUser(db, target.id_project, target.rid_users)
        db.commit()

        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def updateBug(db: Session, target:schema_item.BugUpdate):
    try:
        param_item = ItemUpdateCommon(
            rid=target.rid,
            state=target.state,
            rid_users=target.rid_users,
            title=target.title,
            detail=target.detail,
            result=target.result
        )

        db.begin()
        item = _updateItem(db, param_item)

        addition = db.query(Bug).filter(Bug.rid_items == target.rid)
        addition.update({
            Bug.workload: target.workload
        })

        id_project = db.query(Item.id_project).filter(Item.rid == target.rid)

        _createSummaryItem(db, item.rid)
        _createSummaryUser(db, id_project, target.rid_users)
        db.commit()

        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def deleteBug(db: Session, rid: int):
    try:
        _deleteItem(db, rid)

    except Exception as e:
        raise e


def updateBugPriority(db: Session, target:schema_item.BugPriorityUpdate):
    try:
        db.begin()
        item = db.query(Item).filter(Item.rid == target.rid)
        item.update({
            Item.priority: target.priority
        })
        db.commit()

        item_updated = item.first()
        db.refresh(item_updated)
        return item_updated

    except Exception as e:
        db.rollback()
        raise e

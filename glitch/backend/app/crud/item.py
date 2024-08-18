from sqlalchemy import Text, case               # type: ignore
from sqlalchemy.orm import Session, aliased     # type: ignore
from sqlalchemy.sql import func                 # type: ignore
from sqlalchemy.sql import select               # type: ignore

import pytz                                     # type: ignore
from datetime import datetime
from enum import Enum

import sys
sys.path.append('~/app')

from schema import item as schema_item
from model.item import Item
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


class ItemCommon():
    def __init__(self, rid: int, state: int, rid_users: int, title: str, detail: str, result: str):
        self.rid       = rid
        self.state     = state
        self.rid_users = rid_users
        self.title     = title
        self.detail    = detail
        self.result    = result


def _getCurrentDatetime():
    current_utc_time = datetime.now(pytz.timezone('Asia/Tokyo'))
    current_datetime = current_utc_time.isoformat()
    return current_datetime


def _updateItem(db: Session, target: ItemCommon):
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


def getItems(db: Session, rid_project: int):
    try:
        UserAlias1 = aliased(User)
        UserAlias2 = aliased(User)

        t0 = aliased(Item, name='t0')
        order_state_t0 = case(
            (t0.state == 3, 1),
            (t0.state == 4, 2),
            (t0.state == 2, 3),
            (t0.state == 1, 4),
            (t0.state == 5, 5),
            else_=0
        )

        query_base = db.query(
            t0.rid,
            t0.rid_items,
            t0.rid_users,
            t0.rid_users_review,
            t0.type,
            t0.state,
            t0.risk,
            t0.risk_factors,
            t0.title,
            t0.detail,
            t0.result,
            t0.datetime_entry,
            t0.datetime_update,
            (func.cast(order_state_t0, Text) + ':' + func.cast(t0.rid, Text)).label('path')
        )\
        .filter(t0.rid == rid_project)\
        .filter(t0.is_deleted == 0)

        query_recursive = query_base.cte(name='targets', recursive=True)

        n = aliased(Item, name='n')
        t = aliased(query_recursive, name='t')

        order_state_n = case(
            (n.state == 3, 1),
            (n.state == 4, 2),
            (n.state == 2, 3),
            (n.state == 1, 4),
            (n.state == 5, 5),
            else_=0
        )

        query_recursive = query_recursive.union_all(
            db.query(
                n.rid,
                n.rid_items,
                n.rid_users,
                n.rid_users_review,
                n.type,
                n.state,
                n.risk,
                n.risk_factors,
                n.title,
                n.detail,
                n.result,
                n.datetime_entry,
                n.datetime_update,
                (t.c.path + '-' + func.cast(order_state_n, Text) + ':' + func.cast(n.rid, Text)).label('path')
            )\
            .join(t, t.c.rid == n.rid_items)\
            .filter(n.is_deleted == 0)\
        )

        query_final = db.query(
            query_recursive.c.rid,
            query_recursive.c.type,
            query_recursive.c.state,
            query_recursive.c.risk,
            query_recursive.c.risk_factors,
            query_recursive.c.title,
            query_recursive.c.detail,
            query_recursive.c.result,
            query_recursive.c.datetime_entry,
            query_recursive.c.datetime_update,
            UserAlias1.rid.label('rid_users'),
            UserAlias1.name.label('name'),
            UserAlias2.rid.label('rid_users_review'),
            UserAlias2.name.label('name_review'),
            Project.datetime_start.label('project_datetime_start'),
            Project.datetime_end.label('project_datetime_end'),
            Event.datetime_end.label('event_datetime_end'),
            Story.datetime_start.label('story_datetime_start'),
            Story.datetime_end.label('story_datetime_end'),
            Task.priority.label('task_priority'),
            Task.type.label('task_type'),
            Task.workload.label('task_workload'),
            Task.number_completed.label('task_number_completed'),
            Task.number_total.label('task_number_total'),
            Bug.priority.label('bug_priority'),
            Bug.workload.label('bug_workload'))\
        .outerjoin(UserAlias1,  UserAlias1.rid == query_recursive.c.rid_users)\
        .outerjoin(UserAlias2,  UserAlias2.rid == query_recursive.c.rid_users_review)\
        .outerjoin(Project, Project.rid_items == query_recursive.c.rid)\
        .outerjoin(Event, Event.rid_items == query_recursive.c.rid)\
        .outerjoin(Feature, Feature.rid_items == query_recursive.c.rid)\
        .outerjoin(Story, Story.rid_items == query_recursive.c.rid)\
        .outerjoin(Task, Task.rid_items == query_recursive.c.rid)\
        .outerjoin(Bug, Bug.rid_items == query_recursive.c.rid)\
        .order_by(query_recursive.c.path)

        result = query_final.all()
        return result

    except Exception as e:
        raise e


def getProjects(db: Session):
    try:
        UserAlias = aliased(User)

        query = db.query(
            Item.rid,
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


def createProject(db: Session, target:schema_item.ProjectCreate):
    try:
        current_datetime = _getCurrentDatetime()

        item = Item(
            rid_users=target.rid_users,
            rid_users_review=None,
            type=ItemType.PROJECT.value,
            title=target.title,
            detail=target.detail,
            datetime_entry=current_datetime,
            datetime_update=current_datetime
        )
        db.begin()
        db.add(item)
        db.flush()

        addition = Project(
            rid_items=item.rid,
            datetime_start=target.datetime_start,
            datetime_end=target.datetime_end
        )
        db.add(addition)
        db.commit()
        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def updateProject(db: Session, target:schema_item.ProjectUpdate):
    try:
        param_item = ItemCommon(
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

        item = Item(
            rid_items=target.rid_items,
            rid_users=target.rid_users,
            rid_users_review=None,
            type=ItemType.EVENT.value,
            title=target.title,
            detail=target.detail,
            datetime_entry=current_datetime,
            datetime_update=current_datetime
        )
        db.begin()
        db.add(item)
        db.flush()

        addition = Event(
            rid_items=item.rid,
            datetime_end=target.datetime_end
        )
        db.add(addition)
        db.commit()
        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def updateEvent(db: Session, target:schema_item.EventUpdate):
    try:
        param_item = ItemCommon(
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

        item = Item(
            rid_items=target.rid_items,
            rid_users=target.rid_users,
            rid_users_review=None,
            type=ItemType.FEATURE.value,
            title=target.title,
            detail=target.detail,
            datetime_entry=current_datetime,
            datetime_update=current_datetime
        )
        db.begin()
        db.add(item)
        db.flush()

        addition = Feature(
            rid_items=item.rid
        )
        db.add(addition)
        db.commit()
        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def updateFeature(db: Session, target:schema_item.FeatureUpdate):
    try:
        param_item = ItemCommon(
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

        item = Item(
            rid_items=target.rid_items,
            rid_users=target.rid_users,
            rid_users_review=None,
            type=ItemType.STORY.value,
            title=target.title,
            detail=target.detail,
            datetime_entry=current_datetime,
            datetime_update=current_datetime
        )
        db.begin()
        db.add(item)
        db.flush()

        addition = Story(
            rid_items=item.rid,
            datetime_start=target.datetime_start,
            datetime_end=target.datetime_end
        )
        db.add(addition)
        db.commit()
        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def updateStory(db: Session, target:schema_item.StoryUpdate):
    try:
        param_item = ItemCommon(
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

        item = Item(
            rid_items=target.rid_items,
            rid_users=target.rid_users,
            rid_users_review=None,
            type=ItemType.TASK.value,
            title=target.title,
            detail=target.detail,
            datetime_entry=current_datetime,
            datetime_update=current_datetime
        )
        db.begin()
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
        db.commit()
        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def updateTask(db: Session, target:schema_item.TaskUpdate):
    try:
        param_item = ItemCommon(
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


def createBug(db: Session, target:schema_item.BugCreate):
    try:
        current_datetime = _getCurrentDatetime()

        item = Item(
            rid_items=target.rid_items,
            rid_users=target.rid_users,
            rid_users_review=None,
            type=ItemType.BUG.value,
            title=target.title,
            detail=target.detail,
            datetime_entry=current_datetime,
            datetime_update=current_datetime
        )
        db.begin()
        db.add(item)
        db.flush()

        addition = Bug(
            rid_items=item.rid,
            workload=target.workload
        )
        db.add(addition)
        db.commit()
        db.refresh(item)
        return item

    except Exception as e:
        db.rollback()
        raise e


def updateBug(db: Session, target:schema_item.BugUpdate):
    try:
        param_item = ItemCommon(
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

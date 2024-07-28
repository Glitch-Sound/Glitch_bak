from sqlalchemy import Text                     # type: ignore
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
from model.user import User


class ItemType(Enum):
    PROJECT = 1
    EVENT   = 2
    FEATURE = 3
    STORY   = 4
    TASK    = 5


def getCurrentDatetime():
    current_utc_time = datetime.now(pytz.timezone('Asia/Tokyo'))
    current_datetime = current_utc_time.isoformat()
    return current_datetime


def getItems(db: Session, rid_project: int):
    try:
        t0 = aliased(Item, name='t0')
        query_base = db.query(
            t0.rid,
            t0.rid_items,
            t0.rid_users,
            t0.type,
            t0.state,
            t0.risk,
            t0.title,
            t0.detail,
            t0.result,
            t0.datetime_entry,
            t0.datetime_update,
            func.cast(t0.rid, Text).label('path')
        ).filter(t0.rid == rid_project)

        query_recursive = query_base.cte(name='targets', recursive=True)

        n = aliased(Item, name='n')
        t = aliased(query_recursive, name='t')

        query_recursive = query_recursive.union_all(
            db.query(
                n.rid,
                n.rid_items,
                n.rid_users,
                n.type,
                n.state,
                n.risk,
                n.title,
                n.detail,
                n.result,
                n.datetime_entry,
                n.datetime_update,
                (t.c.path + '-' + func.cast(n.rid, Text)).label('path')
            ).join(t, t.c.rid == n.rid_items)
        )

        query_final = db.query(
            query_recursive.c.rid,
            query_recursive.c.type,
            query_recursive.c.state,
            query_recursive.c.risk,
            query_recursive.c.title,
            query_recursive.c.detail,
            query_recursive.c.result,
            query_recursive.c.datetime_entry,
            query_recursive.c.datetime_update,
            User.name.label('name'),
            Project.datetime_start.label('project_datetime_start'),
            Project.datetime_end.label('project_datetime_end'),
            Event.datetime_end.label('event_datetime_end'),
            Story.datetime_start.label('story_datetime_start'),
            Story.datetime_end.label('story_datetime_end'),
            Task.priority.label('task_priority'),
            Task.type.label('task_type'),
            Task.workload.label('task_workload'),
            Task.number_completed.label('task_number_completed'),
            Task.number_total.label('task_number_total'))\
        .outerjoin(User,  User.rid == query_recursive.c.rid_users)\
        .outerjoin(Project, Project.rid_items == query_recursive.c.rid)\
        .outerjoin(Event, Event.rid_items == query_recursive.c.rid)\
        .outerjoin(Feature, Feature.rid_items == query_recursive.c.rid)\
        .outerjoin(Story, Story.rid_items == query_recursive.c.rid)\
        .outerjoin(Task, Task.rid_items == query_recursive.c.rid)\
        .order_by(query_recursive.c.path)

        result = query_final.all()
        return result

    except Exception as e:
        raise e


def getProjects(db: Session):
    try:
        query = db.query(
            Item.rid,
            Item.state,
            Item.risk,
            Item.title,
            Item.detail,
            Item.result,
            Item.datetime_entry,
            Item.datetime_update,
            User.name.label('name'),
            Project.datetime_start.label('project_datetime_start'),
            Project.datetime_end.label('project_datetime_end'))\
        .outerjoin(User,  User.rid == Item.rid_users)\
        .outerjoin(Project, Project.rid_items == Item.rid)\
        .filter(Item.type == ItemType.PROJECT.value)\
        .order_by(Item.rid)
         
        result = query.all()
        return result

    except Exception as e:
        raise e


def createProject(db: Session, target:schema_item.ProjectCreate):
    try:
        current_datetime = getCurrentDatetime()

        item = Item(
            rid_users=target.rid_user,
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
    

def createEvent(db: Session, target:schema_item.EventCreate):
    try:
        current_datetime = getCurrentDatetime()

        item = Item(
            rid_items=target.rid_items,
            rid_users=target.rid_user,
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


def createFeature(db: Session, target:schema_item.FeatureCreate):
    try:
        current_datetime = getCurrentDatetime()

        item = Item(
            rid_items=target.rid_items,
            rid_users=target.rid_user,
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


def createStory(db: Session, target:schema_item.StoryCreate):
    try:
        current_datetime = getCurrentDatetime()

        item = Item(
            rid_items=target.rid_items,
            rid_users=target.rid_user,
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


def createTask(db: Session, target:schema_item.TaskCreate):
    try:
        current_datetime = getCurrentDatetime()

        item = Item(
            rid_items=target.rid_items,
            rid_users=target.rid_user,
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

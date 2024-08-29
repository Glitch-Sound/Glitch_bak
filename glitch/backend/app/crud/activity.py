from sqlalchemy import Text                     # type: ignore
from sqlalchemy.orm import Session, aliased     # type: ignore
from sqlalchemy.sql import func                 # type: ignore
from sqlalchemy.sql import select               # type: ignore

import pytz                                     # type: ignore
from datetime import datetime

import sys
sys.path.append('~/app')

from crud.common import getCurrentDate, getCurrentDatetime
from schema import activity as schema_activity
from model.activity import Activity
from model.user import User


def getActivities(db: Session, rid_items: int):
    try:
        query = db.query(
            Activity.rid,
            Activity.activity,
            Activity.datetime_entry,
            Activity.datetime_update,
            User.rid.label('rid_users'),
            User.name.label('name')
        )\
        .outerjoin(User,  User.rid == Activity.rid_users)\
        .filter(Activity.rid_items == rid_items)\
        .order_by(Activity.rid)
         
        result = query.all()
        return result

    except Exception as e:
        raise e


def createActivity(db: Session, target:schema_activity.ActivityCreate):
    try:
        current_datetime = getCurrentDatetime()

        db.begin()
        activity = Activity(
            rid_items=target.rid_items,
            rid_users=target.rid_users,
            activity=target.activity,
            datetime_entry=current_datetime,
            datetime_update=current_datetime
        )
        db.add(activity)
        db.commit()
        db.refresh(activity)
        return activity

    except Exception as e:
        db.rollback()
        raise e


def updateActivity(db: Session, target:schema_activity.ActivityUpdate):
    try:
        current_datetime = getCurrentDatetime()

        activity = db.query(Activity).filter(Activity.rid == target.rid)
        activity.update({
            Activity.activity: target.activity
        })

        activity_updated = activity.first()
        return activity_updated

    except Exception as e:
        db.rollback()
        raise e


def deleteActivity(db: Session, rid: int):
    try:
        current_datetime = getCurrentDatetime()

        db.begin()
        item = db.query(Activity).filter(Activity.rid == rid)
        item.update({
            Activity.is_deleted: 1,
            Activity.datetime_update: current_datetime
        })
        db.commit()

    except Exception as e:
        raise e

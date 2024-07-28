from sqlalchemy import Text                     # type: ignore
from sqlalchemy.orm import Session, aliased     # type: ignore
from sqlalchemy.sql import func                 # type: ignore
from sqlalchemy.sql import select               # type: ignore

import pytz                                     # type: ignore
from datetime import datetime

import sys
sys.path.append('~/app')

from schema import activity as schema_activity
from model.activity import Activity
from model.user import User


# TODO:共通化.
def getCurrentDatetime():
    current_utc_time = datetime.now(pytz.timezone('Asia/Tokyo'))
    current_datetime = current_utc_time.isoformat()
    return current_datetime


def getActivities(db: Session, rid_items: int):
    try:
        query = db.query(
            Activity.rid,
            Activity.rid_items,
            Activity.state_pre,
            Activity.state_post,
            Activity.activity,
            Activity.datetime_entry,
            Activity.datetime_update,
            User.rid.label('rid_users'),
            User.name.label('name')
        )\
        .outerjoin(User,  User.rid == Activity.rid_users)\
        .order_by(Activity.rid)
         
        result = query.all()
        return result

    except Exception as e:
        raise e


def createActivity(db: Session, target:schema_activity.ActivityCreate):
    try:
        current_datetime = getCurrentDatetime()

        activity = Activity(
            rid_items=target.rid_items,
            rid_users=target.rid_users,
            state_pre=target.state_pre,
            state_post=target.state_post,
            activity=target.activity,
            datetime_entry=target.datetime_entry,
            datetime_update=target.datetime_update
        )
        db.begin()
        db.add(activity)
        db.commit()
        db.refresh(activity)
        return activity

    except Exception as e:
        db.rollback()
        raise e

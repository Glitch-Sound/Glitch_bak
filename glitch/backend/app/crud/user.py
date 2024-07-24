from sqlalchemy.orm import Session  # type: ignore

from enum import Enum

import sys
sys.path.append('~/app')

from model.user import User
from schema import user as schema_user


class Authority(Enum):
    USER  = 0
    ADMIN = 1


def getUsers(db: Session):
    try:
        return db.query(User).all()

    except Exception as e:
        raise e


def getUser(db: Session, rid_users: int):
    try:
        return db.query(User).filter(rid_users == rid_users).one()

    except Exception as e:
        raise e


def createUser(db: Session, target: schema_user.UserCreate):
    try:
        user = User(
             name_user=target.name_user,
             name_display=target.name_display,
             password=target.password,
             is_admin=target.is_admin
        )
        db.begin()
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    except Exception as e:
        db.rollback()
        raise e

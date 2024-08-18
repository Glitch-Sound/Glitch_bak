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
        return db.query(User).filter(User.is_deleted == 0).all()

    except Exception as e:
        raise e


def getUser(db: Session, rid_users: int):
    try:
        return db.query(User).filter(User.rid_users == rid_users).one()

    except Exception as e:
        raise e


def createUser(db: Session, target: schema_user.UserCreate):
    try:
        user = User(
             user=target.user,
             password=target.password,
             name=target.name,
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


def updateUser(db: Session, target: schema_user.UserUpdate):
    try:
        db.begin()
        user = db.query(User).filter(User.rid == target.rid)
        user.update({
            User.user: target.user,
            User.password: target.password,
            User.name: target.name,
            User.is_admin: target.is_admin
        })
        db.commit()

        user_updated = user.first()
        db.refresh(user_updated)
        return user_updated

    except Exception as e:
        db.rollback()
        raise e


def deleteUser(db: Session, rid: int):
    try:
        db.begin()
        user = db.query(User).filter(User.rid == rid)
        user.update({
            User.is_deleted: 1
        })
        db.commit()

    except Exception as e:
        db.rollback()
        raise e

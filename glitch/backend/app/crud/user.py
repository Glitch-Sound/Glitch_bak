from sqlalchemy.orm import Session  # type: ignore

from enum import Enum

import sys
sys.path.append('~/app')

from model.user import User


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


def createUser(db: Session, name: str, password: str, is_admin: int):
    try:
        user = User(
             name=name, password=password, is_admin=is_admin
        )
        db.begin()
        db.add(user)
        db.commit()

    except Exception as e:
        db.rollback()
        raise e

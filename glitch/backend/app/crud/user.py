import bcrypt                       # type: ignore
from sqlalchemy.orm import Session  # type: ignore

from enum import Enum

import sys
sys.path.append('~/app')

from model.user import User
from schema import user as schema_user


class Authority(Enum):
    USER  = 0
    ADMIN = 1


def _createHashPassword(password: str) -> str:
    password_bytes = password.encode('utf-8')
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed.decode('utf-8')


def _verifyHashPassword(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def getUsers(db: Session):
    try:
        query = db.query(
            User
        )\
        .filter(User.is_deleted == 0)\
        .order_by(User.rid)

        result = query.all()
        return result

    except Exception as e:
        raise e


def getUser(db: Session, rid_users: int):
    try:
        query = db.query(
            User
        )\
        .filter(
            User.is_deleted == 0,
            User.rid == rid_users
        )

        result = query.one()
        return result

    except Exception as e:
        raise e


def createUser(db: Session, target: schema_user.UserCreate):
    try:
        user = User(
             user=target.user,
             password=_createHashPassword(target.password),
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
            User.password: _createHashPassword(target.password),
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


def login(db: Session, target: schema_user.Login):
    try:
        user = db.query(User).filter(User.user == target.user).first()
        if user is None:
            return None
        
        if not _verifyHashPassword(target.password, user.password):
            return None

        return user

    except Exception as e:
        raise e

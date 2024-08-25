from sqlalchemy import Column, Integer, String, DateTime    # type: ignore
from sqlalchemy.orm import relationship                     # type: ignore

import sys
sys.path.append('~/app')

from database import Base


class User(Base):
    __tablename__ = 'users'

    rid        = Column(Integer, primary_key=True)
    user       = Column(String, index=True, unique=True)
    password   = Column(String, default='' )
    name       = Column(String, default='')
    is_admin   = Column(Integer, index=True, default=0)
    is_deleted = Column(Integer, index=True, default=0)

    items          = relationship('Item', foreign_keys='Item.rid_users', back_populates='user')
    items_review   = relationship('Item', foreign_keys='Item.rid_users_review', back_populates='user_review')
    activities     = relationship('Activity', back_populates='user')
    summaries_user = relationship('SummaryUser', back_populates='user')


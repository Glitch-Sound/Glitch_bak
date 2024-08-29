from sqlalchemy import Column, ForeignKey, Integer, String  # type: ignore
from sqlalchemy.orm import relationship                     # type: ignore

import sys
sys.path.append('~/app')

from database import Base


class Activity(Base):
    __tablename__ = 'activities'

    rid             = Column(Integer, primary_key=True)
    rid_items       = Column(Integer, ForeignKey('items.rid'))
    rid_users       = Column(Integer, ForeignKey('users.rid'))
    activity        = Column(String, default='')
    datetime_entry  = Column(String, default='')
    datetime_update = Column(String, default='')
    is_deleted      = Column(Integer, index=True, default=0)

    items = relationship('Item', back_populates='activity')
    user  = relationship('User', back_populates='activities')

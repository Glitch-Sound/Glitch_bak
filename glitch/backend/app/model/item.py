from sqlalchemy import Column, ForeignKey, Integer, String  # type: ignore
from sqlalchemy.orm import relationship                     # type: ignore

import sys
sys.path.append('~/app')

from database import Base


class Item(Base):
    __tablename__ = 'items'

    rid             = Column(Integer, primary_key=True)
    rid_items       = Column(Integer, ForeignKey('items.rid'))
    rid_users       = Column(Integer, ForeignKey('users.rid'))
    type            = Column(Integer, index=True, default=0)
    state           = Column(Integer, index=True, default=1)
    title           = Column(String, index=True)
    detail          = Column(String)
    result          = Column(String)
    datetime_entry  = Column(String)
    datetime_update = Column(String)
    is_deleted      = Column(Integer, index=True, default=0)

    parent  = relationship("Item", remote_side=[rid], backref='children')
    project = relationship('Project', back_populates='items')
    event   = relationship('Event', back_populates='items')
    feature = relationship('Feature', back_populates='items')
    story   = relationship('Story', back_populates='items')
    task    = relationship('Task', back_populates='items')
    user    = relationship('User', back_populates='items')

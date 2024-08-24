from sqlalchemy import Column, ForeignKey, Integer, String  # type: ignore
from sqlalchemy.orm import relationship                     # type: ignore

import sys
sys.path.append('~/app')

from database import Base


class Item(Base):
    __tablename__ = 'items'

    rid              = Column(Integer, primary_key=True)
    rid_users        = Column(Integer, ForeignKey('users.rid'))
    rid_users_review = Column(Integer, ForeignKey('users.rid'), nullable=True)
    path_sort        = Column(Integer, index=True, default=0)
    id_project       = Column(Integer, index=True, default=0)
    type             = Column(Integer, index=True, default=0)
    state            = Column(Integer, index=True, default=1)
    risk             = Column(Integer, index=True, default=0)
    risk_factors     = Column(Integer, default=0)
    priority         = Column(Integer, index=True, default=0)
    title            = Column(String, default='')
    detail           = Column(String, default='')
    result           = Column(String, default='')
    datetime_entry   = Column(String, default='')
    datetime_update  = Column(String, default='')
    is_deleted       = Column(Integer, index=True, default=0)

    ancestors = relationship('Tree', foreign_keys='Tree.rid_descendant', back_populates='descendant', cascade="all, delete-orphan")
    descendants = relationship('Tree', foreign_keys='Tree.rid_ancestor', back_populates='ancestor', cascade="all, delete-orphan")

    project     = relationship('Project', back_populates='items')
    event       = relationship('Event', back_populates='items')
    feature     = relationship('Feature', back_populates='items')
    story       = relationship('Story', back_populates='items')
    task        = relationship('Task', back_populates='items')
    bug         = relationship('Bug', back_populates='items')
    activity    = relationship('Activity', back_populates='items')
    user        = relationship('User', foreign_keys=[rid_users], back_populates='items')
    user_review = relationship('User', foreign_keys=[rid_users_review], back_populates='items_review')
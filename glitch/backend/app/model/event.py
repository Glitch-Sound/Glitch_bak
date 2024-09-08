from sqlalchemy import Column, ForeignKey, Integer, String  # type: ignore
from sqlalchemy.orm import relationship                     # type: ignore

import sys
sys.path.append('~/app')

from database import Base


class Event(Base):
    __tablename__ = 'events'

    rid          = Column(Integer, primary_key=True)
    rid_items    = Column(Integer, ForeignKey('items.rid'))
    datetime_end = Column(String)

    items = relationship('Item', back_populates='event')

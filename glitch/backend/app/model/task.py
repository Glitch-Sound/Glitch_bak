from sqlalchemy import Column, ForeignKey, Integer  # type: ignore
from sqlalchemy.orm import relationship             # type: ignore

import sys
sys.path.append('~/app')

from database import Base


class Task(Base):
    __tablename__ = 'tasks'

    rid              = Column(Integer, primary_key=True)
    rid_items        = Column(Integer, ForeignKey('items.rid'))
    type             = Column(Integer)
    workload         = Column(Integer)
    number_completed = Column(Integer)
    number_total     = Column(Integer)

    items = relationship('Item', back_populates='task')

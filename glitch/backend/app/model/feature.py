from sqlalchemy import Column, ForeignKey, Integer  # type: ignore
from sqlalchemy.orm import relationship             # type: ignore

import sys
sys.path.append('~/app')

from database import Base


class Feature(Base):
    __tablename__ = 'features'

    rid                   = Column(Integer, primary_key=True)
    rid_items             = Column(Integer, ForeignKey('items.rid'))
    task_workload         = Column(Integer, default=0)
    task_number_completed = Column(Integer, default=0)
    task_number_total     = Column(Integer, default=0)
    bug_workload          = Column(Integer, default=0)

    items = relationship('Item', back_populates='feature')

from sqlalchemy import Column, ForeignKey, Integer, String  # type: ignore
from sqlalchemy.orm import relationship                     # type: ignore

import sys
sys.path.append('~/app')

from database import Base


class Story(Base):
    __tablename__ = 'stories'

    rid                     = Column(Integer, primary_key=True)
    rid_items               = Column(Integer, ForeignKey('items.rid'))
    datetime_start          = Column(String, default='')
    datetime_end            = Column(String, default='')
    task_count_completed    = Column(Integer, default=0)
    task_count_total        = Column(Integer, default=0)
    task_workload_completed = Column(Integer, default=0)
    task_workload_total     = Column(Integer, default=0)
    task_number_completed   = Column(Integer, default=0)
    task_number_total       = Column(Integer, default=0)
    bug_count_completed     = Column(Integer, default=0)
    bug_count_total         = Column(Integer, default=0)
    bug_workload_completed  = Column(Integer, default=0)
    bug_workload_total      = Column(Integer, default=0)

    items = relationship('Item', back_populates='story')

from sqlalchemy import Column, ForeignKey, Integer  # type: ignore
from sqlalchemy.orm import relationship             # type: ignore

import sys
sys.path.append('~/app')

from database import Base


class SummaryItem(Base):
    __tablename__ = 'summaries_item'

    rid                   = Column(Integer, primary_key=True)
    rid_items             = Column(Integer, ForeignKey('items.rid'))

    task_count_idle       = Column(Integer, default=0)
    task_count_run        = Column(Integer, default=0)
    task_count_alert      = Column(Integer, default=0)
    task_count_review     = Column(Integer, default=0)
    task_count_complete   = Column(Integer, default=0)
    task_count_total      = Column(Integer, default=0)

    task_workload_total   = Column(Integer, default=0)
    task_number_completed = Column(Integer, default=0)
    task_number_total     = Column(Integer, default=0)

    bug_count_idle        = Column(Integer, default=0)
    bug_count_run         = Column(Integer, default=0)
    bug_count_alert       = Column(Integer, default=0)
    bug_count_review      = Column(Integer, default=0)
    bug_count_complete    = Column(Integer, default=0)
    bug_count_total       = Column(Integer, default=0)

    bug_workload_total    = Column(Integer, default=0)

    items = relationship('Item', back_populates='summary_item')

from sqlalchemy import Column, String, Integer  # type: ignore

import sys
sys.path.append('~/app')

from database import Base


class Log(Base):
    __tablename__ = 'logs'

    rid              = Column(Integer, primary_key=True)
    rid_project      = Column(Integer, default=0)
    workload         = Column(Integer, default=0)
    number_completed = Column(Integer, default=0)
    number_total     = Column(Integer, default=0)
    task_total       = Column(Integer, default=0)
    task_idle        = Column(Integer, default=0)
    task_run         = Column(Integer, default=0)
    task_review      = Column(Integer, default=0)
    task_completed   = Column(Integer, default=0)
    datetime_entry   = Column(String, default='', index=True)

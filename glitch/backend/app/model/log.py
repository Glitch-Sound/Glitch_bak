from sqlalchemy import Column, String, Integer  # type: ignore

import sys
sys.path.append('~/app')

from database import Base


class Log(Base):
    __tablename__ = 'logs'

    rid                     = Column(Integer, primary_key=True)
    rid_project             = Column(Integer, default=0)
    task_workload_completed = Column(Integer, default=0)
    task_workload_total     = Column(Integer, default=0)
    task_number_completed   = Column(Integer, default=0)
    task_number_total       = Column(Integer, default=0)
    task_total              = Column(Integer, default=0)
    task_idle               = Column(Integer, default=0)
    task_run                = Column(Integer, default=0)
    task_review             = Column(Integer, default=0)
    task_completed          = Column(Integer, default=0)
    bug_workload_completed  = Column(Integer, default=0)
    bug_workload_total      = Column(Integer, default=0)
    bug_total               = Column(Integer, default=0)
    bug_idle                = Column(Integer, default=0)
    bug_run                 = Column(Integer, default=0)
    bug_review              = Column(Integer, default=0)
    bug_completed           = Column(Integer, default=0)
    datetime_entry          = Column(String, default='', index=True)



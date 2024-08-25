from sqlalchemy import Column, ForeignKey, String, Integer      # type: ignore
from sqlalchemy.orm import relationship                         # type: ignore

import sys
sys.path.append('~/app')

from database import Base


class SummaryUser(Base):
    __tablename__ = 'summaries_user'

    rid                   = Column(Integer, primary_key=True)
    rid_users             = Column(Integer, ForeignKey('users.rid'))
    id_project            = Column(Integer, index=True, default=0)
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
    date_entry            = Column(String, index=True, default='')

    user  = relationship('User', back_populates='summaries_user')

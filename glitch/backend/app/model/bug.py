from sqlalchemy import Column, ForeignKey, Integer  # type: ignore
from sqlalchemy.orm import relationship             # type: ignore

import sys
sys.path.append('~/app')

from database import Base


class Bug(Base):
    __tablename__ = 'bugs'

    rid              = Column(Integer, primary_key=True)
    rid_items        = Column(Integer, ForeignKey('items.rid'))
    priority         = Column(Integer, default=0)
    workload         = Column(Integer, default=0)

    items = relationship('Item', back_populates='task')

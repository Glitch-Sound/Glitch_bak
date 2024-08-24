from sqlalchemy import ForeignKey, Column, Integer      # type: ignore
from sqlalchemy.orm import relationship                 # type: ignore

import sys
sys.path.append('~/app')

from database import Base


class Tree(Base):
    __tablename__ = 'trees'

    rid_ancestor   = Column(Integer, ForeignKey('items.rid'), primary_key=True)
    rid_descendant = Column(Integer, ForeignKey('items.rid'), primary_key=True)

    ancestor = relationship('Item', foreign_keys=[rid_ancestor], back_populates='descendants')
    descendant = relationship('Item', foreign_keys=[rid_descendant], back_populates='ancestors')

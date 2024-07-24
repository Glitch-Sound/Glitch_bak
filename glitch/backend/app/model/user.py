from sqlalchemy import Column, Integer, String, DateTime    # type: ignore
from sqlalchemy.orm import relationship                     # type: ignore

import sys
sys.path.append('~/app')

from database import Base


class User(Base):
    __tablename__ = 'users'

    rid          = Column(Integer, primary_key=True)
    name_user    = Column(String, index=True, unique=True)
    name_display = Column(String, index=True)
    password     = Column(String)
    is_admin     = Column(Integer, index=True)
    is_deleted   = Column(Integer, index=True, default=0)

    items = relationship('Item', back_populates='user')

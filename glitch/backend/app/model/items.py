from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import sys
sys.path.append("~/app")

from database import Base

class Item(Base):
    __tablename__ = "items"

    rid   = Column(Integer, primary_key=True)
    title = Column(String,  index=True)

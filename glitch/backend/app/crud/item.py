from sqlalchemy.orm import Session

import sys
sys.path.append("~/app")

from model import items

def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(items.Item).offset(skip).limit(limit).all()

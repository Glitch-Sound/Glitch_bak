from sqlalchemy import Text         # type: ignore
from sqlalchemy.orm import Session  # type: ignore

import sys
sys.path.append('~/app')

from model.log import Log


def getLogs(db: Session, id_project: int):
    try:
        return db.query(Log).filter(id_project == id_project).all()

    except Exception as e:
        raise e

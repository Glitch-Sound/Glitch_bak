from fastapi import Depends, APIRouter, HTTPException   # type: ignore
from sqlalchemy.orm import Session                      # type: ignore

import sys
sys.path.append('~/app')

from database import get_db
from schema import log as schema_log
from crud import log as crud_log


router = APIRouter()

@router.get('/log/{rid_project}', response_model=schema_log.Log)
def get_users(rid_project: int, db: Session = Depends(get_db)):
    try:
        result = crud_log.getLogs(db, rid_project)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')

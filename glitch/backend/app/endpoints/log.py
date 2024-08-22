import traceback
from fastapi import Depends, APIRouter, HTTPException, status   # type: ignore
from sqlalchemy.orm import Session                              # type: ignore

import sys
sys.path.append('~/app')

from database import get_db
from schema import log as schema_log
from crud import log as crud_log


router = APIRouter()

@router.get('/log/{id_project}', response_model=schema_log.Log)
def get_users(id_project: int, db: Session = Depends(get_db)):
    try:
        result = crud_log.getLogs(db, id_project)
        return result

    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'error: {str(e)}')

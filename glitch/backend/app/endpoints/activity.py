from fastapi import Depends, APIRouter, HTTPException   # type: ignore
from sqlalchemy.orm import Session                      # type: ignore

import sys
sys.path.append('~/app')

from database import get_db
from schema import activity as schema_activity
from crud import activity as crud_activity


router = APIRouter()

@router.get('/activities/{rid_items}', response_model=list[schema_activity.Activity])
def get_items(rid_items: int, db: Session = Depends(get_db)):
    try:
        result = crud_activity.getActivities(db, rid_items=rid_items)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')


@router.post('/activity/', response_model=schema_activity.Activity)
def create_project(target:schema_activity.ActivityCreate, db: Session = Depends(get_db)):
    try:
        result = crud_activity.createActivity(db, target)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')

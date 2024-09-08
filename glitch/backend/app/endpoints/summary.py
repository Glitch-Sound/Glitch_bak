import traceback
from fastapi import Depends, APIRouter, HTTPException, status    # type: ignore
from sqlalchemy.orm import Session                                      # type: ignore

import sys
sys.path.append('~/app')

from database import get_db
from schema import summary as schema_summary
from crud import summary as crud_summary


router = APIRouter()

@router.get('/summaries/item/{rid_items}', response_model=list[schema_summary.SummaryItem])
def get_summary_item(rid_items: int, db: Session = Depends(get_db)):
    try:
        result = crud_summary.getSummariesItem(db, rid_items)
        return result

    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'error: {str(e)}')


@router.get('/summaries/user/{id_project}/{rid_users}', response_model=list[schema_summary.SummaryUser])
def get_summary_item(id_project: int, rid_users: int, db: Session = Depends(get_db)):
    try:
        result = crud_summary.getSummariesUser(db, id_project, rid_users)
        return result

    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'error: {str(e)}')


@router.get('/ancestors/item/{rid}', response_model=list[schema_summary.Ancestor])
def get_ancestor_item(rid: int, db: Session = Depends(get_db)):
    try:
        result = crud_summary.getAncestorsItem(db, rid)
        return result

    except Exception as e:
        print(traceback.format_exc())
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f'error: {str(e)}')

from fastapi import Depends, APIRouter, HTTPException   # type: ignore
from sqlalchemy.orm import Session                      # type: ignore

import sys
sys.path.append('~/app')

from database import get_db
from schema import user as schema_user
from crud import user as crud_user

router = APIRouter()


@router.get('/users/', response_model=list[schema_user.User])
def get_users(db: Session = Depends(get_db)):
    try:
        result = crud_user.getUsers(db)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')


@router.get('/user/{rid_users}', response_model=schema_user.User)
def get_users(rid_users: int, db: Session = Depends(get_db)):
    try:
        result = crud_user.getUser(db, rid_users)
        print(result)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')


@router.post('/user/', response_model=schema_user.User)
def create_user(target:schema_user.UserCreate, db: Session = Depends(get_db)):
    try:
        result = crud_user.createUser(db, target)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')

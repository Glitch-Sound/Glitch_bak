from fastapi import Depends, APIRouter, HTTPException   # type: ignore
from sqlalchemy.orm import Session                      # type: ignore

import sys
sys.path.append('~/app')

from database import get_db
from schema import item as schema_item
from crud import item as crud_item


router = APIRouter()

@router.get('/items/{rid_project}', response_model=list[schema_item.Item])
def get_items(rid_project: int, db: Session = Depends(get_db)):
    try:
        result = crud_item.getItems(db, rid_project=rid_project)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')


@router.get('/projects/', response_model=list[schema_item.Project])
def get_items(db: Session = Depends(get_db)):
    try:
        result = crud_item.getProjects(db)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')


@router.post('/project/', response_model=schema_item.Item)
def create_project(target:schema_item.ProjectCreate, db: Session = Depends(get_db)):
    try:
        result = crud_item.createProject(db, target)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')


@router.post('/event/', response_model=schema_item.Item)
def create_event(target:schema_item.EventCreate, db: Session = Depends(get_db)):
    try:
        result = crud_item.createEvent(db, target)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')


@router.post('/feature/', response_model=schema_item.Item)
def create_feature(target:schema_item.FeatureCreate, db: Session = Depends(get_db)):
    try:
        result = crud_item.createFeature(db, target)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')


@router.post('/story/', response_model=schema_item.Item)
def create_story(target:schema_item.StoryCreate, db: Session = Depends(get_db)):
    try:
        result = crud_item.createStory(db, target)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')


@router.post('/task/', response_model=schema_item.Item)
def create_task(target:schema_item.TaskCreate, db: Session = Depends(get_db)):
    try:
        result = crud_item.createTask(db, target)
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')

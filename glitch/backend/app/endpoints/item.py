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


@router.post('/project/', response_model=schema_item.ProjectCreate)
def create_project(target=schema_item.ProjectCreate, db: Session = Depends(get_db)):
    try:
        result = crud_item.createProject(
            db, rid_user=target.rid_user,
            title=target.title, detail=target.detail, result=target.result,
            datetime_start=target.datetime_start, datetime_end=target.datetime_end
        )
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')


@router.post('/event/', response_model=schema_item.EventCreate)
def create_event(target=schema_item.EventCreate, db: Session = Depends(get_db)):
    try:
        result = crud_item.createEvent(
            db, rid_project=target.rid_project, rid_user=target.rid_user,
            title=target.title, detail=target.detail, result=target.result,
            datetime_end=target.datetime_end
        )
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')


@router.post('/feature/', response_model=schema_item.FeatureCreate)
def create_feature(target=schema_item.FeatureCreate, db: Session = Depends(get_db)):
    try:
        result = crud_item.createFeature(
            db, rid_event=target.rid_event, rid_user=target.rid_user,
            title=target.title, detail=target.detail, result=target.result
        )
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')


@router.post('/story/', response_model=schema_item.StoryCreate)
def create_story(target=schema_item.StoryCreate, db: Session = Depends(get_db)):
    try:
        result = crud_item.createStory(
            db, rid_feature=target.rid_feature, rid_user=target.rid_user,
            title=target.title, detail=target.detail, result=target.result,
            datetime_start=target.datetime_start, datetime_end=target.datetime_end
        )
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')


@router.post('/task/', response_model=schema_item.TaskCreate)
def create_task(target=schema_item.TaskCreate, db: Session = Depends(get_db)):
    try:
        result = crud_item.createTask(
            db, rid_story=target.rid_story, rid_user=target.rid_user,
            title=target.title, detail=target.detail, result=target.result,
            type=target.type, workload=target.workload, number_completed=target.number_completed, number_total=target.number_total
        )
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')


# TODO:削除
@router.get('/addItems/')
def add_items(db: Session = Depends(get_db)):
    try:
        crud_item.addItems(db)
        return {'message": "success'}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f'error: {str(e)}')

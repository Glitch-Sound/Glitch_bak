from pydantic import BaseModel  # type: ignore
from typing import Optional


class Item(BaseModel):
    rid: int
    type: int
    state: int
    risk: int
    title: str
    detail: str
    result: str
    datetime_entry: str
    datetime_update: str
    name: Optional[str] = None
    project_datetime_start: Optional[str] = None
    project_datetime_end: Optional[str] = None
    event_datetime_end: Optional[str] = None
    story_datetime_start: Optional[str] = None
    story_datetime_end: Optional[str] = None
    task_type: Optional[int] = None
    task_workload: Optional[int] = None
    task_number_completed: Optional[int] = None
    task_number_total: Optional[int] = None

    class Config:
        orm_mode = True


class Project(BaseModel):
    rid: int
    state: int
    risk: int
    title: str
    detail: str
    result: str
    datetime_entry: str
    datetime_update: str
    name: Optional[str] = None
    project_datetime_start: Optional[str] = None
    project_datetime_end: Optional[str] = None

    class Config:
        orm_mode = True


class ProjectCreate(BaseModel):
    rid_user: int
    title: str
    detail: str
    datetime_start: str
    datetime_end: str

    class Config:
        orm_mode = True


class EventCreate(BaseModel):
    rid_project: int
    rid_user: int
    title: str
    detail: str
    datetime_end: str

    class Config:
        orm_mode = True


class FeatureCreate(BaseModel):
    rid_event: int
    rid_user: int
    title: str
    detail: str

    class Config:
        orm_mode = True


class StoryCreate(BaseModel):
    rid_feature: int
    rid_user: int
    title: str
    detail: str
    datetime_start: str
    datetime_end: str

    class Config:
        orm_mode = True


class TaskCreate(BaseModel):
    rid_story: int
    rid_user: int
    title: str
    detail: str
    type: int
    workload: int
    number_completed: int
    number_total: int

    class Config:
        orm_mode = True




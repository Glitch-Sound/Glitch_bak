from pydantic import BaseModel  # type: ignore
from typing import List, Optional


class Item(BaseModel):
    rid: int
    id_project: int
    type: int
    state: int
    risk: int
    risk_factors: int
    priority: int
    title: str
    detail: str
    result: str
    datetime_entry: str
    datetime_update: str
    rid_users: int
    name: Optional[str] = None
    rid_users_review: Optional[int] = None
    name_review: Optional[str] = None
    project_datetime_start: Optional[str] = None
    project_datetime_end: Optional[str] = None
    event_datetime_end: Optional[str] = None
    story_datetime_start: Optional[str] = None
    story_datetime_end: Optional[str] = None
    task_type: Optional[int] = None
    task_workload: Optional[int] = None
    task_number_completed: Optional[int] = None
    task_number_total: Optional[int] = None
    bug_workload: Optional[int] = None

    class Config:
        orm_mode = True


class Project(BaseModel):
    rid: int
    id_project: int
    state: int
    risk: int
    risk_factors: int
    title: str
    detail: str
    result: str
    datetime_entry: str
    datetime_update: str
    rid_users: int
    name: Optional[str] = None
    project_datetime_start: Optional[str] = None
    project_datetime_end: Optional[str] = None

    class Config:
        orm_mode = True


class ProjectCreate(BaseModel):
    rid_users: int
    title: str
    detail: str
    datetime_start: str
    datetime_end: str

    class Config:
        orm_mode = True


class ProjectUpdate(BaseModel):
    rid: int
    state: int
    rid_users: int
    rid_users_review: Optional[int] = None
    title: str
    detail: str
    result: str
    datetime_start: str
    datetime_end: str

    class Config:
        orm_mode = True


class EventCreate(BaseModel):
    id_project: int
    rid_items: int
    rid_users: int
    title: str
    detail: str
    datetime_end: str

    class Config:
        orm_mode = True


class EventUpdate(BaseModel):
    rid: int
    state: int
    rid_users: int
    rid_users_review: Optional[int] = None
    title: str
    detail: str
    result: str
    datetime_end: str

    class Config:
        orm_mode = True


class FeatureCreate(BaseModel):
    id_project: int
    rid_items: int
    rid_users: int
    title: str
    detail: str

    class Config:
        orm_mode = True


class FeatureUpdate(BaseModel):
    rid: int
    state: int
    rid_users: int
    rid_users_review: Optional[int] = None
    title: str
    detail: str
    result: str

    class Config:
        orm_mode = True


class StoryCreate(BaseModel):
    id_project: int
    rid_items: int
    rid_users: int
    title: str
    detail: str
    datetime_start: str
    datetime_end: str

    class Config:
        orm_mode = True


class StoryUpdate(BaseModel):
    rid: int
    state: int
    rid_users: int
    rid_users_review: Optional[int] = None
    title: str
    detail: str
    result: str
    datetime_start: str
    datetime_end: str

    class Config:
        orm_mode = True


class TaskCreate(BaseModel):
    id_project: int
    rid_items: int
    rid_users: int
    title: str
    detail: str
    type: int
    workload: int
    number_completed: int
    number_total: int

    class Config:
        orm_mode = True


class TaskUpdate(BaseModel):
    rid: int
    state: int
    rid_users: int
    rid_users_review: Optional[int] = None
    title: str
    detail: str
    result: str
    type: int
    workload: int
    number_completed: int
    number_total: int

    class Config:
        orm_mode = True


class TaskPriorityUpdate(BaseModel):
    rid: int
    priority: int

    class Config:
        orm_mode = True


class BugCreate(BaseModel):
    id_project: int
    rid_items: int
    rid_users: int
    title: str
    detail: str
    workload: int

    class Config:
        orm_mode = True


class BugUpdate(BaseModel):
    rid: int
    state: int
    rid_users: int
    rid_users_review: Optional[int] = None
    title: str
    detail: str
    result: str
    workload: int

    class Config:
        orm_mode = True


class BugPriorityUpdate(BaseModel):
    rid: int
    priority: int

    class Config:
        orm_mode = True


class ItemHierarchy(BaseModel):
    rid: int
    rid_users: int
    name: str
    type: int
    title: str
    workload_task: Optional[int] = None
    workload_bug: Optional[int] = None
    children: Optional[List['ItemHierarchy']] = None

    class Config:
        orm_mode = True 

class SummaryProject(BaseModel):
    rid: int
    type: int
    state: int
    title: str
    datetime_start: str
    datetime_end: str

    class Config:
        orm_mode = True 

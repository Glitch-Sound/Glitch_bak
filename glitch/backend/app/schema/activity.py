from pydantic import BaseModel  # type: ignore
from typing import Optional


class Activity(BaseModel):
    rid: int
    state_pre: int
    state_post: int
    activity: str
    datetime_entry: str
    datetime_update: str
    rid_users: int
    name: Optional[str] = None

    class Config:
        orm_mode = True


class ActivityCreate(BaseModel):
    rid_items: int
    rid_users: int
    state_pre: int
    state_post: int
    activity: str
    datetime_entry: str
    datetime_update: str

    class Config:
        orm_mode = True

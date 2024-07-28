from pydantic import BaseModel  # type: ignore
from typing import Optional


class Log(BaseModel):
    rid: int
    workload: int
    number_completed: int
    number_total: int
    task_total: int
    task_idle: int
    task_run: int
    task_review: int
    task_completed: int
    datetime_entry: str

    class Config:
        orm_mode = True

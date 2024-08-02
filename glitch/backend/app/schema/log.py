from pydantic import BaseModel  # type: ignore


class Log(BaseModel):
    rid: int
    task_workload_completed: int
    task_workload_total: int
    task_number_completed: int
    task_number_total: int
    task_total: int
    task_idle: int
    task_run: int
    task_review: int
    task_completed: int
    bug_workload_completed: int
    bug_workload_total: int
    bug_total: int
    bug_idle: int
    bug_run: int
    bug_review: int
    bug_completed: int
    datetime_entry: str

    class Config:
        orm_mode = True

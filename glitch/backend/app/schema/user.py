from pydantic import BaseModel  # type: ignore


class User(BaseModel):
    rid: int
    name_user: str
    name_display: str
    password: str
    is_admin: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    name_user: str
    name_display: str
    password: str
    is_admin: int

    class Config:
        orm_mode = True

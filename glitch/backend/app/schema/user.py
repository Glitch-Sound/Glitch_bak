from pydantic import BaseModel  # type: ignore


class User(BaseModel):
    rid: int
    name: str
    password: str
    is_admin: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    name: str
    password: str
    is_admin: int

    class Config:
        orm_mode = True

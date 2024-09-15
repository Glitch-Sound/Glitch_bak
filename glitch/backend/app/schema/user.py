from pydantic import BaseModel


class User(BaseModel):
    rid: int
    user: str
    name: str
    is_admin: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    user: str
    password: str
    name: str
    is_admin: int

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    rid: int
    user: str
    password: str
    name: str
    is_admin: int

    class Config:
        orm_mode = True


class Login(BaseModel):
    user: str
    password: str

    class Config:
        orm_mode = True

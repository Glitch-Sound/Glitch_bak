from pydantic import BaseModel


class Item(BaseModel):
    rid: int
    title: str

    class Config:
        orm_mode = True

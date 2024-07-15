
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import sys
sys.path.append("~/app")

from crud import item
from schema import items
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/items/", response_model=list[items.Item])
def get_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = item.get_items(db, skip=skip, limit=limit)
    return items

@app.get("/")
def read_root():
    return {"message": "Hello World"}




# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./glitch.db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# # ----------------------------------------------------------------------------------------------------

# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship

# class ModelUser(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

# # ----------------------------------------------------------------------------------------------------

# from pydantic import BaseModel

# class SchemaUser(BaseModel):
#     id: int
#     email: str
#     password: str
#     is_active: bool

#     class Config:
#         orm_mode = True

# # ----------------------------------------------------------------------------------------------------

# from sqlalchemy.orm import Session

# # from . import models, schemas

# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(ModelUser).offset(skip).limit(limit).all()

# # ----------------------------------------------------------------------------------------------------

# from fastapi import Depends, FastAPI, HTTPException
# from sqlalchemy.orm import Session

# # from . import crud, models, schemas
# # from .database import SessionLocal, engine

# Base.metadata.create_all(bind=engine)

# app = FastAPI()


# # Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.get("/users/", response_model=list[SchemaUser])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = get_users(db, skip=skip, limit=limit)
#     return users

# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}

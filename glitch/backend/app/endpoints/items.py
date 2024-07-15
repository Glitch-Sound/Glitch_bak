# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from app import crud, model, database

# router = APIRouter()

# def get_db():
#     db = database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.get("/item/", response_model=model.Item)
# def get_item(db: Session = Depends(get_db)):
#     return {"message": "Hello World"}
#     # db_item = crud.get_item(db)
#     # if db_item is None:
#     #     raise HTTPException(status_code=404, detail="item not found")
#     # return db_item

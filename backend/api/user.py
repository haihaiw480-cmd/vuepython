from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud.user import create_user
from database.db import get_db
from models.user import User

router = APIRouter(prefix="")


@router.get("/")
def root():
    return {"message": "Hello World"}


@router.post("/user")
def add_user(data: dict, db: Session = Depends(get_db)):
    return create_user(db, data)


@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    # users = db.query(User).all()
    return {"0000"}

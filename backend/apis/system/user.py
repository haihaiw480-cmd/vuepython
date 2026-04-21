from fastapi import APIRouter, Depends
from database.db import get_db, test_connection
from models.system.user import User
from pydantic import BaseModel, Field
from schemas.response import ResponseModel
from core.exceptions import BizException

from typing import Optional
from utils.response import success, error
from sqlalchemy.ext.asyncio import AsyncSession
from services.system.user_service import UserService
from schemas.system.user import UserQuery, UserLogin

router = APIRouter()
user_service = UserService()


@router.get("/", status_code=200)
async def root():
    return {"message": "Hello World"}


@router.get("/user/{user_id}")
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    return await user_service.get_user(db, user_id=user_id)


@router.get("/user")
async def get_users(
    username: Optional[str] = None,
    user_id: Optional[int] = None,
    db: AsyncSession = Depends(get_db),
):
    return await user_service.get_user(db, username, user_id)


# 注册接口
@router.post("/register")
async def register(
    data: UserQuery,
    db: AsyncSession = Depends(get_db),
):
    return await user_service.create_user(db, data)


@router.post("/login")
async def login(
    params: UserLogin,
    db: AsyncSession = Depends(get_db),
):
    return await user_service.login_by_password(db, params)

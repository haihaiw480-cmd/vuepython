from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud.user import create_user, get_user_all
from database.db import get_db
from models.user import User
from pydantic import BaseModel, Field
from schemas.response import ResponseModel
from schemas.user import UserCreate
from core.exceptions import BizException
from crud.user import get_user_by_username
from utils.jwt import verify_token, create_access_token
from utils.security import verify_password, hash_password
from utils.response import success, error

router = APIRouter(prefix="")


class UserOut(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True


# 注册接口
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    print("user:", user)
    # 1. 校验用户名是否存在
    existing_user = get_user_by_username(db, user.username)
    if existing_user:
        raise BizException(msg="用户名已存在")
    # # 2. 加密密码
    print("password:", user.password)
    print("length:", len(user.password))
    hashed_password = hash_password(user.password)
    print(hashed_password, len(hashed_password))
    # # 3. 创建用户
    user_data = {"username": user.username, "password": hashed_password}
    new_user = create_user(db, user_data)
    return {
        "code": 200,
        "msg": "注册成功",
        "data": {"id": new_user.id, "username": new_user.username},  # type: ignore
    }


@router.get("/", status_code=201)
def root():
    return {"message": "Hello World"}


@router.post("/user")
def add_user(data: dict, db: Session = Depends(get_db)):
    return create_user(db, data)


@router.get("/user", response_model=ResponseModel[list[UserOut]])
def get_user(db: Session = Depends(get_db)):
    users = get_user_all(db)
    return {"code": 200, "msg": "success", "data": users}


@router.post("/login")
def login(data: dict, db: Session = Depends(get_db)):
    # 查用户
    user = db.query(User).filter_by(username=data["username"]).first()
    if not user:
        raise BizException(msg="用户不存在")
    # 校验密码
    print("输入密码:", data["password"])
    print("数据库密码:", user.password)  # type: ignore
    if not verify_password(data["password"], user.password):  # type: ignore
        raise BizException(msg="密码错误")
    # todo 返回token

    token = create_access_token(data)
    print("token:", token)
    return success(data={"access_token": token})


# type: ignore

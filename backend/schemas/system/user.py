from pydantic import BaseModel, Field
from typing import Optional


class UserQuery(BaseModel):
    username: Optional[str] = None
    user_id: Optional[int] = None
    password: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    status: Optional[int] = None
    nickname: Optional[str] = None


class UserLogin(BaseModel):
    username: Optional[str] = Field(..., description='用户名')
    password: Optional[str] = Field(..., description='密码')

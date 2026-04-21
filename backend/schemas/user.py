from pydantic import BaseModel, Field
from typing import Optional


class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, description="用户名，长度3-20")
    password: str = Field(
        ...,
        min_length=6,
        # max_length=20,
        # pattern=r"^(?=.*[A-Z]).+$",
        description="密码6-20位，必须包含大小写字母和数字",
    )


class UserLogin(BaseModel):
    username: Optional[str] = Field(..., description='用户名')
    password: Optional[str] = Field(..., description='密码')

from backend.app.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from typing import Optional


class User(BaseModel):
    __tablename__ = "sys_user"
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, comment="用户名")
    password: Mapped[str] = mapped_column(String(255), nullable=False, comment="密码")
    nickname: Mapped[str] = mapped_column(String(50), comment="昵称")
    phone: Mapped[str] = mapped_column(String(20), comment="手机号")
    email: Mapped[str] = mapped_column(String(100), comment="邮箱")
    status: Mapped[int] = mapped_column(Integer, default=1, comment="状态 1正常 0禁用")

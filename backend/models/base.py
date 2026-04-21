from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import BigInteger, DateTime, Boolean, func


class BaseModel(DeclarativeBase):
    """基本表"""

    id = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    created_at = mapped_column(DateTime, default=func.now())
    updated_at = mapped_column(DateTime, default=func.now(), onupdate=func.now())
    is_deleted = mapped_column(Boolean, default=False)

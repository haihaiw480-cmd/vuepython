# ✔ 字段类型
# ✔ 唯一约束
# ✔ 是否索引


from sqlalchemy import Column, Integer, String
from database.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    # 唯一约束（数据库层）
    username = Column(String)
    password = Column(String)

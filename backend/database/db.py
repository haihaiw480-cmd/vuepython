from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 使用 sqlite 数据库 数据库文件在当前目录 test.db
DATABASE_URL = "sqlite:///./test.db"
# SQLite 默认只能单线程访问 FastAPI 是多线程 → 必须关闭限制
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
# 生成数据库会话（Session）的工厂
SessionLocal = sessionmaker(bind=engine)

# 所有模型类的父类
Base = declarative_base()


# 创建数据库会话 → 提供给接口使用 → 用完自动关闭
def get_db():
    # 生成一个数据库 Session（会话）
    db = SessionLocal()
    try:
        # 把 db 提供给 FastAPI 路由使用
        yield db
    finally:
        # 释放数据库连接（防止泄漏）
        db.close()

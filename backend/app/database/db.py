from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
    AsyncSession,
)
from sqlalchemy.orm import DeclarativeBase
from typing import AsyncGenerator
from sqlalchemy import text
from backend.app.models.system.user import User
from backend.app.models.system.menu import Menu
from backend.app.models.base import BaseModel

DATABASE_URL = "mysql+aiomysql://dev:123456@127.0.0.1:3306/vue_fastapi"

# 1) Engine（异步）
engine = create_async_engine(
    DATABASE_URL,
    echo=True,  # 开发期可开
    pool_pre_ping=True,  # 连接健康检查
)


# 3) Session 工厂（2.x 专用）
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


# 4) 依赖注入（FastAPI）
async def get_db() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSessionLocal() as session:
        yield session


async def test_connection():
    try:

        async with engine.begin() as conn:
            await conn.run_sync(BaseModel.metadata.create_all)
        async with engine.connect() as conn:
            result = await conn.execute(text("SELECT 1"))
            print("✅ 数据库连接成功:", result)
    except Exception as e:
        print("❌ 连接失败:", e)


# asyncio.run(test_connection())

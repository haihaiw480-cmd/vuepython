from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# ===== 1. 数据库地址 =====
# SQLite 文件路径（相对路径）
DATABASE_URL = "sqlite:///./DB/menu.db"

# ===== 2. 创建引擎 =====
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},  # SQLite 多线程支持
    echo=True,  # 打印 SQL（开发环境建议开启）
    pool_pre_ping=True,  # 连接有效性检测（防止断连）
)

# ===== 3. Session 工厂 =====
SessionLocal = sessionmaker(
    autocommit=False,  # 禁用自动提交（必须手动 commit）
    autoflush=False,  # 禁用自动 flush（更可控）
    bind=engine,
)

# ===== 4. ORM 基类 =====
Base = declarative_base()


# ===== 5. 依赖注入：获取数据库 Session =====
def get_menu_db():
    """
    FastAPI 数据库依赖：
    - 每个请求创建一个 Session
    - 请求结束自动关闭
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

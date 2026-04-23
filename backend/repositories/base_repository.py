from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:

    def __init__(self, model, allowed_fields=None):
        self.model = model
        self.allowed_fields = allowed_fields or set()

    def filter_data(self, data):
        if not self.allowed_fields:
            return data
        return {k: v for k, v in data.items() if k in self.allowed_fields}

    async def create(self, db, data):
        data = self.filter_data(data)
        obj = self.model(**data)
        db.add(obj)
        await db.flush()  # 把 SQL 发给数据库（但不提交）
        await db.commit()  # 真正写入数据库（持久化）
        return obj

    async def update(self, db, id: int, data: dict):
        data = self.filter_data(data)

        stmt = update(self.model).where(self.model.id == id).values(**data)
        await db.execute(stmt)

    async def get(self, db: AsyncSession, **kwargs):

        stmt = select(self.model)

        # 自动拼接 where 条件
        conditions = []
        print(kwargs, 'kwargs')
        for key, value in kwargs.items():
            if value is None:
                continue
            # ❗字段白名单（推荐用 allowed_fields）
            if key in self.allowed_fields:
                column = getattr(self.model, key)
                conditions.append(column == value)

        # 默认逻辑删除过滤
        # if hasattr(self.model, "is_deleted"):
        #     conditions.append(self.model.is_deleted == False)
        if conditions:
            stmt = stmt.where(*conditions)
        result = await db.execute(stmt)
        return result.scalars().all()

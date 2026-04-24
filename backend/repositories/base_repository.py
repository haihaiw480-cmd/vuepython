from sqlalchemy import select, update, delete, func
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Optional


class BaseRepository:

    def __init__(self, model, allowed_fields=None):
        self.model = model
        self.allowed_fields = allowed_fields or set()

    def filter_data(self, data):
        if not self.allowed_fields:
            return data
        return {k: v for k, v in data.items() if k in self.allowed_fields}

    def _to_dict(self, obj):
        if isinstance(obj, dict):
            return obj
        if hasattr(obj, "__table__"):
            return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
        return obj

    async def create(self, db, data):
        print(data, 'data')
        data = self.filter_data(data)
        obj = self.model(**data)
        db.add(obj)
        await db.flush()  # 把 SQL 发给数据库（但不提交）
        await db.commit()  # 真正写入数据库（持久化）
        result = [self._to_dict(r) for r in data]
        return result

    async def update(self, db, id: int, data: dict):
        data = self.filter_data(data)

        stmt = update(self.model).where(self.model.id == id).values(**data)
        await db.execute(stmt)

    async def get(self, db: AsyncSession, kwargs):

        stmt = select(self.model)

        # 自动拼接 where 条件
        conditions = []
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
        # -------------------------
        # 1️⃣ 查询总数
        # -------------------------
        count_stmt = select(func.count()).select_from(self.model)
        if conditions:
            count_stmt = count_stmt.where(*conditions)

        total = (await db.execute(count_stmt)).scalar()
        # -------------------------
        # 2️⃣ 分页
        # -------------------------
        page = kwargs['page']
        page_size = kwargs['page_size']
        stmt = stmt.offset((page - 1) * page_size).limit(page_size)
        result = await db.execute(stmt)
        rows = result.scalars().all()
        data = [self._to_dict(r) for r in rows]
        return {"list": data, "total": total, "page": page, "page_size": page_size}

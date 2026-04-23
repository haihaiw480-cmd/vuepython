import asyncio
import random
from faker import Faker
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from database.db import AsyncSessionLocal
from models.system.user import User

fake = Faker("zh_CN")


async def seed_users(count: int = 1000):

    async with AsyncSessionLocal() as db:

        users = []

        for _ in range(count):

            users.append(
                User(
                    username=fake.user_name() + str(random.randint(100, 999)),
                    nickname=fake.name(),
                    password="123456",
                    email=fake.email(),
                    phone=fake.phone_number(),
                    status=random.choice([0, 1]),
                )
            )

        db.add_all(users)
        await db.commit()

        print(f"✅ 插入完成：{count} 条用户")


if __name__ == "__main__":
    asyncio.run(seed_users(2000))

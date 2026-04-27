from faker import Faker
import asyncio
import random
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from backend.app.database.db import AsyncSessionLocal, test_connection
from backend.app.models.system.menu import Menu

fake = Faker("zh-CN")


async def make_menu():
    await test_connection()
    async with AsyncSessionLocal() as db:
        menu_list = []
        menu_id = 1
        for i in range(5):
            catalog_name = fake.word() + '管理'

            catalog = Menu(
                id=menu_id,
                name=catalog_name,
                route_name=f"module_{i}",
                path=f"/module{i}",
                component="",
                parent_id=0,
                type=1,
                sort=i,
                icon=random.choice(["Menu", "Setting", "User"]),
                is_hidden=0,
                perms="",
            )
            menu_list.append(catalog)
            catalog_id = menu_id
            menu_id += 1
            # -------------------------
            # 2️⃣ 子菜单（页面）
            # -------------------------
            for j in range(random.randint(3, 6)):

                page_name = fake.word() + "页面"

                menu = Menu(
                    id=menu_id,
                    name=page_name,
                    route_name=f"module_{i}_page_{j}",
                    path=f"/module{i}/page{j}",
                    component=f"/module{i}/page{j}/index",
                    parent_id=catalog_id,
                    type=2,
                    sort=j,
                    icon="Document",
                    is_hidden=0,
                    perms="",
                )

                menu_list.append(menu)
                menu_parent_id = menu_id
                menu_id += 1

                # -------------------------
                # 3️⃣ 按钮
                # -------------------------
                for k in range(random.randint(2, 4)):

                    action = random.choice(["add", "edit", "delete", "view"])

                    button = Menu(
                        id=menu_id,
                        name=f"{page_name}-{action}",
                        route_name="",
                        path="",
                        component="",
                        parent_id=menu_parent_id,
                        type=3,
                        perms=f"module{i}:page{j}:{action}",
                        sort=k,
                        is_hidden=0,
                        icon="",
                    )

                    menu_list.append(button)
                    menu_id += 1
        db.add_all(menu_list)
        await db.commit()

        print(f"✅ 插入菜单数据：{len(menu_list)} 条")


if __name__ == "__main__":
    asyncio.run(make_menu())

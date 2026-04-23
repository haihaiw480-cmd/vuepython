from repositories.system.menu_repository import MenuRepository
from typing import Optional


# 不做数据结构转换
# 只做业务逻辑
class MenuService:
    def __init__(self):
        self.repo = MenuRepository()

    async def get_menu_list(self, db, page, page_size, type):

        return await self.repo.get(db, page, page_size, type=type)

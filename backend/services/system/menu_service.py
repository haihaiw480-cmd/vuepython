from repositories.system.menu_repository import MenuRepository
from typing import Optional


# 不做数据结构转换
# 只做业务逻辑
class MenuService:
    def __init__(self):
        self.repo = MenuRepository()

    async def get_menu_list(self, db, params):
        if params is None:
            params_dict = {}
        elif isinstance(params, dict):
            params_dict = params
        else:
            params_dict = params.model_dump()
        return await self.repo.get(db, params_dict)

    # 创建菜单
    async def create_menu(self, db, data):

        data_dict = data.model_dump()

        name = data_dict["name"]
        params = {'name': name, 'page': 1, "page_size": 10}
        result = await self.get_menu_list(db, params)
        if result['total'] > 0:
            # 提示该菜单名已经存在
            raise ValueError("菜单名称已存在")
        return await self.repo.create(db, data_dict)

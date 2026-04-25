from repositories.system.menu_repository import MenuRepository
from dto.system.menu_dto import SearchMenuParams
from typing import Union
from schemas.system.menu import MenuItem


# 不做数据结构转换
# 只做业务逻辑
class MenuService:
    def __init__(self):
        self.repo = MenuRepository()

    def format_data(self, rows):
        # 情况1：分页结构
        if isinstance(rows, dict) and "list" in rows:
            rows["list"] = [
                MenuItem.model_validate(i).model_dump(by_alias=True) for i in rows["list"]
            ]
            return rows
        # 情况2：普通列表
        elif isinstance(rows, list):
            return [MenuItem.model_validate(i).model_dump(by_alias=True) for i in rows]

        # 情况3：单个对象
        elif isinstance(rows, dict):
            return MenuItem.model_validate(rows).model_dump(by_alias=True)

        return rows

    async def get_menu_list(self, db, params: Union[SearchMenuParams, dict, None] = None):
        if params is None:
            params_dict = {}
        elif isinstance(params, dict):
            params_dict = params
        else:
            params_dict = params.model_dump(exclude_none=True)
        rows = await self.repo.get(db, params_dict)
        data = self.format_data(rows)
        # data = [MenuItem.model_validate(i).model_dump(by_alias=True) for i in rows]
        return data

    # 创建菜单
    async def create_menu(self, db, data):

        data_dict = data.model_dump()

        # name = data_dict["name"]
        # params = {'name': name}
        # result = await self.get_menu_list(db, params)
        # if result:
        #     # 提示该菜单名已经存在
        #     raise ValueError("菜单名称已存在")
        return await self.repo.create(db, data_dict)

    # 部分更新
    async def patch_menu(self, db, id, data):
        # 先查询id是不是存在
        params = {"id": id}
        result = await self.get_menu_list(db, params)
        print(result)
        if not result:
            raise ValueError('菜单不存在', result)
        return await self.repo.patch(db, id, data)

    # 删除菜单
    async def delete_menu(self, db, id: int):
        # -------------------------
        # 1️⃣ 校验是否存在
        # -------------------------
        result = await self.repo.get(db, {"id": id})

        if not result:
            raise ValueError("菜单不存在")

        # -------------------------
        # 2️⃣ 校验是否有子菜单
        # -------------------------
        children = await self.repo.get(db, {"parent_id": id})

        if children:
            raise ValueError("请先删除子菜单")

        # -------------------------
        # 3️⃣ 删除
        # -------------------------
        return await self.repo.delete_item(db, id)

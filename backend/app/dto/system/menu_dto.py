from pydantic import BaseModel, Field
from typing import Optional


class MenuItem(BaseModel):
    name: Optional[str] = Field(description="菜单名称")
    route_name: Optional[str] = Field(description="路由name", alias="routeName")
    path: Optional[str] = Field(
        description="路由路径",
        default="",
    )
    component: Optional[str] = Field(
        description="组件路径",
        default="",
    )
    parent_id: Optional[int] = Field(description="父级ID", default=0, alias="parentId")
    sort: Optional[int] = Field(
        description="排序",
        default=0,
    )
    type: Optional[int] = Field(description="类型 1目录 2菜单 3按钮")
    perms: Optional[str] = Field(
        description="权限标识",
        default="",
    )
    icon: Optional[str] = Field(
        description="图标",
        default="",
    )
    is_hidden: Optional[int] = Field(description="是否隐藏", default=0, alias="isHidden")
    is_cache: Optional[int] = Field(description="是否缓存", default=0, alias="isCache")
    menu_statuse: Optional[int] = Field(description="菜单状态", default=0, alias="menuStatuse")
    is_link: Optional[int] = Field(description="是否外链", default=0, alias="isLink")
    quary: Optional[str] = Field(description="路由参数", default='', alias="quary")


# 创建菜单入参
class CreateMenu(BaseModel):
    name: Optional[str] = Field(description="菜单名称")
    route_name: Optional[str] = Field(description="路由name", alias="routeName")
    path: Optional[str] = Field(
        description="路由路径",
        default="",
    )
    component: Optional[str] = Field(
        description="组件路径",
        default="",
    )
    parent_id: Optional[int] = Field(description="父级ID", default=None, alias="parentId")
    sort: Optional[int] = Field(
        description="排序",
        default=None,
    )
    type: Optional[int] = Field(description="类型 1目录 2菜单 3按钮")
    perms: Optional[str] = Field(
        description="权限标识",
        default="",
    )
    icon: Optional[str] = Field(
        description="图标",
        default="",
    )
    is_hidden: Optional[int] = Field(description="是否隐藏", default=0, alias="isHidden")
    is_cache: Optional[int] = Field(description="是否缓存", default=0, alias="isCache")
    menu_statuse: Optional[int] = Field(description="菜单状态", default=0, alias="menuStatuse")
    is_link: Optional[int] = Field(description="是否外链", default=0, alias="isLink")
    quary: Optional[str] = Field(description="路由参数", default='', alias="quary")


# 查询参数
class SearchMenuParams(BaseModel):
    name: Optional[str] = Field(
        description="菜单名称",
        default=None,
    )
    type: Optional[int] = Field(
        description="类型 1目录 2菜单 3按钮",
        default=None,
    )
    page: Optional[int] = Field(
        description="page",
        default=None,
    )
    page_size: Optional[int] = Field(
        description="page_size",
        default=None,
        alias="pageSize",
    )
    is_hidden: Optional[int] = Field(description="是否隐藏", default=None, alias="isHidden")

    parent_id: Optional[int] = Field(description="父级ID", default=None, alias="parentId")
    id: Optional[int] = Field(description="id", default=None, alias="id")


# 更新参数
class PatchMenu(BaseModel):
    name: Optional[str] = Field(
        description="菜单名称",
        default="",
    )
    route_name: Optional[str] = Field(description="路由name", default="", alias="routeName")
    path: Optional[str] = Field(
        description="路由路径",
        default="",
    )
    component: Optional[str] = Field(
        description="组件路径",
        default="",
    )
    parent_id: Optional[int] = Field(description="父级ID", default=None, alias="parentId")
    sort: Optional[int] = Field(
        description="排序",
        default=None,
    )
    type: Optional[int] = Field(description="类型 1目录 2菜单 3按钮")
    perms: Optional[str] = Field(
        description="权限标识",
        default="",
    )
    icon: Optional[str] = Field(
        description="图标",
        default="",
    )
    is_hidden: Optional[int] = Field(description="是否隐藏", default=None, alias="isHidden")
    is_cache: Optional[int] = Field(description="是否缓存", default=0, alias="isCache")
    menu_statuse: Optional[int] = Field(description="菜单状态", default=0, alias="menuStatuse")
    is_link: Optional[int] = Field(description="是否外链", default=0, alias="isLink")
    quary: Optional[str] = Field(description="路由参数", default='', alias="quary")

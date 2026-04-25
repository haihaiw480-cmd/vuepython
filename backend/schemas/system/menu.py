from pydantic import BaseModel, Field
from typing import Optional, List


class MenuIn(BaseModel):
    name: Optional[str] = Field(..., description="菜单名称")
    path: Optional[str] = Field(..., description="路径")


class MenuItem(BaseModel):
    id: Optional[int] = Field(description="菜单Id")
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
    children: Optional[List] = Field(
        description="子菜单",
        default=[],
    )

    class Config:
        populate_by_name = True  # 允许用字段名 or alias 赋值

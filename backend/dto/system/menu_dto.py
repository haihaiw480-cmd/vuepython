from pydantic import BaseModel, Field
from typing import Optional


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

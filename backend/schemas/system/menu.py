from pydantic import BaseModel, Field
from typing import Optional, List


class MenuIn(BaseModel):
    name: Optional[str] = Field(..., description="菜单名称")
    path: Optional[str] = Field(..., description="路径")


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


class MenuSearch(BaseModel):
    page: int = 1
    page_size: int = 10
    name: Optional[str] = Field(description="菜单名称", default=None)
    path: Optional[str] = Field(description="路径", default=None)
    type: Optional[int] = Field(description="类型名称：目录、菜单、按钮", default=None)


class MenuOut(BaseModel):
    id: int
    name: str
    path: str
    component: str
    parent_id: int

    children: Optional[List["MenuOut"]] = []

    class Config:
        from_attributes = True

from pydantic import BaseModel, Field
from typing import Optional, List


class MenuIn(BaseModel):
    name: Optional[str] = Field(..., description="菜单名称")
    path: Optional[str] = Field(..., description="路径")

    pass


class MenuSearch(BaseModel):
    name: Optional[str] = Field(description="菜单名称")
    path: Optional[str] = Field(description="路径")
    type: Optional[int] = Field(description="类型名称：目录、菜单、按钮")


class MenuOut(BaseModel):
    id: int
    name: str
    path: str
    component: str
    parent_id: int

    children: Optional[List["MenuOut"]] = []

    class Config:
        from_attributes = True

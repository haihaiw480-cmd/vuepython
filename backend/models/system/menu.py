from models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, ARRAY


class Menu(BaseModel):
    __tablename__ = 'sys_menu'
    name: Mapped[str] = mapped_column(String(50), comment="菜单名称")
    path: Mapped[str] = mapped_column(String(100), comment="路由路径")
    component: Mapped[str] = mapped_column(String(100), comment="组件路径")
    parent_id: Mapped[int] = mapped_column(Integer, default=0, comment="父级ID")
    sort: Mapped[int] = mapped_column(Integer, default=0, comment="排序")
    type: Mapped[int] = mapped_column(Integer, comment="类型 1目录 2菜单 3按钮")
    perms: Mapped[str] = mapped_column(String(100), comment="权限标识")
    icon: Mapped[str] = mapped_column(String(50), comment="图标")
    is_hidden: Mapped[int] = mapped_column(Integer, default=0, comment="是否隐藏")

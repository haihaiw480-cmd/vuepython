from backend.app.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer


class Menu(BaseModel):
    __tablename__ = 'sys_menu'

    # -------------------------
    # 基础信息
    # -------------------------
    name: Mapped[str] = mapped_column(String(50), comment="菜单名称")
    route_name: Mapped[str] = mapped_column(String(50), comment="路由name")

    # -------------------------
    # 路由信息
    # -------------------------
    path: Mapped[str] = mapped_column(String(100), default="", comment="路由路径")
    component: Mapped[str] = mapped_column(String(100), default="", comment="组件路径")

    # -------------------------
    # 层级
    # -------------------------
    parent_id: Mapped[int] = mapped_column(Integer, default=0, comment="父级ID")
    sort: Mapped[int] = mapped_column(Integer, default=0, comment="显示排序")

    # -------------------------
    # 类型
    # -------------------------
    type: Mapped[int] = mapped_column(Integer, comment="类型 1目录 2菜单 3按钮")

    # -------------------------
    # 权限
    # -------------------------
    perms: Mapped[str] = mapped_column(String(100), default="", comment="权限标识")
    # -------------------------
    # UI
    # -------------------------
    icon: Mapped[str] = mapped_column(String(50), default="", comment="图标")
    is_hidden: Mapped[int] = mapped_column(Integer, default=0, comment="是否隐藏")
    is_cache: Mapped[int] = mapped_column(Integer, default=0, comment="是否缓存")
    menu_status: Mapped[int] = mapped_column(Integer, default=0, comment="菜单状态")
    is_link: Mapped[int] = mapped_column(Integer, default=0, comment="是否外链")
    quary: Mapped[str] = mapped_column(String(100), default="", comment="路由参数")

from sqlalchemy import (
    Column,  # 定义字段
    Integer,  # 整型
    String,  # 字符串
    ForeignKey,  # 外键约束
    DateTime,  # 时间类型
    Boolean,  # 布尔类型
    Index,  # 索引
    UniqueConstraint,  # 唯一约束（表级）
)
from database.db import Base  # Base 是所有模型的父类（ORM基类）
from datetime import datetime


class Menu(Base):
    """
    菜单表（支持：动态路由 + 权限控制 + 树结构）
    """

    # ===== 表名 =====
    __tablename__ = "menu"

    # ===== 主键 =====
    id = Column(
        Integer,  # 数据类型：整数
        primary_key=True,  # 主键（唯一 + 非空）
        index=True,  # 自动创建索引（查询更快）
        comment="主键ID",
    )

    # ===== 菜单名称 =====
    name = Column(
        String(50),  # 最多50个字符
        nullable=False,  # 不允许为空（必须填写）
        comment="菜单名称",
    )

    # ===== 前端路由路径 =====
    path = Column(
        String(100),
        nullable=True,  # 可以为空（按钮不需要path）
        comment="路由路径，例如 /system/user",
    )

    # ===== Vue组件路径 =====
    component = Column(
        String(100), nullable=True, comment="前端组件路径，例如 system/user/index"
    )

    # ===== 图标 =====
    icon = Column(String(50), nullable=True, comment="菜单图标（如 el-icon-user）")

    # ===== 父级ID（树结构核心）=====
    parent_id = Column(
        Integer,
        ForeignKey("menu.id"),  # 外键：关联本表 id（自关联）
        default=0,  # 默认0表示顶级菜单
        index=True,  # 高频查询字段（必须加索引）
        comment="父级菜单ID",
    )

    # ===== 菜单类型 =====
    type = Column(Integer, default=1, comment="类型：1菜单 2按钮")

    # ===== 权限标识 =====
    permission = Column(
        String(100),
        nullable=True,
        unique=True,  # 唯一约束（不能重复）
        comment="权限标识，例如 user:add",
    )

    # ===== 是否显示 =====
    visible = Column(Boolean, default=True, comment="是否显示：True显示 False隐藏")

    # ===== 排序 =====
    sort = Column(
        Integer,
        default=0,
        index=True,  # 排序通常会参与查询
        comment="排序（值越小越靠前）",
    )

    # ===== 层级（建议加）=====
    level = Column(Integer, default=1, comment="菜单层级（1-一级 2-二级 3-三级）")

    # ===== 创建时间 =====
    create_time = Column(
        DateTime, default=datetime.utcnow, comment="创建时间"  # 默认当前时间（UTC）
    )

    # ===== 更新时间 =====
    update_time = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,  # 每次更新自动修改时间
        comment="更新时间",
    )

    # ===== 表级约束（重点）=====
    __table_args__ = (
        # 联合唯一约束：
        # 同一个父菜单下，name不能重复
        UniqueConstraint("name", "parent_id", name="uq_menu_name_parent"),
        # 联合索引：
        # 优化“按父级查 + 排序”的查询
        Index("idx_parent_sort", "parent_id", "sort"),
    )

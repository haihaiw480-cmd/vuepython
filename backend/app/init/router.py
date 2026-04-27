from backend.app.apis.app_router import app_router
from fastapi import FastAPI


def init_router(app: FastAPI):
    """注册路由"""
    # 权限(权限在每个接口上)
    app.include_router(app_router, prefix='')

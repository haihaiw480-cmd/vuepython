from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from core.exceptions import BizException
from utils.response import success, error
from init.router import init_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
import traceback
from contextlib import asynccontextmanager
from database.db import test_connection

# app = FastAPI()


# @app.exception_handler(BizException)
# async def biz_exception_handler(request: Request, exc: BizException, status_code=200):
#     return error(msg=exc.msg, data=None, code=exc.code, status_code=status_code)


# @app.exception_handler(RequestValidationError)
# async def validation_exception_handler(request: Request, exc: RequestValidationError):
#     return error(msg="参数校验失败", data=exc.errors())


def create_app() -> FastAPI:
    app: FastAPI = FastAPI(
        title="vue-fastapi-admin",
        # config=config,
        # description=config.SERVER_DESC,
        # version=config.SERVER_VERSION,
        lifespan=lifespan,
    )
    # init_exception(app)  # 注册捕获全局异常
    init_router(app)  # 注册路由
    # init_middleware(app)  # 注册请求响应拦截
    # init_cors(app)  # 初始化跨域
    return app


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 🚀 启动时执行
    print('---------')
    await test_connection()

    yield


app = create_app()
# 添加代理
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.exception_handler(SQLAlchemyError)


async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
    print("❌ 数据库异常：", str(exc))
    traceback.print_exc()

    return JSONResponse(
        status_code=500, content={"code": 500, "msg": "数据库错误", "detail": str(exc)}
    )


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print("❌ 全局异常：", str(exc))
    traceback.print_exc()

    return JSONResponse(
        status_code=500,
        content={
            "code": 500,
            "msg": "服务器内部错误",
        },
    )

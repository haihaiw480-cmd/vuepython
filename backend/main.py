from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from api import user
from core.exceptions import BizException
from utils.response import success, error

app = FastAPI()


@app.exception_handler(BizException)
async def biz_exception_handler(request: Request, exc: BizException, status_code=200):
    return error(msg=exc.msg, data=None, code=exc.code, status_code=status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return error(msg="参数校验失败", data=exc.errors())


app.include_router(user.router)

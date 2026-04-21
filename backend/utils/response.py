from fastapi.responses import JSONResponse

# 序列化（Python → JSON）
import orjson
from starlette import status
from starlette.responses import JSONResponse


def success(data=None, msg="success", status_code=200):
    return JSONResponse(content={"code": 200, "msg": msg, "data": data}, status_code=status_code)


def error(code=400, msg="error", data=None, status_code=200):
    return JSONResponse(content={"code": 400, "msg": msg, "data": data}, status_code=status_code)

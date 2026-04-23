from pydantic import BaseModel

from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    code: int
    msg: str
    data: Optional[T] = None


def success(data=None, msg="success", code=200):
    return ResponseModel(code=code, data=data, msg=msg)

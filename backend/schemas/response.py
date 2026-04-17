from pydantic import BaseModel

from typing import Optional, TypeVar, Generic

T = TypeVar("T")


class ResponseModel(BaseModel, Generic[T]):
    code: int
    msg: str
    data: Optional[T] = None

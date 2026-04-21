from pydantic import BaseModel
from typing import Optional, List


class MenuOpthion(BaseModel):
    pass


class MenuOut(BaseModel):
    id: int
    name: str
    path: str
    component: str
    parent_id: int

    children: Optional[List["MenuOut"]] = []

    class Config:
        from_attributes = True

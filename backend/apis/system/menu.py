from fastapi import APIRouter, Depends
from services.system.menu_service import MenuService
from database.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.response import ResponseModel, success
from typing import Optional

router = APIRouter()
menu_service = MenuService()


@router.get("/", status_code=200)
async def root():
    return {"message": "Hello World"}


@router.get("/list", response_model=ResponseModel)
async def get_menu_list(
    db: AsyncSession = Depends(get_db),
    pageNum: int = 1,
    page_size: int = 10,
    type: Optional[int] = None,
):
    data = await menu_service.get_menu_list(db, pageNum, page_size, type)
    return success(data)


@router.post("/add", response_model=ResponseModel)
async def menu_add(data: dict, db: AsyncSession = Depends(get_db)):
    return success(data)
    pass
    # data = await menu_service.get_menu_list(db)
    # return success(data)

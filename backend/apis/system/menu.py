from fastapi import APIRouter, Depends
from services.system.menu_service import MenuService
from database.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.response import ResponseModel, success
from typing import Optional
from schemas.system.menu import MenuItem, MenuSearch

router = APIRouter()
menu_service = MenuService()


@router.get("/", status_code=200)
async def root():
    return {"message": "Hello World"}


@router.get("/list", response_model=ResponseModel)
async def get_menu_list(
    params: MenuSearch = Depends(),
    db: AsyncSession = Depends(get_db),
):
    data = await menu_service.get_menu_list(db, params)
    return success(data)


# 新增menu
@router.post("/add", response_model=ResponseModel)
async def menu_add(data: MenuItem, db: AsyncSession = Depends(get_db)):
    datalist = await menu_service.create_menu(db, data)
    return success(datalist)


@router.delete("/add", response_model=ResponseModel)
async def menu_delete(data: MenuItem, db: AsyncSession = Depends(get_db)):
    datalist = await menu_service.create_menu(db, data)
    return success(datalist)

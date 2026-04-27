from fastapi import APIRouter, Depends
from backend.app.services.system.menu_service import MenuService
from backend.app.database.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from backend.app.schemas.response import ResponseModel, success
from typing import Optional
from backend.app.dto.system.menu_dto import SearchMenuParams, MenuItem, PatchMenu

router = APIRouter()
menu_service = MenuService()


@router.get("/", status_code=200)
async def root():
    return {"message": "Hello World"}


@router.get("/list", response_model=ResponseModel)
async def get_menu_list(
    params: SearchMenuParams = Depends(),
    db: AsyncSession = Depends(get_db),
):
    data = await menu_service.get_menu_list(db, params)
    return success(data)


# 新增menu
@router.post("/add", response_model=ResponseModel)
async def menu_add(data: MenuItem, db: AsyncSession = Depends(get_db)):
    datalist = await menu_service.create_menu(db, data)
    return success(datalist)


@router.delete("/delete/{id}", response_model=ResponseModel)
async def menu_delete(id: int, db: AsyncSession = Depends(get_db)):
    datalist = await menu_service.delete_menu(db, id)
    return success(datalist)


# 部分更新
@router.patch("/updata/{id}", response_model=ResponseModel)
async def menu_updata(id: int, data: PatchMenu, db: AsyncSession = Depends(get_db)):
    result = await menu_service.patch_menu(db, id, data)
    return success(result)

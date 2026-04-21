from fastapi import APIRouter, Depends
from services.system.menu_service import MenuService
from database.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()
menu_service = MenuService()


@router.get("/", status_code=200)
async def root():
    return {"message": "Hello World"}


@router.get("/list", status_code=200)
async def get_menu_list(db: AsyncSession = Depends(get_db)):
    return menu_service.get_menu_list(db)

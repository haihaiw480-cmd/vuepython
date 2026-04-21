from fastapi import APIRouter
import uvicorn
from apis.system import user
from apis.system import menu

app_router = APIRouter()

app_router.include_router(user.router, prefix="", tags=["user"])
app_router.include_router(menu.router, prefix="/menu", tags=["menu"])

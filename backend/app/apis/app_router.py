from fastapi import APIRouter
import uvicorn
from backend.app.apis.system import user
from backend.app.apis.system import menu
from backend.app.apis import ai_router

app_router = APIRouter()

app_router.include_router(user.router, prefix="", tags=["user"])
app_router.include_router(menu.router, prefix="/menu", tags=["menu"])
app_router.include_router(ai_router.router, prefix="/ai", tags=["ai"])

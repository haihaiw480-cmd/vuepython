from fastapi import APIRouter
import uvicorn
from apis.system import user

app_router = APIRouter()

app_router.include_router(user.router, prefix="", tags=["user"])

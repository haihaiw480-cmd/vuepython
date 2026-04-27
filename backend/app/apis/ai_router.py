# apis/ai_router.py
from fastapi import APIRouter, Depends
from backend.app.services.agent.orchestrator import agent_run
from backend.app.database.db import get_db

router = APIRouter()


@router.post("/query")
async def ai_query(q: str, db=Depends(get_db)):
    return await agent_run(db, q)

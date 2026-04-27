# services/agent/executor.py
from backend.app.services.agent.safety import sanitize_args
from backend.app.repositories.system.user_repository import UserRepository

user_repo = UserRepository()


async def execute_tool(db, tool_name: str, args: dict):
    safe_args = sanitize_args(tool_name, args)

    if tool_name == "query_user":
        return await user_repo.get(db, **safe_args)

    if tool_name == "create_user":
        # 这里可加密码加密、唯一性校验
        return await user_repo.create(db, safe_args)

    raise ValueError("未知工具")

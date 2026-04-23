# services/agent/tools.py
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "query_user",
            "description": "根据条件查询用户",
            "parameters": {
                "type": "object",
                "properties": {
                    "username": {"type": "string"},
                    "email": {"type": "string"},
                    "status": {"type": "integer"},
                },
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "create_user",
            "description": "创建用户",
            "parameters": {
                "type": "object",
                "properties": {
                    "username": {"type": "string"},
                    "password": {"type": "string"},
                    "email": {"type": "string"},
                },
                "required": ["username", "password"],
                "additionalProperties": False,
            },
        },
    },
]

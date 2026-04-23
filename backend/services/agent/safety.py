# services/agent/safety.py
ALLOWED_FIELDS = {
    "query_user": {"username", "email", "status"},
    "create_user": {"username", "password", "email"},
}


def sanitize_args(tool_name: str, args: dict) -> dict:
    allow = ALLOWED_FIELDS.get(tool_name, set())
    return {k: v for k, v in args.items() if k in allow}

# services/agent/retry.py 重试与降级
def with_fallback(primary_fn, fallback_fn):
    try:
        return primary_fn()
    except Exception:
        return fallback_fn()

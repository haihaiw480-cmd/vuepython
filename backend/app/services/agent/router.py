# services/agent/router.py
def choose_model(task: str) -> str:
    # 简单规则，可后续替换为分类器
    if any(k in task for k in ["总结", "润色"]):
        return "qwen-turbo"  # 便宜输出
    if any(k in task for k in ["查询", "用户", "创建"]):
        return "qwen-turbo"  # 工具调用稳定
    return "qwen-turbo"  # 复杂推理

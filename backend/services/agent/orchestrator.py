# services/agent/orchestrator.py 编排器
import json
from .llm import get_clients, call_llm
from .router import choose_model
from .tools import TOOLS
from .executor import execute_tool

clients = get_clients()


def parse_tool(resp):
    msg = resp.choices[0].message
    if not msg.tool_calls:
        return None
    call = msg.tool_calls[0]
    return call.function.name, json.loads(call.function.arguments)


async def agent_run(db, question: str):
    # 1️⃣ 选模型（用于决策）
    model_key = choose_model(question)
    client = clients[model_key]

    messages = [
        {"role": "system", "content": "你是后台管理系统助手"},
        {"role": "user", "content": question},
    ]

    # 2️⃣ AI决定是否调用工具
    resp = call_llm(client, model_key, messages, TOOLS)
    print(resp, '00')
    tool = parse_tool(resp)

    # 3️⃣ 无工具 → 直接返回
    if not tool:
        return resp.choices[0].message.content

    tool_name, args = tool

    # 4️⃣ 执行工具
    result = await execute_tool(db, tool_name, args)

    # 5️⃣ 二次总结（用便宜模型）
    summary_client = clients["qwen-turbo"]
    print('# 5️⃣ 二次总结（用便宜模型）')
    final = call_llm(
        summary_client,
        "qwen-turbo",
        [
            {"role": "user", "content": question},
            {"role": "assistant", "content": str(result)},
            {"role": "system", "content": "整理为用户可读结果"},
        ],
    )

    return final.choices[0].message.content

# services/agent/llm.py
from openai import OpenAI
from typing import Dict, Any
import os


def get_clients() -> Dict[str, OpenAI]:
    clients = {}

    qwen_key = os.getenv("DASHSCOPE_API_KEY")
    print(os.getenv("DASHSCOPE_API_KEY"))
    if qwen_key:
        clients["qwen-turbo"] = OpenAI(
            api_key=qwen_key,
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )
    # return {
    #     "qwen-turbo": OpenAI(
    #         api_key='sk-cb645ef57a864074b2801d48822eb9ec',
    #         base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    #     ),
    #     "deepseek": OpenAI(api_key="DEEPSEEK_KEY", base_url="https://api.deepseek.com"),
    #     "gemini": OpenAI(
    #         api_key="GEMINI_KEY",
    #         base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    #     ),
    # }
    return clients


def call_llm(client: OpenAI, model: str, messages, tools=None, timeout=20):
    kwargs = {
        "model": "qwen-turbo",
        "messages": messages,
        "timeout": timeout,
    }

    if tools is not None:
        kwargs["tools"] = tools
        kwargs["tool_choice"] = "auto"
    return client.chat.completions.create(**kwargs)

# -*- coding: utf-8 -*-
"""最小可用的 DeepSeek API 调用示例。

用法：
    set DEEPSEEK_API_KEY=sk-xxxx      # Windows
    export DEEPSEEK_API_KEY=sk-xxxx   # Linux / macOS
    python api_demo.py
"""
import json
import os
import sys
import urllib.error
import urllib.request

API_URL = "https://api.deepseek.com/chat/completions"


def chat(prompt: str, model: str = "deepseek-chat", max_tokens: int = 256) -> dict:
    key = os.environ.get("DEEPSEEK_API_KEY")
    if not key:
        sys.exit("请先设置环境变量 DEEPSEEK_API_KEY")

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
    }
    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        # 401 = key 不对；402 = 余额不足；429 = 限流
        print(f"HTTP {e.code}: {e.read().decode('utf-8', 'ignore')[:200]}")
        raise


def main() -> None:
    prompt = " ".join(sys.argv[1:]) or "用一句话介绍你自己"
    data = chat(prompt)
    text = data["choices"][0]["message"]["content"].strip()
    usage = data.get("usage", {})

    print(f"model : {data.get('model')}")
    print(f"reply : {text}")
    print(f"tokens: {usage.get('total_tokens')} (prompt {usage.get('prompt_tokens')} + "
          f"completion {usage.get('completion_tokens')})")


if __name__ == "__main__":
    main()

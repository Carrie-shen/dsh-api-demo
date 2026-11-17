# dsh-api-demo

一个最小可用的 **DeepSeek API** 调用示例：不装任何第三方库，用标准库 `urllib` 直接请求 `chat/completions`。

## 跑起来

```bash
# 1. 设置你的 API key（去 https://platform.deepseek.com 创建）
set DEEPSEEK_API_KEY=sk-xxxxxxxx        # Windows CMD
$env:DEEPSEEK_API_KEY="sk-xxxxxxxx"     # Windows PowerShell
export DEEPSEEK_API_KEY=sk-xxxxxxxx     # Linux / macOS

# 2. 运行
python api_demo.py "用一句话介绍你自己"
```

输出：

```
model : deepseek-flash
reply : 我是 DeepSeek，一个由深度求索公司创造的 AI 助手……
tokens: 45 (prompt 8 + completion 37)
```

## 说明

- 纯标准库实现，`urllib` + `json`，没有 `openai` 包，便于看清请求本身
- key 只从环境变量读取，不写进代码
- 常见错误码：`401` key 无效，`402` 余额不足，`429` 触发限流

## 文件

| 文件 | 作用 |
| --- | --- |
| `api_demo.py` | 调用示例，支持命令行传 prompt |

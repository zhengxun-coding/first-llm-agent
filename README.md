# Agent Project

这是一个基于大语言模型（LLM）的智能 Agent 示例项目，演示了如何通过 Tool Calling 机制让模型具备查询天气、计算数学公式和检索知识库的能力。

## 项目结构

- `main.py`: 项目的执行入口。
- `agent.py`: Agent 的核心执行逻辑（将对话上下文进行管理，并实现了调用的循环）。
- `tools.py`: 定义了所有的工具函数及其规范配置（即 JSON Schema）。
- `prompts.py`: 存放了系统预设 Prompt，方便将其分离出核心逻辑，便于集中管理或修改。
- `README.md`: 项目说明文件。

## 有哪些工具

1. **get_weather**: 获取某个城市天气，比如查询“北京天气”。
2. **calculator**: 计算数学表达式（仅支持四则运算），遇到数字问题会优先调用避免大模型出现幻觉。
3. **search_knowledge**: 模拟一个小型的知识库，能够查询特定概念、术语的简化解释（如 ReAct、Agent、Memory、Planning 等）。

## 怎么运行

首先确保已经安装了所需的依赖包：

```bash
pip install openai
```

使用前请需要设置你的 OpenAI API key 等相关环境变量（默认配置使用了 deepseek 的代理，也可以修改 `agent.py` 文件换为原生的）：

```bash
export OPENAI_API_KEY="your-api-key-here"
```

进入目录直接运行：

```bash
cd agent_project
python main.py
```

在交互式命令行中输入你的问题，或者输入 `exit`/`quit` 来退出程序。

def get_weather(city: str):
    fake_weather_data={
        "台北": "台北今天 25°C，晴天 ☀️",
        "北京": "北京今天 18°C，多云 ☁️",
        "上海": "上海今天 22°C，小雨 🌧️",
        "深圳": "深圳今天 28°C，阴天 ☁️"
    }
    return fake_weather_data.get(city,f"{city}天气查不到")

def calculator(expression:str):
    try:
        allowed_chars="1234567890+-*/(). "
        if any(ch not in allowed_chars for ch in expression):
            return "表达式非法"
        result=eval(expression)
        return f"{expression}={result}"
    except Exception as e:
        return f"计算失败：{str(e)}"
    
def search_knowledge(query: str):
    fake_knowledge_base = {
        "react": "ReAct 是一种 Agent 推理模式，核心是 Thought → Action → Observation 的循环。",
        "agent": "Agent 一般指基于 LLM 的智能体系统，能够结合工具、记忆和控制逻辑完成任务。",
        "tool calling": "Tool Calling 指的是让 LLM 决定是否调用外部函数或 API，以获得额外能力。",
        "memory": "Memory 指 Agent 保存上下文或历史信息的机制，通常分为短期记忆和长期记忆。",
        "planning": "Planning 指 Agent 在执行任务前或执行过程中，对步骤进行拆解和安排。"
    }
    q=query.strip().lower()
    for key,value in fake_knowledge_base.items():
        if key in q or q in key:
            return value
    return f"知识库中暂时没有关于{query}的信息"

tools_maps = {
    "get_weather": get_weather,
    "calculator":calculator,
    "search_knowledge":search_knowledge
}

tool_specs=[
    {
        "type":"function",
        "function":{
            "name":"get_weather",
            "description":"获取某个城市天气",
            "parameters":{
                "type":"object",
                "properties":{
                    "city":{
                        "type":"string",
                        "description":"城市名，比如台北、北京、上海"
                    }
                },
                "required":["city"]
            }

        }
    },
    {
        "type":"function",
        "function":{
            "name":"calculator",
            "description":"计算数学表达式",
            "parameters":{
                "type":"object",
                "properties":{
                    "expression":{
                        "type":"string",
                        "description":"要计算的数学表达式"
                    } 
                },
                "required":["expression"]
            }
        }
    },
    {
        "type":"function",
        "function":{
            "name":"search_knowledge",
            "description":"查询某个概念、术语或知识点的简要解释，比如 ReAct、Agent、Memory、Planning",
            "parameters":{
                "type":"object",
                "properties":{
                    "query":{
                        "type":"string",
                        "description":"查询内容，比如 ReAct、Agent、Memory、Planning"
                    }
                },
                "required":["query"]
            }
        }
    }
]

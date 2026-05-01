import os
import json
from openai import OpenAI
from tools import tools_maps, tool_specs
from prompts import SYSTEM_PROMPT

class Agent:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.environ.get('OPENAI_API_KEY'),
            base_url="https://api.deepseek.com"
        )
        self.messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

    def run(self, user_input:str, max_steps:int=5):
        self.messages.append({"role":"user","content":user_input})

        for step in range(max_steps):
            print(f"\n========== 第{step + 1}轮 ==========")

            response=self.client.chat.completions.create(
                model="deepseek-chat",
                messages=self.messages,
                tools=tool_specs
            )

            msg=response.choices[0].message

            if msg.tool_calls:
               self.messages.append(msg)

               for tool_call in msg.tool_calls:
                   tool_name=tool_call.function.name
                   try:
                        args = json.loads(tool_call.function.arguments)
                   except Exception as e:
                        args = {}
                        result = f"工具参数解析失败：{str(e)}"

                        print(f"[Agent决定调用工具] {tool_name}")
                        print(f"[工具参数解析失败] {tool_call.function.arguments}")
                        print(f"[工具返回] {result}")

                        self.messages.append({
                            "role":"tool",
                            "tool_call_id":tool_call.id,
                            "content":result
                        })
                        continue
                   print(f"[Agent决定调用工具] {tool_name}")
                   print(f"[工具参数] {args}")

                   if tool_name not in tools_maps:
                        result = f"错误：未知工具 {tool_name}"
                   else:
                        try:
                            result = tools_maps[tool_name](**args)
                        except TypeError as e:
                            result = f"工具参数错误：{str(e)}"
                        except Exception as e:
                            result = f"工具执行失败：{str(e)}"

                   print(f"[工具返回] {result}")

                   self.messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result
                    })
            else:
                print(f"最终回答:{msg.content}")
                self.messages.append(msg)
                break

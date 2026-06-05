import asyncio
import os
from http.client import responses

import dotenv

dotenv.load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.callbacks import BaseCallbackHandler

llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4-Pro",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)
#
# response=llm.invoke(
#     "讲一个笑话,并且解释一下",config={
#         "tags":["humor","demo"],
#         "metadata":{"user_id":"123"},
#     }
# )
# print(response)
class MyDebugCallback(BaseCallbackHandler):
    def on_chat_model_start(self, serialized, prompts, **kwargs):
        print("\n" + "="*40)
        print(" [拦截到 LLM 启动请求]")
        print(f" Tags: {kwargs.get('tags')}")
        print(f" Metadata: {kwargs.get('metadata')}")

        print("="*40 + "\n")

# llm = ChatOpenAI(model="gpt-4o-mini")

# 2. 在调用时，将你的回调处理器传进去
response = llm.invoke(
    "讲一个短笑话",
    config={
        "tags": ["humor", "demo"],
        "metadata": {"user_id": "123"},
        "callbacks": [MyDebugCallback()]  # 关键：挂载你的回调
    }
)

print("最终返回的 response 依然只有大模型的内容：")
print(response.content)
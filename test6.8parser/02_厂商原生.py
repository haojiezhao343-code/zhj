import asyncio
import os
import dotenv
from pydantic import BaseModel, Field

dotenv.load_dotenv()
from langchain_openai import ChatOpenAI
from openai import OpenAI

# 1. 补上 base_url、api_key，和 llm 保持一致
client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4-Pro",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

class CalendarEvent(BaseModel):
    # 2. Field 必须写 description=xxx
    name: list[str] = Field(description="参与者姓名")
    date: str
    activity: str = Field(description="活动名字")

res = client.chat.completions.parse(
    model="deepseek-ai/DeepSeek-V4-Pro",
    messages=[
        {"role": "user", "content": "Alice and Bob are going to a science fair on Friday"}
    ],
    response_format=CalendarEvent
)  # 3. 补上右括号

# 你后面要打印解析结果可以加：
# print(res.choices[0].message.parsed)

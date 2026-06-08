import asyncio
import os
from platform import system

import dotenv
from langchain_core.output_parsers import JsonOutputParser
from pydantic.v1.schema import json_scheme

dotenv.load_dotenv()
from langchain_openai import ChatOpenAI
from pydantic import BaseModel,Field
llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4-Pro",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)
# #定义结构
# class Primer(BaseModel):
#     prime: list[int] = Field(description="素数")
#     count: list[int] = Field(description="小于该素数的个数")
# #构造解析器
# json_parser = JsonOutputParser(pydantic_object=Primer)
# # 将格式说明放入SystemMessage
# res=llm.invoke(
#     [
#         ("system",json_parser.get_format_instructions()),
#         ("user","任意生成5个1000-100000之间的素数，并标出小于该素数的素数个数")
#     ]
# )
# print(res.content)
# # 解析为Python字典
# parsed_res=json_parser.invoke(res)
# print(type(parsed_res))




# 1. 定义正确的Pydantic模型
class table_stu(BaseModel):
    name: str = Field(description="学生姓名")
    age: int = Field(description="学生年龄")
    address: str = Field(description="学生家庭住址")

# 2. 解析器
json_parser2 = JsonOutputParser(pydantic_object=table_stu)

# 3. 提示词（必须是自然语言）
prompt = f"""
请把下面的学生信息转换成标准JSON格式：
学生姓名：张三
学生年龄：20
家庭住址：郑州市荥阳市

{json_parser2.get_format_instructions()}
"""

# 4. 正确调用 LLM 格式！！！
dd = llm.invoke(
    [
        ("user", prompt)  # 必须用 user / system / assistant
    ]
)

# 输出结果
print(dd.content)
#LangChain 的 invoke() 只认：
# user / ai / system 这种角色消息
# 不认 name、age 这种键！
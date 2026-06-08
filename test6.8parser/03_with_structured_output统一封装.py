# import asyncio
# import os
# import dotenv
from pydantic import BaseModel,Field
#
# dotenv.load_dotenv()
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="deepseek-ai/DeepSeek-V4-Pro",
#     base_url=os.getenv("OPENAI_BASE_URL"),
#     api_key=os.getenv("OPENAI_API_KEY")
# )
# class CalendarEvent(BaseModel):
#     name:str = Field(description="活动名称")
#     date:str
#     participants:list[str] = Field("参与者名字")
# structured_llm=llm.with_structured_output(schema=CalendarEvent)
# result=structured_llm.invoke("Alice and Bob are going to a science fair on Friday.")
# print(result)
# print(type(result))
import asyncio
import os
import dotenv
from openai import BaseModel

dotenv.load_dotenv()
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4-Pro",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)
class Demo(BaseModel):
    name: str =Field(description='收件人姓名')
    phone:str=Field(description='收件人电话')
    address:str=Field(description='收件人地址')
#langchain统一格式
#定义输出解析器
sp=llm.with_structured_output(schema=Demo)
#模拟
raw_text="给张三寄一个快递，电话是12345678900，地址在河南省郑州市xxxxxx"
res=sp.invoke(raw_text)
print(res)
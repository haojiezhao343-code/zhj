# class Dog:
#     name:str
#     age:int
#     address:str
# d=Dog()


#
#
# from pydantic import BaseModel
# class Dog(BaseModel):
#     name:str
#     age:int
#     address:str
# d=Dog()





#python很宽松不会强制，例如
# def test(a:int):
#     print(a)
# test("abc")#正常要求传入int类型，但是传入字符串也不会报错


# from pydantic import BaseModel,Field
# class User(BaseModel):
#     name:str
#     age:int
#     email:str = Field(description='用户邮箱地址')
# user=User(name='张三',age=18,email='asd@12.com')
# print(user)
# print(user.name)
# print(user.age)


#pydantic有强制要求传入类型
# from pydantic import BaseModel,Field
# class User(BaseModel):
#     name:str
#     age:int
#     email:str = Field(description='用户邮箱地址')
# user=User(name='张三',age="abc",email='asd@12.com')
# print(user)
# print(user.name)
# print(user.age)











# import asyncio
# import os
#
#
# import dotenv
# from langchain_core.output_parsers import JsonOutputParser
# from pydantic import BaseModel,Field
#
# dotenv.load_dotenv()
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="deepseek-ai/DeepSeek-V4-Flash",
#     base_url=os.getenv("OPENAI_BASE_URL"),
#     api_key=os.getenv("OPENAI_API_KEY")
# )
# class Joke(BaseModel):
#     title: str = Field(description='笑话的标题'),
#     content: str = Field(description='笑话的正文内容'),
#     theme:str = Field(description='笑话的主题，比如日常、职场')
# #以JSON格式输出 langchain json解释器JsonOutputParser
# jsp=JsonOutputParser(pydantic_object=Joke)
# res=llm.invoke(
#     [
#         ('system',jsp.get_format_instructions()),
#         ('human','请给我讲一个冷笑话')
#     ]
# )
# print(res.content)
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field, field_validator
from langchain_openai import ChatOpenAI

import os
import dotenv

dotenv.load_dotenv()

# 定义结构化输出模型
class MovieReview(BaseModel):
    title: str = Field(description='电影标题')
    rating: int = Field(description='电影评分', ge=1, le=10)
    summary: str = Field(description='剧情简介')
    recommended: bool = Field(description='是否推荐')

    @field_validator('rating')
    @classmethod
    def rating_must_be_valid(cls, value):
        if not (1 <= value <= 10):
            raise ValueError('评分必须在1-10之间')
        return value

# 初始化模型
llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4-Flash",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

# 解析器
parser = PydanticOutputParser(pydantic_object=MovieReview)

# ✅ 正确的模板写法（关键）
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是专业的电影评论员。\n{format_instructions}"),
    ("human", "评价电影《夺宝特工队》")
])

# 构建链
chain = prompt | llm | parser

# ✅ 正确调用（必须传入 format_instructions）
result = chain.invoke({
    "format_instructions": parser.get_format_instructions()
})

# 输出
print(f"电影: {result.title}, 评分: {result.rating}/10")
print(f"简介: {result.summary}")
print(f"是否推荐: {result.recommended}")
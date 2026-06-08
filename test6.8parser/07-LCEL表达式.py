# from itertools import chain
#
# import dotenv
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import ChatPromptTemplate
# from langchain.chat_models import init_chat_model
# import os
# dotenv.load_dotenv()
# prompt=ChatPromptTemplate.from_template("请用{xxx}风格回答{question}")
# llm=init_chat_model(model='deepseek-ai/DeepSeek-V4-Flash',
#                       model_provider='openai',
#                       base_url=os.getenv("OPENAI_BASE_URL"),
#                       api_key=os.getenv("OPENAI_API_KEY")
#                       )
#
# chain=prompt|llm
# print(chain.invoke({
#     "xxx": '幽默',
#     "question": '我们谈恋爱吧'
# }).content)
from dataclasses import Field
from itertools import chain
from pydantic import BaseModel,Field
import dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.chat_models import init_chat_model
import os

from pydantic import BaseModel

dotenv.load_dotenv()
prompt=ChatPromptTemplate.from_template("请用{xxx}风格回答{question}")
llm=init_chat_model(model='deepseek-ai/DeepSeek-V4-Flash',
                      model_provider='openai',
                      base_url=os.getenv("OPENAI_BASE_URL"),
                      api_key=os.getenv("OPENAI_API_KEY")
                      )
class Demo(BaseModel):
    title:str = Field(description=('用户原始的问题'))
    content:str=Field(description="大模型对于用户原始的问题的回答")
llm_with_demo=llm.with_structured_output(schema=Demo)


chain=prompt|llm_with_demo
print(chain.invoke({
    "xxx": '幽默',
    "question": '我们谈恋爱吧'
}).content)


















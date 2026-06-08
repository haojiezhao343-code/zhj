from itertools import chain

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

parser = StrOutputParser()
import asyncio
import os
import dotenv

dotenv.load_dotenv()
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4-Pro",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)
prompt=ChatPromptTemplate.from_template(
    '你是一个资深的宠物起名专家，请为一只{color}颜色的{breed}起三个搞笑的名字'

)
chain=prompt|llm|StrOutputParser()
resource=chain.invoke({'color':'橘色','breed':'狸花猫'})
print(resource)

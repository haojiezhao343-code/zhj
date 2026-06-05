import asyncio
import os
import dotenv

dotenv.load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4-Pro",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

from langchain_core.prompts import ChatPromptTemplate
from pyexpat.errors import messages
#第一种
# chat_prompt=ChatPromptTemplate.from_messages(
#     [
#         ("system","你是一个专业的{role}"),
#         ("human","请回答关于{topic}的问题"),
#         ("ai","好的，我会尽量的去回答"),
#         ("human","{question}")
#     ]
# )
# messages=chat_prompt.invoke(
#     {
#         "role":"分手大师",
#         "topic":"如何分手",
#         "question":"老板跟香烟如何和平分手"
#     }
# )
#第二种
chat_prompt=ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="你是一个有帮助的AI助手"),
        HumanMessage(content="你好"),
        AIMessage(content="你好"),
        ("human","请介绍{topic}")
    ]
)
messages=chat_prompt.invoke({"topic":"LangChain"})
print(llm.invoke(messages).content)

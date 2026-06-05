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

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.messages import AIMessage,HumanMessage
from pyexpat.errors import messages

# prompt=ChatPromptTemplate.from_messages(
#     [
#         ("system","你是AI助手"),
#         MessagesPlaceholder(variable_name="history"),
#         ("human",f"{input}")
#
#     ]
# )

#等价写法
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","你是一个AI助手"),
        ("placeholder","{history}"),
        ("human",f"{input}")
    ]
)
messages=prompt.invoke(
    {
        "history":[
            HumanMessage(content="家良这个名字是什么意思"),
            AIMessage(content="家良是一个名字")
        ],
        "input":"它有什么含义"
    }
)
print(llm.invoke(messages).content)
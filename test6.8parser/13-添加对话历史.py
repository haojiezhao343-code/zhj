

from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

import os
import dotenv
dotenv.load_dotenv()
from langchain_openai import ChatOpenAI

#创建会话存储(以session_id为key)
store={}


def get_session_history(session_id:str):
    if session_id not in store:
        store[session_id]=InMemoryChatMessageHistory()
    return store[session_id]

#创建基础链

prompt=ChatPromptTemplate.from_messages([
    ('system',"你是AI助手"),
    MessagesPlaceholder(variable_name='history'),
    ('human',"{input}")
])
llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4-Pro",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

chain=prompt|llm

#包装为带历史记录的链
chain_with_history=RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)
response_1=chain_with_history.invoke(
    {"input":"我叫张三"},
    config={"configurable":{"session_id":"user123"}}

)
print(response_1.content)
response_2=chain_with_history.invoke(
    {"input":"我叫什么名字"},
     config={"configurable":{"session_id":"user123"}}
)
print(response_2.content)
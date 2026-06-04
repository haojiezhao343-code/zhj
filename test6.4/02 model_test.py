import os
from pydoc_data.topics import topics

import dotenv
from pyexpat.errors import messages

dotenv.load_dotenv()
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_openai import ChatOpenAI
llm=ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4-Pro",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),

)

# resource=llm.invoke([HumanMessage(content="请用一句话介绍自己")])
# resource=llm.invoke([HumanMessage(content="你是一个情感大师"),
#                      SystemMessage("你好，请问有什么情感问题吗"),
#                      HumanMessage(content="写一首关于爱情的诗词，要求100字左右")])
# resource=llm.invoke([
#     SystemMessage("你是一个情商极高的老手"),
#     HumanMessage("我叫家良"),
#     AIMessage("你好啊，家良"),
#     HumanMessage("HJ是我爸爸，我该怎么关爱他")
# ])

# print(resource)
# dict_messages = llm.invoke([
#     {"role": "system", "content": "你叫刘家良"},
#     {"role": "user", "content": "我是你爸爸"}
# ])
# print(dict_messages)
dict_dict_dict=[
    {"role":"system","content":"你是一个{role}"},
    {"role":"user","content":"请解释{topic}"}
]
messages=[
    {
        "role":t["role"],
        "content":t["content"].format(
            role="翻译助手",
            topic="机器翻译",
        ),
    }
    for t in dict_dict_dict
]
print(llm.invoke(messages).content)


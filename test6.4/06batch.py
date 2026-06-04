import asyncio
import os
import dotenv
dotenv.load_dotenv()
# def batch_example():
#     from langchain_openai import ChatOpenAI
#     llm = ChatOpenAI(
#         model="deepseek-ai/DeepSeek-V4-Pro",
#         base_url=os.getenv("OPENAI_BASE_URL"),
#         api_key=os.getenv("OPENAI_API_KEY")
#     )
#     questions=[
#         "什么是历史？",
#         "为什么铭记历史？",
#         "为什么不平反历史？"
#     ]
#     resource=llm.batch(questions)
#     for q,r in zip(questions,resource):
#         print(f"Q:{q}")
#         print(f"A:{r.content}\n")
# batch_example()



#批量异步调用：
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
        model="deepseek-ai/DeepSeek-V4-Pro",
        base_url=os.getenv("OPENAI_BASE_URL"),
        api_key=os.getenv("OPENAI_API_KEY")
    )
async def batch_async():

    questions=[
        "什么是历史？",
        "为什么铭记历史？",
        "为什么不平反历史？"
    ]
    resource = await llm.abatch(questions)
    for q,r in zip(questions,resource):
        print(f"Q: {q}\nA: {r.content}\n")
asyncio.run(batch_async())
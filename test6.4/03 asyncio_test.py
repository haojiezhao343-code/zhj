import asyncio
import os
import dotenv
dotenv.load_dotenv()
from langchain_openai import ChatOpenAI
llm=ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4-Pro",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)


async def llm_async():
    response=await llm.ainvoke(
        "什么是爱情"
    )
    print(response.content)
asyncio.run(llm_async())
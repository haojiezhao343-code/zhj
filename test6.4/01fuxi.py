
#第一种方式
#langchain
from langchain_openai import ChatOpenAI
import os
import dotenv
dotenv.load_dotenv()
# llm=ChatOpenAI(
#     model="MiniMaxAI/MiniMax-M2.5",
#     base_url=os.getenv("GUIJI_BASE_URL"),
#     api_key=os.getenv("GUIJI_API_KEY")
# )
llm=ChatOpenAI(
    model="Pro/zai-org/GLM-5.1",
    base_url=os.getenv("GUIJI_BASE_URL"),
    api_key=os.getenv("GUIJI_API_KEY"),
    temperature=1,  # 随机性，0=确定性，1=有创意（默认因模型而异）
    max_tokens=100,  # 最大输出长度
    timeout=60,  # 超时时间（秒）
    max_retries=2

)
res=llm.invoke("请写一首夸赞家良的诗")
print(res.content)


#第二种方式init_chat_model
# from langchain.chat_models import init_chat_model
# import os
# import dotenv
# dotenv.load_dotenv()
# llm_openai=init_chat_model(
#     model="MiniMaxAI/MiniMax-M2.5",
#     model_provider="openai",
#     api_key=os.getenv("GUIJI_API_KEY"),
#     base_url=os.getenv("GUIJI_API_URL"),
#     temperature=1,  # 随机性，0=确定性，1=有创意（默认因模型而异）
#     max_tokens=100,  # 最大输出长度
#     timeout=30,  # 超时时间（秒）
#     max_retries=2
# )
# print(llm_openai.invoke("请写一首夸赞家良的诗").content)












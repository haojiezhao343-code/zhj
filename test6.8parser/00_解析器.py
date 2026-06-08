# import asyncio
# import os
# import dotenv
#
# dotenv.load_dotenv()
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="deepseek-ai/DeepSeek-V4-Flash",
#     base_url=os.getenv("OPENAI_BASE_URL"),
#     api_key=os.getenv("OPENAI_API_KEY")
# )
# res = llm.invoke([
#     ("system","请你返回一段JSON格式内容"),
#     ("human","请你给我讲个笑话")
# ])
# print(res.content)












#JSON格式输出  jsp=JsonOutputParser()


# import asyncio
# import os
# import dotenv
# from langchain_core.output_parsers import JsonOutputParser
#
# dotenv.load_dotenv()
# from langchain_openai import ChatOpenAI
#
# llm = ChatOpenAI(
#     model="deepseek-ai/DeepSeek-V4-Flash",
#     base_url=os.getenv("OPENAI_BASE_URL"),
#     api_key=os.getenv("OPENAI_API_KEY")
# )
# jsp=JsonOutputParser()#解析器
# res = llm.invoke([
#     ("system",jsp.get_format_instructions()),
#     ("human","请你给我讲个笑话")
# ])
# print(res.content)
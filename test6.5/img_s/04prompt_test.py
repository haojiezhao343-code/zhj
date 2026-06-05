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

from langchain_core.prompts import PromptTemplate
prompt=PromptTemplate(
    template="讲一个关于{topic}的{adjective}故事",
    input_variables=["topic", "adjective"],
)
formatted_prompt=prompt.invoke({"topic":"人工智能","adjective":"有趣的"})

print(llm.invoke(formatted_prompt).content)



# prompt=PromptTemplate.from_template(
#      "讲一个关于{topic}的{adjective}故事"
# )
# fixed_prompt=prompt.partial(adjective="有趣的")
# print(fixed_prompt.invoke({"topic":"编程"}))




# prompt=PromptTemplate(
#     template="请解释{concept},使用{style}风格",
#     input_variables=["concept"],
#     partial_variables={"style":"简单易懂"}
#
# )
# print(prompt.invoke({"concept":"递归"}))
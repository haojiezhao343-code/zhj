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

from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
examples = [
    {"input": "高兴", "output": "开心"},
    {"input": "难过", "output": "悲伤"},
    {"input": "生气", "output": "愤怒"}
]
example_formatter=PromptTemplate(
    template="输入：{input}\n输出:{output}",
    input_variables=["input","output"]
)
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_formatter,
    prefix="以下是一些同义词转换的例子：",
    suffix="\n输入: {input}\n输出:",
    input_variables=["input"]
)
print(few_shot_prompt.invoke({"input":"兴奋"}))
#对接LLM

prompt_value=few_shot_prompt.invoke({"input":"兴奋"})
resource=llm.invoke(prompt_value)
print(resource)
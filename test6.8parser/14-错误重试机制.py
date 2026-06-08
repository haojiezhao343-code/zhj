import os
import dotenv
dotenv.load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#1.定义提示词解析器
prompt=ChatPromptTemplate.from_template("请用一句话夸奖一下:{target}")
parser=StrOutputParser()

#2.初始化大模型
#提示：我们可以故意把timeout设置很短比如0.0001，来强行模拟“网络超时错误”
llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4-Pro",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=0.0001
)
#3.核心：为LLM组件外挂“自动重试”
#如果第一次失败，他会在后台让其第二次第三次直到超过规定的次数彻底死心
llm_with_retry=llm.with_retry(
    stop_after_attempt=5,
)

#4.组装LCEL链（把带重试的模型放进去）
retry_chain=prompt|llm_with_retry|parser
#5.执行调用
if __name__ == "__main__":
    try:
        print("正在发起请求（如果网络抖动，后台会自动重试）...")
        result=retry_chain.invoke({"target":"正在努里学习"})
        print(result)
    except Exception as e:
        print("\n[最终失败]哪怕重试了5次，依然没救回来，错误原因：")
        print(e)
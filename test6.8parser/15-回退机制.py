import os
import dotenv
dotenv.load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

#1.定义提示词解析器
prompt=ChatPromptTemplate.from_template("请用一句话解释一下什么是{concept}")
parser=StrOutputParser()
#2.初始化大模型
#提示：故意写错模型名，模型主力大模型彻底瘫痪
primary_llm = ChatOpenAI(
    model="V4-Pro",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=0.0001
)
#3.初始化备用模型
#提示：我们可以故意把timeout设置很短比如0.0001，来强行模拟“网络超时错误”
fallback_llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V4-Pro",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)
#4.核心：为主力模型绑定回退备用方案
llm_with_fallback=primary_llm.with_fallbacks([fallback_llm])
#5.组装LCEL链，把带回退能力的新对象放进里面
fallback_chain=prompt|llm_with_fallback|parser
#6.执行调用
if __name__ == "__main__":
    print("正在发送请求（主力模型配置错误，观察系统是否会自动切换到备用模型）....")
    try:
        result=fallback_chain.invoke({"concept":"大模型回退机制"})
        print("\n[调用成功最终大模型回复（注意，这其实是备用模型救场完成的）：]")
        print(result)
    except Exception as e:
        print("\n完蛋了，备用模型也挂了：",e)
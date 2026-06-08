import os
import dotenv
from langchain_core.output_parsers import StrOutputParser
dotenv.load_dotenv()
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
llm = init_chat_model(
    model_provider='openai',
    model="deepseek-ai/DeepSeek-V4-Flash",
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)
#创建两个链
chain1=(
    PromptTemplate.from_template("对这首诗做赏析，并分析含义:{sss}")|
    llm|StrOutputParser()
)
chain2=(
    PromptTemplate.from_template("对这首诗做赏析，并分析意境:{sss}")|
    llm|StrOutputParser()
)

summary_chain=(
    PromptTemplate.from_template(
       "第一种赏析:{chain1}\n\n第二种赏析{chain2}\n\n请比较哪一种更好，为什么"
    )|llm|StrOutputParser()
)
full_chain={
    'chain1': chain1,
    'chain2': chain2,
}|summary_chain
res=full_chain.invoke({"sss":"菩提本无树，明镜亦非台，本来无一物，何处惹尘埃。"})
print(res)
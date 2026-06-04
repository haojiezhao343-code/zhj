import os
import dotenv
dotenv.load_dotenv()
def streming_example():
    from langchain_openai import ChatOpenAI
    llm=ChatOpenAI(
        model="deepseek-ai/DeepSeek-V4-Pro",
        base_url=os.getenv("OPENAI_BASE_URL"),
        api_key=os.getenv("OPENAI_API_KEY")
    )
    print("AI回答.......")
    full_message=None
    for chunk in llm.stream("请写一手关于初遇的诗词"):
        full_message=chunk if full_message is None else full_message + chunk
        print(chunk.content,end="",flush=True)
    print(f"\n\n完整消息:\n{full_message.content}")
streming_example()

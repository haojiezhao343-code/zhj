import time
import os
import dotenv
dotenv.load_dotenv()
from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_openai import ChatOpenAI
rate_limiter = InMemoryRateLimiter(
    requests_per_second=0.1,
    check_every_n_seconds=0.1,
)
llm = ChatOpenAI(
    model="Pro/moonshotai/Kimi-K2.6",  # 多模态识图模型
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    rate_limiter=rate_limiter,
)

# def test_rate_limit(n=3):
#     print("开始时间:",time.strftime("%X"))
#     last=time.time()
#     for i in range(n):
#         t0 = time.time()
#         resp=llm.invoke(f"第{i}次调用，简单回一句就行")
#         t1 = time.time()
#         print(
#             f"调用{i}完成，耗时{t1-t0:.2f}s"
#             f"距上次调用结束间隔{t1-last:.2f}s"
#
#         )
#         last = t1
# test_rate_limit(3)





from langchain_core.callbacks import get_usage_metadata_callback
with get_usage_metadata_callback() as cb:
    llm.invoke("你好")
    llm.invoke("再见")
    print(cb.usage_metadata)
print(llm.profile)
from langchain_core.runnables import RunnablePassthrough,RunnableParallel
#场景一，直接传递输出
chain=RunnablePassthrough()
result=chain.invoke({"key":"value"})
print(result)
#场景二：保留原始输入+添加新字段
chain=RunnableParallel(
    original=RunnablePassthrough(),#保留原始输入
    uppercase=lambda x :x["text"].upper()#添加转换后的字段
)
result=chain.invoke({"text":"value"})
print(result)
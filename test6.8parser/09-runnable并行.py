from langchain_core.runnables import RunnableSequence,RunnableLambda,RunnableParallel
# p_chain=RunnableParallel({
#     'a':RunnableLambda(lambda x:len(x)),
#     'b':RunnableLambda(lambda x:x.upper()),
#     'c':RunnableLambda(lambda x:len(x.split())),
#     'd':RunnableLambda(lambda x:x[::-1]),
# })
# res=p_chain.invoke("hello world hello world")
# print(res)

#等价写法
# 字典语法自动创建RunnableParallel
chain = {
    "length": RunnableLambda(lambda x: len(x)),
    "uppercase": RunnableLambda(lambda x: x.upper()),
    "reversed": RunnableLambda(lambda x: x[::-1]),
    "word_count": RunnableLambda(lambda x: len(x.split()))
}
# 不能单独用，单独用实际是个字典不能invoke,如果想使用一定要是一个链chain
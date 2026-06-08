from itertools import chain

from langchain_core.runnables import RunnableSequence,RunnableLambda
# sequence_chain= RunnableSequence(
#     first=RunnableLambda(lambda x:x.upper()),
#     middle=[RunnableLambda(lambda x: f"HELLO{x}!")],#列表可以有多个中间节点
#     last=RunnableLambda(lambda x:f"最终输出:{x}"),
# )
# res=sequence_chain.invoke('world')
# print(res)



#推荐写法第二种
chain=(
    RunnableLambda(lambda x:x.upper())|
    RunnableLambda(lambda x: f"HELLO{x}!")|
    RunnableLambda(lambda x: f"HELLO{x}")|
    RunnableLambda(lambda x:f"最终输出:{x}")|
    RunnableLambda(lambda x: f"HELLO{x}!")
)
res=chain.invoke('world')
print(res)
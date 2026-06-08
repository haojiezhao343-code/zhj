from langchain_core.output_parsers import BaseOutputParser,StrOutputParser
class DemoOutputParser(BaseOutputParser):
    def parse(self,text:str):
        return [item.strip() for item in text.split(';')]#列表推导式
p=DemoOutputParser()#自定义输出解析器
res=p.parse("苹果;香蕉;橘子")
print(res)

from langchain_core.runnables import RunnableLambda
def extract_domain(url):
    return url.split('//')[-1].split('/')[0]
def add_protocol(domain):
    #添加前缀
    return f'http://{domain}'
#包装成Runnable
extractor_domain=RunnableLambda(extract_domain)
adder_protocol=RunnableLambda(add_protocol)
#在链中使用
url_processor=extractor_domain|adder_protocol
result=url_processor.invoke("https://www.example.com/path")
print(result)
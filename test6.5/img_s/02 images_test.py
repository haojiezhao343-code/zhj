import base64
import os
import dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()

llm = ChatOpenAI(
    model="Pro/moonshotai/Kimi-K2.6",  # 多模态识图模型
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY")
)

# with open("zhj.webp", "rb") as image_file:
#     image = image_file.read()
#
# message = HumanMessage(
#     content=[
#         {"type": "text", "text": "描述这张图片"},
#         {"type": "image_url", "image_url": {
#             "url": f"data:image/webp;base64,{base64.b64encode(image).decode('utf-8')}"
#         }}
#     ]
# )



with (open("zhj.webp", "rb") as f):
    binary_data = f.read()
    base64_bytes = base64.b64encode(binary_data)
    base64_string = base64_bytes.decode("utf-8")
binary_data = base64.b64decode(base64_string)
# response = llm.invoke([message])
# print(response.content)
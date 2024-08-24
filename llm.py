import os
from langchain_openai import ChatOpenAI
openAiKey = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(
    api_key=openAiKey,
)
response = llm.invoke("Hello, how are you?")
print(response)
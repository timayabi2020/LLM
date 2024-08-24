import os
from langchain_openai import ChatOpenAI
openAiKey = os.environ.get("OPENAI_API_KEY")
llm = ChatOpenAI(
    api_key=openAiKey,
    model="gpt-3.5-turbo",
    temperature=0.7,
)
response = llm.batch(["Hello, how are you?", "What is the meaning of life?"])

for chunk in response:
    print(chunk.content, end="", flush=True)
import os
from langchain_openai import ChatOpenAI
from langchain_core.propmts import ChatPromptTemplate
#Import API key from environment variables
openAiKey = os.environ.get("OPENAI_API_KEY")

#Create an instance of ChatOpenAI
llm = ChatOpenAI(
    api_key=openAiKey,
    model="gpt-3.5-turbo",
    temperature=0.7,
)
#Prompt templates
prompt = ChatPromptTemplate.from_template("Tell me a joke about a {subject}")

#Create LLM chain
chain = prompt | llm

response = chain.invoke({"subject": "chicken"})
print(response)
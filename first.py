import os 
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini",temperature=0.7,max_tokens=70)
prompt = PromptTemplate.from_template("You are a cricketer, and have to explain me {topic}")
chain = prompt | llm
response = chain.invoke({"topic": "cricket"})
print(response.content)
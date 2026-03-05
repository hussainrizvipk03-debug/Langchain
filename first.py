import os 
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage
import tiktoken
encoder = tiktoken.encoding_for_model("gpt-4o-mini")
chat_history = []
q_1 = "Hi My name is Hussain Adnan, How are you?"
r_1 = "Hey how are you doing I am well , Pleasure to meet you Hussain."
chat_history.append(HumanMessage(content=q_1))
chat_history.append(AIMessage(content=r_1))
load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini",temperature=0.7,max_tokens=20)
prompt = ChatPromptTemplate.from_messages([
    ('system', "You are a AI Engineer help me understand topics"),
    ('placeholder', "{chat_history}"),
    ('human', "{input}")
])

parser = StrOutputParser()

chain = prompt | llm | parser
response = chain.invoke({"chat_history": chat_history , "input": 'what is Machine Learning'})

formated_messages = prompt.format_messages(chat_history=chat_history, input="what is Machine Learning")
input_tokens = sum(len(encoder.encode(msg.content)) for msg in formated_messages)
output_tokens = len(encoder.encode(response))

print(f"no of input tokens:  {input_tokens}")
print(f"no of output tokens: {output_tokens}")



print(prompt)
print("-"*20)

chat_history.append(AIMessage(content=response))
print(chat_history)
print("-"*20)
print(response)
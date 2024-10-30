import os
import json
from http.client import responses

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# configure openai api key
working_dir = os.path.dirname(os.path.abspath(__file__))
config_data = json.load(open(f"{working_dir}/config.json"))
OPENAI_API_KEY = config_data["OPENAI_API_KEY"]
os.environ["OPENAI_API_KEY"]=OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-3.5-turbo",temperature=0)

def translate(input_lan, output_lan,input_text):
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that translates from one language to another."),
        ("user", f"Translate the following text from {input_lan} to {output_lan}:\n{input_text}"),
    ])
    chain = prompt | llm

    response = chain.invoke({
        "input_lan": input_lan,
        "output_lan": output_lan,
        "input_text": input_text
    })


    return response.content
import streamlit as st
import requests

import os
from dotenv import load_dotenv

load_dotenv()


## langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] ="true"

def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/essay/invoke",
                            json={'input':{'topic':input_text}})
    print(response.status_code)
    print(response.json())  # See the actual response
    return response.json()['output']['content']

st.title('Langchin demo with openAI chains')
input_text = st.text_input("write an essay on")

if input_text:
    st.write(get_openai_response(input_text))
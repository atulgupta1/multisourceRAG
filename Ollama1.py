import streamlit as st
from dotenv import load_dotenv
import os
from langchain.llms import Ollama

load_dotenv()

# Set environment variables if needed
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

st.title("Langchain demo with Ollama AI")

input_text = st.text_input("Search the topic you want")

if input_text:
    st.write(f"Input received: {input_text}")

    try:
        llm = Ollama(model="phi")
        
        # Combine system message and user input into one prompt string
        prompt = f"You are a helpful assistant.\nUser: {input_text}\nAssistant:"
        
        with st.spinner("Generating response..."):
            response = llm(prompt)
        
        st.write("Response received:")
        st.write(response)
        
    except Exception as e:
        st.error(f"Error occurred: {e}")

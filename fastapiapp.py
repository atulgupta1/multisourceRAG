from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import uvicorn
import os

# Load environment variables
load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

# Initialize FastAPI app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API server"
)

# OpenAI LLM route
openai_llm = ChatOpenAI()
add_routes(
    app,
    openai_llm,
    path="/openai"
)

# Define prompts
prompt1 = ChatPromptTemplate.from_template("Write an essay about {topic} with 20 words")
prompt2 = ChatPromptTemplate.from_template("Write a poem about {topic} for a 5-year-old child")

# OpenAI-based essay generator
add_routes(
    app,
    prompt1 | openai_llm,
    path="/essay"
)

# Ollama-based poem generator
ollama_llm = Ollama(model="phi")
add_routes(
    app,
    prompt2 | ollama_llm,
    path="/poem"
)

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

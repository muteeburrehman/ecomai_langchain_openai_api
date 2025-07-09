from langchain_openai import ChatOpenAI
from app.core.config import OPENAI_API_KEY

def get_llm():
    return ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-3.5-turbo", temperature=0.5)

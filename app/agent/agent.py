from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

def debug_code(code: str, traceback: str) -> str:
    prompt = f"""You are an expert Python debugger.

Code:
{code}

Error/Traceback:
{traceback}

Explain the root cause and suggest a fix."""
    
    response = llm.invoke(prompt)
    return response.content
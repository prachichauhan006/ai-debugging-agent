from langchain.tools import tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)

@tool
def diagnose_tool(error_info: str) -> str:
    """Analyzes Python error and identifies root cause."""
    response = llm.invoke(f"Identify the root cause of this Python error:\n{error_info}")
    return response.content

@tool
def fix_tool(error_info: str) -> str:
    """Suggests a fix for the diagnosed Python error."""
    response = llm.invoke(f"Suggest a fix for this Python error:\n{error_info}")
    return response.content

@tool
def validate_tool(fix_info: str) -> str:
    """Validates if the suggested fix is correct and complete."""
    response = llm.invoke(f"Validate if this fix is correct and complete:\n{fix_info}")
    return response.content
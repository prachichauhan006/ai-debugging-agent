from langchain_groq import ChatGroq
from dotenv import load_dotenv
from app.utils.code_parser import parse_traceback
import os

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.3-70b-versatile"
)

def debug_code(code: str, traceback: str) -> dict:
    parsed = parse_traceback(traceback)
    
    prompt = f"""You are an expert Python debugger.

Code:
{code}

Error Type: {parsed['error_type']}
Error Message: {parsed['error_message']}
File: {parsed['file_name']}
Line: {parsed['line_number']}
Full Traceback: {traceback}

Explain the root cause and suggest a fix."""

    response = llm.invoke(prompt)
    return {
        "parsed_error": parsed,
        "result": response.content
    }
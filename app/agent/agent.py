from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, ToolMessage
from dotenv import load_dotenv
from app.utils.code_parser import parse_traceback
from app.agent.tools import diagnose_tool, fix_tool, validate_tool
import os

load_dotenv()

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="llama-3.1-8b-instant"
)

tools = [diagnose_tool, fix_tool, validate_tool]
tools_map = {t.name: t for t in tools}
llm_with_tools = llm.bind_tools(tools)

def debug_code(code: str, traceback: str) -> dict:
    parsed = parse_traceback(traceback)
    
    messages = [HumanMessage(content=f"""You are an expert Python debugger.
First call diagnose_tool, then fix_tool, then validate_tool.

Code:
{code}

Error:
{traceback}""")]

    # Agentic loop
    while True:
        response = llm_with_tools.invoke(messages)
        messages.append(response)

        if not response.tool_calls:
            break

        for tool_call in response.tool_calls:
            tool = tools_map[tool_call["name"]]
            tool_result = tool.invoke(tool_call["args"])
            messages.append(ToolMessage(
                content=str(tool_result),
                tool_call_id=tool_call["id"]
            ))

    return {
        "parsed_error": parsed,
        "result": response.content
    }
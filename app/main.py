from fastapi import FastAPI
from pydantic import BaseModel
from app.agent.agent import debug_code

app = FastAPI(title="AI Debugging Agent")


class DebugRequest(BaseModel):
    code: str
    traceback: str

@app.get("/health")
def health():
    return {"status": "ok"}

# Main endpoint 
@app.post("/debug")
def debug(request: DebugRequest):
    result = debug_code(request.code, request.traceback)
    return {"result": result}

@app.post("/debug")
def debug(request: DebugRequest):
    result = debug_code(request.code, request.traceback)
    return result
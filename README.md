# AI Debugging Agent

> An AI-powered multi-step debugging agent that analyzes Python code and error tracebacks, identifies the root cause, suggests a fix, and validates it — built with LangChain, Groq (LLaMA 3), and FastAPI.

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square&logo=fastapi)
![LangChain](https://img.shields.io/badge/LangChain-1.3+-orange?style=flat-square)
![Groq](https://img.shields.io/badge/Groq-LLaMA3-purple?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

---

## Problem

Debugging is one of the most time-consuming parts of software development. Developers often spend more time understanding *why* an error occurred than fixing it — especially when stack traces are long, error messages are vague, or the bug is buried several function calls deep.

**AI Debugging Agent** closes that gap by acting as an automated first-pass debugger: given Python code and its error/traceback, a multi-step AI agent reasons through the failure and returns a structured explanation with a validated fix.

---

## How It Works  

```
User Input (source code + traceback)
        │
        ▼
   FastAPI /debug Endpoint
        │
        ▼
  Traceback Parser
  (extracts error type, message, file, line number)
        │
        ▼
  LangChain Agent (Groq LLaMA 3)
        │
        ├── Step 1: diagnose_tool  → identify root cause
        ├── Step 2: fix_tool       → suggest a fix
        └── Step 3: validate_tool  → validate the fix
        │
        ▼
  Structured JSON Response
  (parsed_error + agent result)
```

---

## Tech Stack

| Layer           | Technology                        |
|-----------------|-----------------------------------|
| LLM Inference   | Groq API (LLaMA 3.1 8B Instant)   |
| Agent Framework | LangChain + LangChain Core        |
| Backend API     | FastAPI + Uvicorn                 |
| Parsing         | Python `re` (regex-based)         |
| Testing         | pytest                            |
| Language        | Python 3.11+                      |

---

## Project Structure

```
ai-debugging-agent/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app + /debug endpoint
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── agent.py         # Agentic loop with tool calling
│   │   └── tools.py         # diagnose, fix, validate tools
│   └── utils/
│       ├── __init__.py
│       ├── code_parser.py   # Traceback parser
│       └── file_handler.py
├── tests/
│   └── test_parser.py       # pytest suite
├── .env                     # GROQ_API_KEY (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/prachichauhan006/ai-debugging-agent.git
cd ai-debugging-agent
```

### 2. Create and activate virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root:

```
GROQ_API_KEY=your_groq_api_key_here
```

Get your free API key at [console.groq.com](https://console.groq.com)

### 5. Run the server

```bash
uvicorn app.main:app --reload
```

Visit `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

---

## Usage

### API Endpoint

```
POST /debug
```

**Request Body:**

```json
{
  "code": "x = [1, 2, 3]\nprint(x[5])",
  "traceback": "File 'test.py', line 2, in <module>\nIndexError: list index out of range"
}
```

**Response:**

```json
{
  "parsed_error": {
    "error_type": "IndexError",
    "error_message": "list index out of range",
    "line_number": 2,
    "file_name": "test.py"
  },
  "result": "The IndexError occurs because index 5 is out of range for a list of length 3. Valid indices are 0-2. Fix: check the list length before accessing an index, or use a try-except block to handle the error gracefully."
}
```

---

## Running Tests

```bash
$env:PYTHONPATH="."      # Windows PowerShell
pytest tests/
```

Expected output:
```
collected 3 items
tests\test_parser.py ...   [100%]
3 passed in 0.04s
```

---

## Roadmap

- [x] Project setup — environment, dependencies, base FastAPI app
- [x] Groq + LangChain integration — LLM call working end-to-end
- [x] Traceback parser — extract file, line number, error type from raw traceback
- [x] Multi-step agentic flow — diagnose → fix → validate using LangChain tool calling
- [x] FastAPI endpoint — `/debug` route with structured JSON response
- [x] Test suite — pytest suite for traceback parser
- [ ] CLI interface — debug Python files directly from terminal
- [ ] File upload support — upload `.py` file instead of pasting code
- [ ] Error history — store past debug sessions (SQLite/PostgreSQL)
- [ ] Frontend — React.js UI for non-technical users
- [ ] Multi-language support — extend beyond Python (JavaScript, Java)

---

## Future Improvements

These are planned enhancements to make the agent more powerful:

- **Smarter context extraction** — instead of passing raw code, extract only the relevant function/block where the error occurred
- **Memory across sessions** — agent remembers past errors in a project and detects recurring patterns
- **VS Code extension** — integrate the agent directly into the editor as a sidebar tool
- **Confidence scoring** — agent rates how confident it is in the suggested fix
- **Auto-fix mode** — agent directly patches the file if confidence is above a threshold
- **Support for async errors** — handle asyncio tracebacks and concurrent execution errors
- **LLM-agnostic** — swap Groq for OpenAI, Anthropic, or a local Ollama model via config

---

## Why This Project

This project is part of a broader focus on applied AI engineering — building practical tools that use LLMs and agentic workflows to solve real developer pain points, rather than wrapping a chatbot around an existing UI.

The goal is not a demo. It is a working, extensible debugging agent with a clean API, structured output, and a test suite.

---

## Author

**Prachi Chauhan**
B.Tech CSE, AKTU (2027) · Python & AI Developer
[LinkedIn](https://linkedin.com/in/prachitechvision) · [Portfolio](https://prachichauhan006.github.io) · [GitHub](https://github.com/prachichauhan006)

---

## License

MIT

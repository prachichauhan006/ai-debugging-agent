# AI Debugging Agent

An AI-powered agent that analyzes Python code and error tracebacks, identifies the root cause, and suggests a fix — built using LangChain, Groq (LLM inference), and FastAPI.

> **Status:** In active development. Core architecture and roadmap defined below; implementation in progress.

---

## Problem

Debugging is one of the most time-consuming parts of software development. Developers often spend more time understanding *why* an error occurred than fixing it — especially when stack traces are long, error messages are vague, or the bug is buried several function calls deep.

**AI Debugging Agent** aims to close that gap by acting as an automated first-pass debugger: given a piece of code and its error/traceback, it reasons through the failure and returns a clear explanation along with a suggested fix.

---

## Goals

- Reduce time spent manually tracing Python errors back to their root cause
- Provide clear, human-readable explanations — not just a fix, but *why* the fix works
- Build a foundation that can later support multi-step (agentic) debugging workflows, not just single-shot error analysis

---

## Planned Architecture

```
User Input (source code + traceback)
        │
        ▼
   FastAPI Endpoint
        │
        ▼
  LangChain Agent (Groq LLM)
        │
        ├── Tool: Traceback Parser
        ├── Tool: Code Context Extractor
        └── Tool: Fix Suggestion Generator
        │
        ▼
  Structured Output
  (Root Cause + Explanation + Suggested Fix)
```

---

## Tech Stack

| Layer            | Technology              |
|-------------------|--------------------------|
| LLM Inference      | Groq API                |
| Agent Framework     | LangChain                |
| Backend API         | FastAPI                  |
| Language            | Python 3.11+              |
| (Planned) Frontend  | React.js                |

---

## Roadmap

- [ ] Project setup — environment, dependencies, base FastAPI app
- [ ] Groq + LangChain integration — basic LLM call working end-to-end
- [ ] Traceback parser tool — extract file, line number, error type from raw traceback
- [ ] Core debugging agent — combine code + traceback context to generate explanation and fix
- [ ] FastAPI endpoint — `/debug` route accepting code + error, returning structured response
- [ ] Test suite — validate agent on a set of common Python error types (IndexError, TypeError, KeyError, etc.)
- [ ] CLI or minimal frontend for trying the agent locally
- [ ] Documentation — usage examples, sample inputs/outputs

---

## Planned Usage (target API shape)

```python
POST /debug

{
  "code": "def divide(a, b):\n    return a / b\n\ndivide(10, 0)",
  "traceback": "ZeroDivisionError: division by zero"
}
```

**Expected response:**

```json
{
  "root_cause": "Division by zero in divide() when b=0",
  "explanation": "The function does not check if 'b' is zero before dividing...",
  "suggested_fix": "Add a check: if b == 0: raise ValueError('b cannot be zero')"
}
```

*(Exact response format may evolve as implementation progresses.)*

---

## Why This Project

This project is part of a broader move toward applied AI engineering — building practical tools that use LLMs and agentic workflows to solve real developer pain points, rather than wrapping a chatbot around an existing UI.

---

## Author

**Prachi Chauhan**
B.Tech CSE, AKTU (2027) · AI/ML & Full Stack Developer
[LinkedIn](https://linkedin.com/in/prachitechvision) · [Portfolio](https://prachichauhan006.github.io) · [GitHub](https://github.com/prachichauhan006)

---

## License

MIT

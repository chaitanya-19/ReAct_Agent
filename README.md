# ReAct Agent with Google ADK

Brief 2-line description of what the project does.

## Architecture
How the ReAct loop works in your agent — a simple text diagram like:

User Query → Agent Reasons → Calls google_search → Observes Results → Final Answer

## Tech Stack
- Google ADK 1.x
- Gemini 2.5 Flash
- Python 3.12

## Project Structure
Paste your folder tree here

## Setup
1. Clone the repo
2. Create venv and install: `pip install -e ".[dev]"`
3. Add `GOOGLE_API_KEY` to `.env`
4. Run: `adk web` from inside `src/`

## Running Tests
pytest tests/ -v

## Features
- ReAct reasoning pattern
- Real-time web search via Google Search grounding
- Full LLM request/response tracing with structured logging
- Conversation history persisted via ADK session service
```

---

**Then do these final things before pushing:**

1. Make sure `.gitignore` covers:
```
.env
.venv/
__pycache__/
*.pyc
.pytest_cache/
dist/
*.egg-info/
src/react_agent/.adk/
src/react_agent/agent_trace.log
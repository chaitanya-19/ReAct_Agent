# ReAct Agent with Google ADK

A production-style ReAct (Reason + Act) agent built with Google Agent Development Kit (ADK) and Gemini 2.5 Flash. The agent answers real-time questions by reasoning step-by-step and grounding its answers using Google Search.

## How it Works

The agent follows the ReAct loop:
```
User Query → Reason → Act (Google Search) → Observe Results → Reason Again → Final Answer
```

Every LLM request and response is traced via ADK callbacks and persisted to a structured log file — giving full visibility into the agent's reasoning process.

## Tech Stack

- **Google ADK 1.x** — agent framework and session management
- **Gemini 2.5 Flash** — LLM with native search grounding
- **Google Search (built-in ADK tool)** — real-time web grounding
- **Python 3.12** — src-layout packaging with pyproject.toml
- **pytest** — unit tests with no API calls

## Project Structure
```
ReAct_Agent/
├── src/
│   └── react_agent/
│       ├── __init__.py       # ADK entry point
│       ├── agent.py          # ReAct agent definition
│       ├── tools.py          # Google Search tool
│       └── callbacks.py      # LLM request/response tracing
├── tests/
│   └── test_agent.py         # Unit tests
├── .env.example              # API key template
├── .gitignore
├── pyproject.toml            # Dependencies and build config
└── README.md
```

## Setup

**1. Clone the repo**
```bash
git clone https://github.com/chaitanya-19/ReAct_Agent.git
cd ReAct_Agent
```

**2. Create a virtual environment and install dependencies**
```bash
python -m venv .venv
source .venv/bin/activate        # Mac/Linux
.venv\Scripts\activate           # Windows
pip install -e ".[dev]"
```

**3. Add your API key**
```bash
cp .env.example .env
# Add your Gemini API key inside .env
GOOGLE_API_KEY=your_key_here
```
Get a free key at [aistudio.google.com](https://aistudio.google.com)

**4. Run the agent**
```bash
cd src
adk web
```
Open `http://localhost:8000` in your browser.

## Example Queries

- *"What is the current age of the President of the United States?"*
- *"How old was the President of India in 1952, and what is that number times 3?"*
- *"What are the latest developments in AI this week?"*

## Running Tests
```bash
pytest tests/ -v
```

All tests run without making API calls.

## Key Design Decisions

- **Native ADK grounding** — uses ADK's built-in `google_search` tool instead of third-party search APIs
- **Callback-based tracing** — `before_model_callback` and `after_model_callback` log every LLM request, response, search queries fired, and token usage
- **Stateless LLM, stateful session** — ADK's session service (SQLite) reconstructs full conversation history on every request
- **src-layout + pyproject.toml** — modern Python packaging standards, no requirements.txt
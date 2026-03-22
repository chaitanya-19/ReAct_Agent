from src.react_agent.agent import root_agent
from src.react_agent.callbacks import before_model_callback, after_model_callback
from google.adk.tools.google_search_tool import GoogleSearchTool


def test_agent_name():
    assert root_agent.name == "react_agent"


def test_agent_model():
    assert root_agent.model == "gemini-2.5-flash"


def test_agent_has_search_tool():
    assert any(isinstance(t, GoogleSearchTool) for t in root_agent.tools)


def test_agent_has_instruction():
    assert root_agent.instruction is not None
    assert len(root_agent.instruction) > 0


def test_agent_has_callbacks():
    assert root_agent.before_model_callback.__name__ == "before_model_callback"
    assert root_agent.after_model_callback.__name__ == "after_model_callback"
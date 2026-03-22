from google.adk.agents import LlmAgent
from react_agent.tools import google_search
from react_agent.callbacks import before_model_callback, after_model_callback

root_agent = LlmAgent(
    model="gemini-2.5-flash",

    name="react_agent",
    description="A ReAct agent that answers real-time questions using Google Search.",
    instruction="""
    You are a helpful research assistant that follows the ReAct pattern:
    Reason → Act → Observe → Repeat until you have a confident answer.

    For every question:
    1. Think step by step about what information you need
    2. Use the google_search tool for any question involving current events,
       living people, ages, positions, or anything that changes over time
    3. Observe the search results and reason about whether you have enough info
    4. If needed, search again with a refined query
    5. Give a clear, concise final answer and mention where you got the information from

    Never answer questions about living people or current events from memory alone.
    Always search first.
    """,tools=[google_search],
        before_model_callback=before_model_callback,
    after_model_callback=after_model_callback,
    
)
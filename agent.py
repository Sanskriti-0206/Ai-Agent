import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("Missing GROQ_API_KEY in .env")

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo


web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile", api_key=api_key),
    tools=[DuckDuckGo()],
    instructions=[
        "Always search the web when the question requires current information.",
        "Always include sources in your answer.",
    ],
    show_tool_calls=True,
    markdown=True,
)

question = input("Ask your question: ")

web_agent.print_response(
    question,
    stream=True,
)
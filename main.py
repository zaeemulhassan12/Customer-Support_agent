# agent lab ...

from datetime import datetime
from pydantic import BaseModel # data part or data validation
# from typing import Optional

from langchain.agents import create_agent


def get_time() -> str:
    """Return current local time"""
    return datetime.now().strftime("%H:%M")

class Reply(BaseModel):
    is_greeting: bool
    time: str | None = None # Optional
    answer: str

agent = create_agent(
    model="ollama:gemma4:31b-cloud",
    tools=[get_time],
    system_prompt=(
        "You are a helpful AI Agent! "
        "If the user is greeting you, set is_greeting=true, call get_time, "
        "fill in time, and greet them based on the time of day. "
        "Otherwise set is_greeting=false and just answer normally."
    ),
    response_format=Reply
)

while True:
    query = input("Query (type 'exit' to quit): ")
    if query.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    result = agent.invoke(
        {"messages": [{"role": "user", "content": query}]}
    )

    response = result.get("structured_response")

    if response is None:
        print("Sorry, I couldn't generate a structured response. Please try again.")
        continue

    if response.is_greeting:
        print(f"Time: {response.time}")
        print(f"Greeting: {response.answer}")
    else:
        print(response.answer)


# Hi
# Time: 09:40
# Greetings: Hi
# What is NLP ?
# NLP is ...
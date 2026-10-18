from langchain.agents import create_agent
from pydantic import BaseModel
from typing import Literal

class Ticket(BaseModel):
    pass


agent = create_agent(
    model="ollama:gemma4:31b-cloud",
    tools=[],
    system_prompt=(
        "Classify the customer support messages "
    ),
    
)

message = input("Customer message: ")
result = agent.invoke(
    {"messages": [{"role": "user", "content": message}]}
)

print(result["messages"][-1].text)
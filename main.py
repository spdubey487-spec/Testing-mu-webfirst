from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

def dummy_tool(prompt):
    return f"Generating code for: {prompt}"

tools = [
    Tool(
        name="Code Generator",
        func=dummy_tool,
        description="Generates frontend and backend code based on user prompt"
    )
]

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

response = agent.run("Create a blog site with login and comment features")
print(response)

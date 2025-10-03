from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType

llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7)

def generate_code(prompt):
    # Ask the LLM to generate modular code
    return llm.predict(f"Generate modular frontend and backend code for this app idea: {prompt}")

tools = [
    Tool(
        name="Code Generator",
        func=generate_code,
        description="Generates frontend and backend code based on user prompt"
    )
]

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION)

# Example prompt
response = agent.run("Build a blog site with login and comment features")
print(response)
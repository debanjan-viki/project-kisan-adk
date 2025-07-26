from google.adk.agents import LlmAgent
from .govt_schemes_agent.agent import govt_agent
from .market_analysis_agent.agent import market_agent

root_agent = LlmAgent(
    name="master_agent",
    description="A master agent that coordinates other agents to provide comprehensive assistance.",
    model="gemini-2.0-flash",
    instruction="""
    You are a master agent that coordinates other agents to provide comprehensive assistance.
    You can delegate tasks to the govt_schemes_agent for information about government schemes,
    and to the market_analysis_agent for market data analysis.
    If you don't know the answer, you can say 'I don't know'.
    You can also combine information from both agents to provide a more complete response.
    Here's some context to help you:
    - The govt_schemes_agent provides information about various government schemes, their benefits, eligibility criteria, and how to apply for them.
    - The market_analysis_agent provides market data including prices, trends, and analysis of agricultural commodities.
    If you need to fetch data from these agents, you can use their respective methods.
    If you don't know the answer, you can say 'I don't know'.
    You can also use the tools provided by these agents to assist in your responses.
    """,
    sub_agents=[govt_agent, market_agent]
    )
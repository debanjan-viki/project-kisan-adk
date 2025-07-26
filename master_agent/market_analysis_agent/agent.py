from google.adk.agents import LlmAgent
from .market_analysis_tool import get_market_data

market_agent = LlmAgent(
    name="market_agent",
    description="An agent that provides market analysis for farming products in India.",
    model="gemini-2.0-flash",
    instruction="""
    You are a helpful assistant.
    Answer the user's questions and provide assistance based on the context.
    Use the provided context to inform your responses.
    If you're asked about farming market analysis, use the get_market_data tool and
    divide the min_price, max_price and modal_price received by 100 to get INR/KG value.
    If you don't know the answer, say "I don't know".
    """,
    tools=[get_market_data],
)
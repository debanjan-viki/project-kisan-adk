from google.adk.agents import LlmAgent
from .context import context

govt_agent = LlmAgent(
    name="govt_schemes_agent",
    description="An agent that provides information about government schemes.",
    model="gemini-2.0-flash",
    instruction=f"""
    You are a helpful assistant that provides information about government schemes.
    You can answer questions about various schemes, their benefits, eligibility criteria, and how to apply for them.
    Here's some context to help you: {context}
    If you don't know the answer, you can say 'I don't know'.
    """)
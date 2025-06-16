import streamlit as st
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from browser_use import Agent
import os

# Load OpenAI key from .env
load_dotenv()

async def run_agent(prompt):
    agent = Agent(
        task=prompt,
        llm=ChatOpenAI(
            model="gpt-4o",  # or "gpt-3.5-turbo" if needed
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )
    )
    await agent.run()

# --- Streamlit UI ---

st.set_page_config(page_title="Browser Agent", layout="centered")
st.title("MCP Browser Agent – Manual Prompt Mode")

with st.form("manual_prompt_form"):
    manual_prompt = st.text_area("Enter your custom prompt:", height=300, placeholder="E.g. Go to https://wikipedia.org and search for 'Python programming language'...")

    submitted = st.form_submit_button("Continue")

    if submitted:
        if manual_prompt.strip() == "":
            st.warning("Please enter a prompt before running.")
        else:
            st.subheader("Your Prompt")
            st.code(manual_prompt, language="markdown")

            st.success("Running browser agent with your custom prompt…")
            asyncio.run(run_agent(manual_prompt))
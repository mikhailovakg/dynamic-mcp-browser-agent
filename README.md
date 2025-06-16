# Dynamic MCP Browser Agent

A browser automation tool using OpenAI + `browser-use`. Run natural-language prompts like:
> "Go to https://example.com, log in, and open the dashboard."

## Setup

1. Clone this repo
2. Create and activate a virtual environment
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   playwright install chromium
4. Create .env from .env.example and add your secrets.

## Run the App
   ```bash
streamlit run app.py

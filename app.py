import os
import streamlit as st
from dotenv import load_dotenv
from agent import run_agent  # import your agent

# Load environment variables
load_dotenv()

st.set_page_config(
    page_title="Mini Agentic AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Mini Agentic AI Assistant")

# --- API Key Checks ---
openai_key = os.getenv("OPENAI_API_KEY")
weather_key = os.getenv("WEATHER_API_KEY")

if openai_key:
    st.success("✅ OpenAI key configured")
else:
    st.error("❌ OpenAI key missing — app will not work without it.")

if weather_key:
    st.info("🌦️ Weather tool enabled")
else:
    st.warning("⚠️ Weather tool disabled (add WEATHER_API_KEY to .env)")

# --- Show available tools ---
st.subheader("🛠️ Available Tools")
tools_list = ["Calculator", "File Reader", "Web Search"]
if weather_key:
    tools_list.append("Weather")
st.write(", ".join(tools_list))

# --- Chat Interface ---
st.subheader("💬 Chat with your Agent")

st.write("Ask me to calculate, search the web, or read from a file.")

query = st.text_area("Enter your query:", placeholder="e.g., What is 25*42?")

if st.button("Run Agent"):
    if query.strip():
        with st.spinner("Agent is thinking..."):
            response = run_agent(query)
        st.success("Done!")
        st.write("### Agent Response:")
        st.write(response)
    else:
        st.warning("Please enter a query first.")

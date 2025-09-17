import streamlit as st
from agent import run_agent

st.set_page_config(page_title="Mini Agentic AI", page_icon="🤖")

st.title("🤖 Mini Agentic AI Assistant")
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
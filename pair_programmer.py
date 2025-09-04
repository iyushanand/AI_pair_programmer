import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.agents import Tool

# Load environment variables from .env
load_dotenv()

st.title("🤖 AI Pair Programmer")

# Input box for prompt
prompt = st.text_area(
    "Describe the code you want:",
    height=150,
    placeholder="e.g. Write a function to reverse a linked list"
)

# Tool logic: generates Python code from natural language
def code_writer(prompt: str) -> str:
    llm = OpenAI(temperature=0.3)  # Uses OPENAI_API_KEY from environment
    full_prompt = (
        "You are an expert Python developer. "
        "ONLY return Python code, fully functional. "
        "Do NOT provide explanations, comments, or text. "
        f"Task: {prompt}"
    )
    return llm.invoke(full_prompt)  # Returns the generated Python code

# Button to trigger code generation
if st.button("Generate Code"):
    if not prompt.strip():
        st.warning("Please enter a prompt to generate code.")
    else:
        with st.spinner("Generating code..."):
            try:
                response = code_writer(prompt)
                st.code(response, language="python")
            except Exception as e:
                st.error(f"Error generating code: {e}")

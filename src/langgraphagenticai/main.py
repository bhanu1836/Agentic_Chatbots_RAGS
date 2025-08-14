import streamlit as st
import os

from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI 

def load_langgraph_agentic_ai_app():
    """
    Load the LangGraph Agentic AI application using Streamlit.
    """
    load_ui = LoadStreamlitUI()
    user_input = load_ui.load_streamlit_ui()

    if not user_input:
        st.error("Failed to load user input. Please check the configuration.")
        return
    
    user_message = st.chat_input("Enter your message:")

    if user_message:
        pass
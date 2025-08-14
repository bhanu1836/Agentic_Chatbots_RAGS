from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
import os,streamlit as st
from langchain_groq import ChatGroq

class groqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input
        
    def get_groq_llm_model(self):
        """
        Get the Groq LLM model based on user input.
        """
        try:
            groq_api_key = self.user_controls_input.get("Groq API Key")
            selected_model = self.user_controls_input.get("selected_model")
            if groq_api_key=='' and os.environ["Groq API Key"]=='':
                st.error("Please enter your Groq API Key to use Groq models.")

            llm = ChatGroq(api_key = groq_api_key, model=selected_model)
        except Exception as e:
            raise ValueError(f"Failed to initialize Groq LLM: {e}")
        
        return llm
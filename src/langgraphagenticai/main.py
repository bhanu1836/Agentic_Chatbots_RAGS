import streamlit as st
import os
from src.langgraphagenticai.LLMS.groqllm import groqLLM
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI 
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit

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
        try:
            obj_llm_config = groqLLM(user_controls_input=user_input)
            model = obj_llm_config.get_groq_llm_model()

            if not model:
                st.error("Failed to initialize the Groq LLM model. Please check your API key and model selection.")
                return
            
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Please select a use case.")
                return
            
            graph_builder = GraphBuilder(model)
            
            try:
                graph = graph_builder.setup_graph(usecase)
                DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph setup failed {e}")
                return
            

        except Exception as e:
            pass
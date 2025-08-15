import streamlit as st
import os

from src.langgraphagenticai.ui.uiconfigfile import config

class LoadStreamlitUI:
    def __init__(self):
        self.config = config()
        self.user_control={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖", layout="wide")
        st.header("🤖 "+self.config.get_page_title())
        st.session_state.timeFrame = ''
        st.session_state.IsFetchButtonClicked = False

        with st.sidebar:
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            self.user_control["selected_llm"] = st.selectbox("select LLM", llm_options)

            if self.user_control["selected_llm"] == "Groq":
                model_options = self.config.get_groq_model_options()
                self.user_control["selected_model"] = st.selectbox("select Groq model", model_options)
                self.user_control["Groq API Key"] =st.session_state["Groq API Key"] = st.text_input("API Key",type="password")

                if not self.user_control["Groq API Key"]:
                    st.warning("Please enter your Groq API Key to use Groq models.")

            ## Use case selection
            self.user_control["selected_usecase"] = st.selectbox("select Use Case", usecase_options)

            if self.user_control["selected_usecase"] == "ChatBot With Web" or self.user_control["selected_usecase"] == "AI News":
                os.environ["TAVILY_API_KEY"] = self.user_control["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILY API KEY",type="password")
                
                if not self.user_control["TAVILY_API_KEY"]:
                    st.warning("Please enter your TAVILY API Key to use Web search Functionality.")

            if self.user_control["selected_usecase"] == "AI News":
                st.subheader("📰 AI News Explorer")

                with st.sidebar:
                    time_frame = st.selectbox(
                        "📅 Select Time Frame",
                        ["Daily","Weekly","Monthly"],
                        index=0
                    )
                
                if st.button("🔍 Fetch Latest AI News",use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeFrame = time_frame

                
        return self.user_control

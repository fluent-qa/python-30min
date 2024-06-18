import os

import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def setup_apikey():
    with st.sidebar:
        openai_key = st.text_input(
            "OpenAI API Key",
            os.getenv("OPENAI_API_KEY"),
            type="password",
            help="please input your OpenAI API key",
        )
        if openai_key:
            os.environ["OPENAI_API_KEY"] = openai_key
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt4-o"


def ai_ui():
    st.title("openai chat root")

import streamlit as st
import os
from dotenv import load_dotenv
import  google.generativeai as gen_ai

load_dotenv()

st.set_page_config(page_title="Gemini AI", page_icon=":robot:", layout="centered")

google_api_key = os.getenv("GOOGLE_API_KEY")

gen_ai.configure(api_key=google_api_key)
model = gen_ai.GenerativeModel("gemini-pro")


def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "Gemini"
    else:
        return user_role


if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

st.title("Gemini AI")

for msg in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(msg["role"])):
        st.markdown(msg.parts[0].text)

user_promt = st.chat_input("Ask...")
if user_promt:
    with st.chat_message("user"):
        st.markdown(user_promt)

    gemini_response = st.session_state.chat_session.send_message(user_promt)

    with st.chat_message("Gemini"):
        st.markdown(gemini_response.text)
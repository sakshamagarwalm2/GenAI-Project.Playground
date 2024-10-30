import streamlit as st
from translator_utils import translate

st.set_page_config(
    page_title="Translator App",
    page_icon=":robot:" ,
    layout="centered"
)

# streamlit page title
st.title("Translator App - GPT4o")

col1, col2 = st.columns(2)
with col1:
    input_lan_list = ["English", "Hindi","German"]
    input_lan = st.selectbox(label="Select Language", options=input_lan_list)

with col2:
    output_lan_list = [x for x in input_lan_list if x != input_lan]
    output_lan = st.selectbox(label="Select Language", options=output_lan_list)

input_text = st.text_area("Type Here!")

if st.button("Translate"):
    translated_text = translate(input_text, input_lan, output_lan)
    st.success(translated_text)
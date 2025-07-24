import streamlit as st
from utils import chat_with_multimodal

st.set_page_config(page_title="Multimodal Chatbot", layout="wide")
st.title("🧠 Multimodal AI Chatbot")
st.write("Upload a PDF, image, or audio and ask anything about it!")

uploaded_file = st.file_uploader("Upload your file", type=["pdf", "png", "jpg", "jpeg", "mp3", "wav"])
user_question = st.text_input("Ask a question about the uploaded content:")

if uploaded_file and user_question:
    response = chat_with_multimodal(uploaded_file, user_question)
    st.success(response)
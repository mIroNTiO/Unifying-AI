import streamlit as st
import requests

st.set_page_config(page_title="Enlightenment AI", layout="wide")
st.title("🧠 Enlightenment AI (Frontend Demo Only)")

st.write("This is a Streamlit-only demo UI. Backend connection is disabled here.")

user_input = st.text_input("Ask a question:")

if user_input:
    st.warning("This demo does not include backend processing.")
    st.info("To test the full AI system, run it locally with FastAPI + LangChain.")

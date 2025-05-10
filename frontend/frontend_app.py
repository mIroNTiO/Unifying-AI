import streamlit as st
import requests

st.set_page_config(page_title="Enlightenment AI", layout="wide")

st.title("🧠 Enlightenment AI Assistant")
st.write("Ask a question and get a sourced, explainable response.")

# User input
user_input = st.text_input("Enter your question:")

# Display response
if user_input:
    with st.spinner("Thinking..."):
        try:
            response = requests.post("http://localhost:8000/ask", json={"question": user_input})
            if response.status_code == 200:
                data = response.json()
                st.markdown(f"### 💬 Answer:
{data['response']}")
                st.markdown(f"**Confidence:** {data['confidence'] * 100:.1f}%")
                st.markdown("**Sources:**")
                for source in data["sources"]:
                    st.markdown(f"- {source}")

                # Feedback buttons
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("👍 Helpful"):
                        requests.post("http://localhost:8000/feedback", json={
                            "question": user_input,
                            "response": data["response"],
                            "rating": "up"
                        })
                        st.success("Thanks for your feedback!")
                with col2:
                    if st.button("👎 Not helpful"):
                        requests.post("http://localhost:8000/feedback", json={
                            "question": user_input,
                            "response": data["response"],
                            "rating": "down"
                        })
                        st.warning("Feedback noted.")
            else:
                st.error("Error: Failed to get a response.")
        except Exception as e:
            st.error(f"Request failed: {e}")

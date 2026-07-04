import streamlit as st
from groq import Groq

# Page title setup
st.title("Amna's AI Assistant")
import streamlit as st
import os

# Secrets se key lein
api_key = st.secrets["GROQ_API_KEY"]

# Ab user se key maangne ki zaroorat nahi hai, 
# aap seedha apna model use karein

if api_key:
    client = Groq(api_key=api_key)

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": "You are a helpful assistant for Amna's AI Animated Shorts channel."}]

    # Chat history display
    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # User input
    if prompt := st.chat_input("Ask me anything about your channel..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        # Bot response
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.markdown(reply)
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.warning("Please enter your Groq API Key in the sidebar to start chatting.")

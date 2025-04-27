import os 
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from openai import OpenAI

# Ensure your API key is being correctly called
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise RuntimeError("❌ OPENAI_API_KEY not found. Please set it in your .env file.")
else:
    # (optionally mask most of it in logs)
    print(f"✅ OPENAI_API_KEY loaded: {openai_api_key[:4]}…")
    

client = OpenAI()
# Define the model you want to use
model = "o4-mini"

st.title("🤖 ChatBot Boilerplate")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Respond to user input 
if prompt := st.chat_input("Hello! Ask me a question... 👋"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
            "role": "system",
            "content": "You are a helpful, friendly assistant."
        },
        {
            "role": "user",
            "content": prompt
        }

        ]
    )
    reply = response.choices[0].message.content

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
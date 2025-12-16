import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read config from .env
TEMPERATURE = float(os.getenv("TEMPERATURE", 0.7))
MAX_TOKENS = int(os.getenv("MAX_TOKENS", 500))
# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    api_version=os.getenv("OPENAI_API_VERSION"),
    azure_endpoint=os.getenv("OPENAI_API_ENDPOINT")
)

# Streamlit page config
st.set_page_config(
    page_title="BasicChatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Basic Chatbot")
st.caption("Conversational AI, powered by Azure OpenAI")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful AI assistant."}
    ]

# Display chat history
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
user_input = st.chat_input("Ask something...")

if user_input:
    # Add user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Call Azure OpenAI
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=st.session_state.messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )

    ai_reply = response.choices[0].message.content

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(ai_reply)

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": ai_reply}
    )

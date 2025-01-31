import streamlit as st
from fin_bot import create_chain
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Check for API key
if not os.getenv("OPENAI_API_KEY"):
    st.error("Please set OPENAI_API_KEY in your .env file")
    st.stop()

# Set page config
st.set_page_config(page_title="Financial Assistant", page_icon="💰", layout="wide")

# Initialize session state for chat history if it doesn't exist
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chain" not in st.session_state:
    st.session_state.chain = None

# Add custom CSS
st.markdown("""
<style>
    .stTextInput {
        position: fixed;
        bottom: 3rem;
        background-color: white;
        padding: 1rem;
        z-index: 100;
    }
    .stButton {
        position: fixed;
        bottom: 3rem;
        right: 3rem;
        z-index: 100;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.title("💰 Financial Assistant")

# Initialize the chain if not already done
if st.session_state.chain is None:
    with st.spinner("Initializing the bot..."):
        st.session_state.chain = create_chain()
    st.success("Bot initialized successfully!")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything about finance..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chain.invoke({"input": prompt})
            st.markdown(response["output"])
            st.session_state.messages.append({"role": "assistant", "content": response["output"]}) 
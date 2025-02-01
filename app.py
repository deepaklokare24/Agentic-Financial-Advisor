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
st.set_page_config(page_title="Agentic Financial Advisor", page_icon="💰", layout="wide")

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
    .sample-questions {
        margin-bottom: 2rem;
    }
    .main-header {
        color: #1E88E5;
        font-size: 3rem !important;
        font-weight: 700 !important;
        margin-bottom: 1rem !important;
        text-align: center;
    }
    .subtitle-container {
        background: linear-gradient(135deg, #1E88E5 0%, #1565C0 100%);
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0 2rem 0;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .subtitle-text {
        font-size: 1.1rem;
        margin-bottom: 1rem;
        text-align: center;
        font-weight: 500;
    }
    .feature-list {
        list-style-type: none;
        padding-left: 0;
        margin: 0;
    }
    .feature-list li {
        padding: 0.5rem 0;
        margin: 0.5rem 0;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 5px;
        padding: 0.7rem 1rem;
        backdrop-filter: blur(5px);
    }
    .emoji-icon {
        font-size: 1.2rem;
        margin-right: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Main title and subtitle
st.markdown('<h1 class="main-header">🤖 Agentic Financial Advisor</h1>', unsafe_allow_html=True)
st.markdown("""
<div class="subtitle-container">
    <p class="subtitle-text">Your Intelligent Financial Companion</p>
    <ul class="feature-list">
        <li><span class="emoji-icon">📚</span> Deep financial knowledge from Zerodha</li>
        <li><span class="emoji-icon">📰</span> Real-time market insights from Yahoo Finance</li>
        <li><span class="emoji-icon">📊</span> Comprehensive financial data analysis from Financial Modeling Prep (FMP)</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Sample Questions Section
with st.expander("📚 Sample Questions - Click to expand"):
    st.markdown("### Try these example questions:")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("#### 🎓 Financial Knowledge")
        st.markdown("""
        - What is an index fund?
        - How do mutual funds work?
        - What is the difference between stocks and bonds?
        - How does dollar-cost averaging work?
        - What is portfolio diversification?
        - How does intraday trading work?
        - What is the difference between equity and debt?
        """)
        
    with col2:
        st.markdown("#### 📰 Market News")
        st.markdown("""
        - What happened with Microsoft stock today?
        - How is Apple performing compared to other tech stocks?
        - What are the latest developments in Tesla?
        - Which companies reported earnings today?
        - What's affecting the market today?
        - What are the recent market trends in tech sector?
        """)
        
    with col3:
        st.markdown("#### 📊 Financial Data")
        st.markdown("""
        - What's Apple's current stock price?
        - Compare Tesla and Ford's profit margins
        - What's the P/E ratio of Microsoft?
        - Show me Amazon's revenue growth
        - What's Netflix's market cap?
        - Get stock market prices and technical indicators
        - Analyze Apple's financial health by:
            1. Examining current ratios and debt levels
            2. Comparing profit margins to industry average
            3. Looking at cash flow trends
            4. Assessing growth metrics
        """)

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
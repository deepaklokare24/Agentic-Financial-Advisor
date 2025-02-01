# 🤖 Agentic Financial Advisor

An intelligent financial assistant that combines deep financial knowledge, real-time market insights, and comprehensive financial data analysis.

## 🌟 Features

### 1. Multi-Source Intelligence
- **📚 Zerodha Knowledge Base**: Educational content for understanding financial concepts
- **📰 Real-time Yahoo Finance News**: Latest market updates and company developments
- **📊 FMP Data Analysis**: Detailed financial metrics and market performance data

### 2. Advanced RAG System
- Conversation-aware retrieval
- Chat history integration
- Semantic search capabilities
- Context-aware responses

### 3. Tool Integration
- **Yahoo Finance Tool**: Real-time market news and updates
- **FMP Data Tool**: Comprehensive financial data analysis
- **Custom Knowledge Base Tool**: Access to Zerodha's educational content

## 🛠️ Technical Stack

- **Framework**: LangChain
- **Language Model**: OpenAI GPT-4
- **Vector Store**: FAISS
- **Embeddings**: OpenAI Embeddings
- **Frontend**: Streamlit
- **Data Sources**: 
  - Zerodha Varsity
  - Yahoo Finance API
  - Financial Modeling Prep API

## 🚀 Getting Started

### Prerequisites
```bash
- Python 3.8+
- OpenAI API Key
- FMP API Key
```

### Installation

1. Clone the repository:
```bash
git clone [your-repo-url]
cd [your-repo-name]
```

2. Create and activate a virtual environment:
```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
# Create .env file and add your API keys
OPENAI_API_KEY=your-openai-api-key
FMP_API_KEY=your-fmp-api-key
```

### Running the Application

```bash
streamlit run app.py
```

## 💡 Usage Examples

### Financial Knowledge Queries
- "What is an index fund?"
- "How do mutual funds work?"
- "What is the difference between stocks and bonds?"

### Market News Queries
- "What happened with Microsoft stock today?"
- "How is Apple performing compared to other tech stocks?"
- "What are the latest developments in Tesla?"

### Financial Data Analysis
- "What's Apple's current stock price?"
- "Compare Tesla and Ford's profit margins"
- "What's the P/E ratio of Microsoft?"

## 🏗️ Architecture

The application uses a three-tier architecture:
1. **Frontend Layer**: Streamlit interface
2. **Processing Layer**: LangChain for orchestration
3. **Data Layer**: Multiple data sources and vector store

## 📚 Documentation

For more information about the tools used:
- [Yahoo Finance Tool Documentation](https://python.langchain.com/docs/integrations/tools/yahoo_finance_news/)
- [FMP Data Tool Documentation](https://python.langchain.com/docs/integrations/tools/fmp-data/)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- LangChain for the amazing framework
- OpenAI for the language model
- Zerodha for the educational content
- Yahoo Finance for real-time market data
- Financial Modeling Prep for financial data

## 📞 Contact

[Your Name] - [Your Email/LinkedIn]

Project Link: [Your Repository URL]
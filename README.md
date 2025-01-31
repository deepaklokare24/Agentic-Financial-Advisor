# Financial Assistant Bot

An intelligent financial assistant that combines knowledge from Zerodha's educational content and real-time Yahoo Finance news to answer your financial queries.

## Features

- RAG (Retrieval Augmented Generation) system using Zerodha's Varsity content
- Real-time financial news integration using Yahoo Finance
- Chat history awareness for contextual conversations
- Beautiful Streamlit-based user interface
- Intelligent agent that chooses the right tool based on the query type
- Environment variable support for secure API key management

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Set up a virtual environment:
```bash
# Install virtualenv if you haven't already
pip install virtualenv

# Create a virtual environment
python -m virtualenv env

# Activate the virtual environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure your OpenAI API key:
   - Copy the `.env.example` file to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit the `.env` file and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

5. Run the Streamlit app:
```bash
streamlit run app.py
```

6. When you're done, deactivate the virtual environment:
```bash
deactivate
```

## Usage

1. The bot can answer questions about:
   - General financial concepts (from Zerodha's knowledge base)
   - Trading terminology
   - Investment basics
   - Current market news (from Yahoo Finance)
   - Recent company developments
   - Market trends

2. Simply type your question in the chat input and press Enter

3. The bot will automatically:
   - Choose the appropriate knowledge source
   - Provide relevant information
   - Maintain context through chat history
   - Cite sources when applicable

## Example Questions

- "What is the difference between equity and debt?"
- "What are the latest news about Tesla stock?"
- "Can you explain what a mutual fund is?"
- "What are the recent market trends in tech sector?"
- "How does intraday trading work?"

## Note

Make sure you have a valid OpenAI API key in your `.env` file. The key is required for both the language model and embeddings.

## Development

To update or modify the application:
1. Activate the virtual environment:
```bash
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

2. Make your changes

3. If you add new dependencies, update requirements.txt:
```bash
pip freeze > requirements.txt
```
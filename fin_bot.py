from langchain_openai import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_community.document_loaders import WebBaseLoader
from langchain.tools import Tool
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_community.tools import YahooFinanceNewsTool
from langchain.memory import ConversationBufferMemory
from langchain_fmp_data import FMPDataTool
import bs4
from langchain_community.document_loaders import RecursiveUrlLoader
from typing import List, Tuple
from langchain_core.messages import BaseMessage
import os
from dotenv import load_dotenv

from urllib.request import Request, urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import ssl
import sys

# Load environment variables
load_dotenv()

# Check for required API keys
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in environment variables")
if not os.getenv("FMP_API_KEY"):
    raise ValueError("FMP_API_KEY not found in environment variables")

def get_sitemap(url):
    req = Request(
        url=url,
        headers={"User-Agent": "Mozilla/5.0"}
    )
    response = urlopen(req)
    xml = BeautifulSoup(
        response,
        "lxml-xml",
        from_encoding=response.info().get_param("charset")
    )
    return xml


def get_urls(xml, name=None, data=None, verbose=False):
    urls = []
    for url in xml.find_all("url"):
        if xml.find("loc"):
            loc = url.findNext("loc").text
            urls.append(loc)
    return urls


def scrape_site(url = "https://zerodha.com/varsity/chapter-sitemap2.xml"):
    ssl._create_default_https_context = ssl._create_stdlib_context
    xml = get_sitemap(url)
    urls = get_urls(xml, verbose=False)

    docs = []
    print("scarping the website ...")
    for i, url in enumerate(urls):
        loader = WebBaseLoader(url)
        docs.extend(loader.load())
        if i % 10 == 0:
            print("\ti", i)
    print("Done!")
    return docs


def vector_retriever(docs):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000,
                                               chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    vectorstore = Chroma.from_documents(documents=splits,
                                    embedding=OpenAIEmbeddings())
    return vectorstore.as_retriever()


def create_chain():
    docs = scrape_site()
    retriever = vector_retriever(docs)

    # Create the YahooFinanceNewsTool
    yahoo_tool = YahooFinanceNewsTool(name="yahoo_finance_news")

    # Create the FMP Tool
    fmp_tool = FMPDataTool()
    fmp_tool.name = "fmp_data"  # Set the name after creation

    # Create a custom tool for our RAG system
    rag_tool = Tool(
        name="financial_kb",
        description="Use this tool for general financial knowledge queries about concepts, terms, and Zerodha-specific information.",
        func=lambda q: retriever.get_relevant_documents(q)
    )

    # Create the agent prompt
    system_prompt = """You are a helpful financial assistant that can answer questions about finance, trading, and investment.
    You have access to three main sources of information:
    1. A knowledge base containing information from Zerodha's educational content
    2. Real-time financial news from Yahoo Finance
    3. Detailed financial data from Financial Modeling Prep (FMP)

    Use the financial_kb tool when questions are about:
    - General financial concepts
    - Trading terminology
    - Zerodha-specific information
    - Investment basics

    Use the Yahoo Finance News tool when questions are about:
    - Current market news
    - Recent company developments
    - Market trends
    - Latest financial events

    Use the FMP tool when questions require:
    - Stock price information
    - Company financial ratios and metrics
    - Technical indicators
    - Financial statements
    - Company comparisons
    - Market performance data

    Always provide accurate, helpful responses and cite your sources when possible.
    If you don't know something, say so clearly.
    
    {chat_history}
    """

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ])

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    
    # Create the agent with all tools
    tools = [rag_tool, yahoo_tool, fmp_tool]
    agent = create_openai_functions_agent(llm, tools, prompt)
    
    # Create memory
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )
    
    # Create the agent executor
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        memory=memory,
        verbose=True
    )
    
    return agent_executor


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Expected one argument: the question")
        exit(1)

    # API key should be in environment variable now
    if not os.getenv("OPENAI_API_KEY"):
        print("Please set OPENAI_API_KEY environment variable")
        exit(1)

    chain = create_chain()
    response = chain.invoke({"input": sys.argv[1]})
    print("-----------------")
    print("Answer:")
    print(response["output"])

from phi.agent import Agent
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import os
from dotenv import load_dotenv, find_dotenv

_= load_dotenv(find_dotenv())
GROQ_API_KEY = os.environ["GROQ_API_KEY"]
PHIDATA_API_KEY = os.environ["PHIDATA_API_KEY"]

# Web Search Agent
web_search_agent = Agent(
    name = "Web Search Agent",
    role= "Search the web for the information",
    model= Groq(id="llama-3.1-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)


## Finance Agent
finance_agent = Agent(
    name= "F,inance AI Agent",
    model= Groq(id="llama-3.1-70b-versatile"),
    tools= [
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent=Agent(
    team=[web_search_agent, finance_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendations and share the latest news for NVDA", stream=True),
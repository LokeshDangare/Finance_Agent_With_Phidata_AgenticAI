import os
from dotenv import load_dotenv, find_dotenv
from phi.agent import Agent 
import phi.api
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import phi
from phi.playground import Playground, serve_playground_app

# Load environment variables from.env file
_ = load_dotenv(find_dotenv())
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

app = Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)


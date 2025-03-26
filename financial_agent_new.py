from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import groq

import os
from dotenv import load_dotenv
load_dotenv()
openai_api_key=os.getenv("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")

api_key = os.getenv("GROQ_API_KEY")

client = groq.Client(api_key=api_key)


#web search agent
web_search_agent=Agent(
  name="web search agent",
  role="search the web for the information",
  model=Groq(id="llama-3.3-70b-versatile"),
  tools=[DuckDuckGo()],
  instructions=["Alway include sources"],
  show_tools_calls=True,
  markdown=True,
  

)

#Financial Agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,

)
#Multiagent work
multi_ai_agent=Agent(
    team=[web_search_agent,finance_agent],
    instructions=["Always include sources","Use table to display the data"],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDAS",stream=True)

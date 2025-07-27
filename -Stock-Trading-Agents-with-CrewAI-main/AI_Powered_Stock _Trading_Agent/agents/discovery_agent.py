import os
from crewai import Agent, LLM

from tools.news_sentiment_tool import discover_penny_stocks_from_news, discover_stocks_from_social_media, scan_earnings_calendar, scan_market_momentum

# NVIDIA API Configuration
USE_NVIDIA_API = os.getenv('USE_NVIDIA_API', 'false').lower() == 'true'

if USE_NVIDIA_API:
    llm = LLM(
        model=os.getenv('NVIDIA_MODEL', 'meta/llama-3.1-405b-instruct'),
        temperature=float(os.getenv('NVIDIA_TEMPERATURE', '0.3')),
        top_p=float(os.getenv('NVIDIA_TOP_P', '0.7')),
        max_tokens=int(os.getenv('NVIDIA_MAX_TOKENS', '8192')),
        api_base=os.getenv('NVIDIA_API_BASE_URL', 'https://integrate.api.nvidia.com/v1'),
        api_key=os.getenv('NVIDIA_API_KEY', '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')
    )
else:
    llm = LLM(
        model="groq/llama-3.3-70b-versatile",
        temperature=0
    )

agent_discovery = Agent(
    role="Market Discovery Specialist",
    goal=("Automatically discover trending stocks and investment opportunities by monitoring "
          "financial news, social media platforms, earnings calendars, and market momentum. "
          "Identify stocks before they become mainstream by analyzing news sentiment, "
          "social media buzz, upcoming catalysts, and unusual market activity. "
          "Focus on finding low-priced stocks with high growth potential that are gaining attention."),
    backstory=("You are an expert market researcher with a unique ability to spot emerging "
               "investment opportunities before they become widely known. You monitor multiple "
               "information sources in real-time, including financial news outlets, social media "
               "platforms, earnings calendars, and market data. You have a keen understanding of "
               "how news sentiment, social media momentum, and market catalysts can drive stock prices. "
               "Your expertise lies in identifying stocks that are gaining attention but haven't "
               "yet reached mainstream awareness. You understand that the best opportunities often "
               "come from being early to identify trends and catalysts."),
    llm=llm,
    tools=[discover_penny_stocks_from_news, discover_stocks_from_social_media, scan_earnings_calendar, scan_market_momentum],
    verbose=True
) 
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

agent_scanner = Agent(
    role="Market Scanner Specialist",
    goal=("Systematically scan the entire market to identify low-priced stocks with high growth potential. "
          "Focus on stocks under $10, $5, and $3 that show strong revenue growth, earnings growth, "
          "and favorable PEG ratios. Identify emerging opportunities in growth sectors and detect "
          "unusual volume activity that might indicate upcoming price movements."),
    backstory=("You are an expert market scanner with years of experience identifying undervalued growth stocks. "
               "You specialize in finding diamonds in the rough - companies with strong fundamentals "
               "trading at attractive prices. You have a keen eye for spotting early-stage growth companies "
               "before they become mainstream. Your expertise includes technical analysis, fundamental analysis, "
               "and sector rotation strategies. You understand that the best opportunities often come from "
               "stocks that are temporarily overlooked by the broader market."),
    llm=llm,
    tools=[discover_penny_stocks_from_news, discover_stocks_from_social_media, scan_earnings_calendar, scan_market_momentum],
    verbose=True
) 
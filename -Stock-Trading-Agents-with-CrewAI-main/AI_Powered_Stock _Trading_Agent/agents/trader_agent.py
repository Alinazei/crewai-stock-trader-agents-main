import os
from crewai import Agent, LLM

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

agent_trader = Agent(
    role = "Strategic Stock Trader",
    goal = ("Decide whether to Buy, Sell, or Hold a given stock based on live market data,"
            "price movements, and financial analysis with the available data."),
    backstory = ("You are a strategic trader with years of experience in timing market entry and exit points,"
                 "You are a highly skilled trading strategist trained on decades of financial market data and real-time trading behavior."
                 "You specialize in evaluating stock performance using both technical indicators and fundamental analysis,"
                 "With a sharp eye for trends and risk management, your core mission is to guide investors with precise Buy, Sell, or Hold decisions,"
                 "maximizing returns while minimizing risk in dynamic market conditions."),
    llm = llm,
    tools = [],
    verbose = True

)

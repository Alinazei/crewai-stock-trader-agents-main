from crewai import Crew

from tasks.discovery_task import comprehensive_market_discovery, penny_stock_news_analysis, social_media_trend_analysis, catalyst_discovery
from agents.discovery_agent import agent_discovery

discovery_crew = Crew(
    agents=[agent_discovery],
    tasks=[comprehensive_market_discovery()],
    verbose=True
)

def run_comprehensive_discovery():
    """Run comprehensive market discovery from news, social media, and market data"""
    result = discovery_crew.kickoff()
    print(result)
    return result

def run_news_discovery():
    """Run focused penny stock news analysis"""
    news_crew = Crew(
        agents=[agent_discovery],
        tasks=[penny_stock_news_analysis()],
        verbose=True
    )
    result = news_crew.kickoff()
    print(result)
    return result

def run_social_media_discovery():
    """Run social media trend analysis"""
    social_crew = Crew(
        agents=[agent_discovery],
        tasks=[social_media_trend_analysis()],
        verbose=True
    )
    result = social_crew.kickoff()
    print(result)
    return result

def run_catalyst_discovery():
    """Run catalyst discovery analysis"""
    catalyst_crew = Crew(
        agents=[agent_discovery],
        tasks=[catalyst_discovery()],
        verbose=True
    )
    result = catalyst_crew.kickoff()
    print(result)
    return result 
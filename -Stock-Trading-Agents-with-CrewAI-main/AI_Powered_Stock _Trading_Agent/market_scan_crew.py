from crewai import Crew

from tasks.scan_task import market_scan_analysis, sector_focus_scan, penny_stock_analysis
from agents.scanner_agent import agent_scanner

market_scan_crew = Crew(
    agents=[agent_scanner],
    tasks=[market_scan_analysis()],
    verbose=True
)

def run_market_scan():
    """Run a comprehensive market scan for low-priced growth stocks"""
    result = market_scan_crew.kickoff()
    print(result)
    return result

def run_sector_scan(sector: str):
    """Run a focused scan on a specific sector"""
    sector_crew = Crew(
        agents=[agent_scanner],
        tasks=[sector_focus_scan(sector)],
        verbose=True
    )
    result = sector_crew.kickoff()
    print(result)
    return result

def run_penny_stock_scan():
    """Run a specialized penny stock analysis"""
    penny_crew = Crew(
        agents=[agent_scanner],
        tasks=[penny_stock_analysis()],
        verbose=True
    )
    result = penny_crew.kickoff()
    print(result)
    return result 
from crewai import Task
from agents.scanner_agent import agent_scanner

def market_scan_analysis():
    return Task(
        description=(
            "Perform a comprehensive market scan to identify low-priced stocks with high growth potential. "
            "Your analysis should include:\n\n"
            "1. **Low-Price Growth Stocks**: Scan for stocks under $10 with strong growth metrics\n"
            "2. **Penny Stock Opportunities**: Identify stocks under $5 with explosive growth potential\n"
            "3. **Micro-Cap Gems**: Find stocks under $3 that could be the next big winners\n"
            "4. **Sector Analysis**: Focus on high-growth sectors like Technology, Healthcare, and Energy\n"
            "5. **Volume Analysis**: Detect unusual volume spikes that might indicate upcoming moves\n\n"
            "For each category, provide:\n"
            "- Top 5-10 stock recommendations\n"
            "- Key growth metrics (revenue growth, earnings growth, PEG ratio)\n"
            "- Risk assessment and potential upside\n"
            "- Sector trends and market conditions\n\n"
            "Prioritize stocks that combine:\n"
            "- Strong revenue growth (>10%)\n"
            "- Positive earnings growth\n"
            "- Favorable PEG ratios (<1.5)\n"
            "- Reasonable market cap for liquidity\n"
            "- Positive technical indicators\n\n"
            "Provide actionable insights for investors looking for growth opportunities in undervalued stocks."
        ),
        agent=agent_scanner,
        expected_output=(
            "A comprehensive market scan report with:\n"
            "1. Executive summary of market opportunities\n"
            "2. Top low-price growth stocks with detailed analysis\n"
            "3. Penny stock recommendations with risk assessment\n"
            "4. Micro-cap opportunities with growth potential\n"
            "5. Sector-specific growth stocks\n"
            "6. Volume spike alerts and momentum plays\n"
            "7. Risk warnings and investment considerations\n"
            "8. Actionable investment recommendations"
        )
    )

def sector_focus_scan(sector: str):
    return Task(
        description=(
            f"Perform a focused scan of the {sector} sector to identify the best growth opportunities. "
            f"Analyze stocks in {sector} that meet the following criteria:\n\n"
            "1. **Growth Metrics**: Strong revenue and earnings growth\n"
            "2. **Valuation**: Attractive PEG ratios and price-to-sales ratios\n"
            "3. **Technical Strength**: Positive price momentum and volume trends\n"
            "4. **Market Position**: Competitive advantages and market share\n"
            "5. **Innovation**: New products, services, or market expansion\n\n"
            f"Focus on {sector} companies that are:\n"
            "- Trading at reasonable valuations\n"
            "- Showing accelerating growth\n"
            "- Benefiting from sector tailwinds\n"
            "- Positioned for future expansion\n\n"
            "Provide detailed analysis of the top 5-8 opportunities in this sector."
        ),
        agent=agent_scanner,
        expected_output=(
            f"Detailed {sector} sector analysis with:\n"
            "1. Sector overview and growth trends\n"
            "2. Top growth stocks with detailed metrics\n"
            "3. Competitive analysis and market positioning\n"
            "4. Risk factors and challenges\n"
            "5. Investment recommendations and price targets"
        )
    )

def penny_stock_analysis():
    return Task(
        description=(
            "Conduct a specialized analysis of penny stocks (under $5) with high growth potential. "
            "Focus on identifying the next big winners among micro-cap and small-cap companies.\n\n"
            "Analysis criteria:\n"
            "1. **Explosive Growth**: Companies with >20% revenue growth\n"
            "2. **Market Disruption**: Innovative products or services\n"
            "3. **Strong Management**: Experienced leadership teams\n"
            "4. **Market Opportunity**: Large addressable markets\n"
            "5. **Financial Health**: Strong balance sheets and cash flow\n\n"
            "Pay special attention to:\n"
            "- Biotech companies with promising drug pipelines\n"
            "- Tech startups with breakthrough technologies\n"
            "- Energy companies with new technologies\n"
            "- Companies in emerging markets or sectors\n\n"
            "Provide risk assessment and potential return scenarios for each recommendation."
        ),
        agent=agent_scanner,
        expected_output=(
            "Comprehensive penny stock analysis with:\n"
            "1. Top penny stock opportunities\n"
            "2. Growth potential and catalysts\n"
            "3. Risk assessment and volatility analysis\n"
            "4. Investment timeline and exit strategies\n"
            "5. Portfolio allocation recommendations"
        )
    )

# Export the main market scan task
market_scan = market_scan_analysis() 
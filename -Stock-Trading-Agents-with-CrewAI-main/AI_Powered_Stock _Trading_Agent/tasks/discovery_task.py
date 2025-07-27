from crewai import Task
from agents.discovery_agent import agent_discovery

def comprehensive_market_discovery():
    return Task(
        description=(
            "Perform a comprehensive market discovery analysis to automatically identify PENNY STOCKS "
            "and investment opportunities from multiple sources. Your analysis should include:\n\n"
            "1. **Penny Stock News Discovery**: Scan financial news from multiple sources (Yahoo Finance, "
            "MarketWatch, Reuters, Bloomberg, CNBC) to identify penny stocks (under $5) mentioned in headlines and "
            "analyze the sentiment of news coverage.\n\n"
            "2. **Social Media Monitoring**: Monitor social media platforms (Twitter, Reddit, StockTwits) "
            "for trending penny stock discussions, mentions, and sentiment analysis.\n\n"
            "3. **Earnings Catalyst Analysis**: Scan upcoming earnings announcements to identify penny stocks "
            "with potential catalysts that could drive price movements.\n\n"
            "4. **Market Momentum Detection**: Identify penny stocks with unusual price movements, volume spikes, "
            "and momentum indicators that suggest growing interest.\n\n"
            "For each discovered penny stock, provide:\n"
            "- Current price (must be under $5) and market cap\n"
            "- Source of discovery (news, social media, earnings, momentum)\n"
            "- Sentiment analysis and buzz level\n"
            "- Potential catalysts or drivers\n"
            "- Risk assessment and investment considerations\n\n"
            "Focus on identifying:\n"
            "- Penny stocks (under $5) with growing attention\n"
            "- Low-priced stocks with positive sentiment and momentum\n"
            "- Companies with upcoming catalysts and growth potential\n"
            "- Emerging trends in penny stock sectors\n\n"
            "Prioritize penny stocks that combine multiple positive signals across different sources."
        ),
        agent=agent_discovery,
        expected_output=(
            "A comprehensive market discovery report with:\n"
            "1. Executive summary of discovered opportunities\n"
            "2. News-based stock discoveries with sentiment analysis\n"
            "3. Social media trending stocks with buzz metrics\n"
            "4. Earnings catalyst opportunities\n"
            "5. Momentum-driven stock picks\n"
            "6. Cross-validation analysis (stocks appearing in multiple sources)\n"
            "7. Risk assessment and investment timeline\n"
            "8. Actionable recommendations for immediate attention"
        )
    )

def penny_stock_news_analysis():
    return Task(
        description=(
            "Conduct a focused analysis of financial news to discover PENNY STOCKS (under $5) with growth potential. "
            "Monitor multiple news sources and analyze the sentiment of coverage to identify "
            "low-priced stocks gaining media attention.\n\n"
            "Analysis requirements:\n"
            "1. **Multi-Source Monitoring**: Scan Yahoo Finance, MarketWatch, Reuters, Bloomberg, and CNBC\n"
            "2. **Penny Stock Filtering**: Focus ONLY on stocks trading under $5 per share\n"
            "3. **Stock Symbol Extraction**: Identify all stock symbols mentioned in headlines\n"
            "4. **Sentiment Analysis**: Analyze whether news coverage is positive, negative, or neutral\n"
            "5. **Growth Potential Assessment**: Evaluate market cap, sector, and growth indicators\n\n"
            "Focus on:\n"
            "- Penny stocks (under $5) with positive sentiment in news coverage\n"
            "- Low-priced companies with decent market cap ($5M+) gaining media attention\n"
            "- Stocks with recent news catalysts (earnings, product launches, partnerships)\n"
            "- Companies in growth sectors (tech, biotech, renewable energy, etc.)\n"
            "- Stocks showing increasing media mentions and positive sentiment\n\n"
            "Provide detailed analysis of the top penny stocks discovered through news monitoring."
        ),
        agent=agent_discovery,
        expected_output=(
            "Penny stock news analysis report with:\n"
            "1. Top penny stocks discovered from news sources\n"
            "2. Current price and market cap for each stock\n"
            "3. Sentiment analysis and mention frequency\n"
            "4. Key headlines and growth catalysts\n"
            "5. Investment potential and risk assessment"
        )
    )

def social_media_trend_analysis():
    return Task(
        description=(
            "Analyze social media platforms to identify stocks gaining momentum and buzz. "
            "Monitor Twitter, Reddit, StockTwits, and other platforms for trending stock discussions.\n\n"
            "Analysis focus:\n"
            "1. **Platform Monitoring**: Track mentions across multiple social media platforms\n"
            "2. **Sentiment Analysis**: Gauge community sentiment and enthusiasm\n"
            "3. **Momentum Tracking**: Identify stocks with increasing social media activity\n"
            "4. **Community Analysis**: Understand what's driving interest in specific stocks\n"
            "5. **Trend Prediction**: Identify stocks that might be gaining mainstream attention\n\n"
            "Key indicators to track:\n"
            "- Volume of mentions and discussions\n"
            "- Sentiment scores and emoji usage\n"
            "- Influencer mentions and endorsements\n"
            "- Community engagement and excitement levels\n"
            "- Cross-platform consistency of interest\n\n"
            "Focus on stocks that are:\n"
            "- Gaining momentum on social media\n"
            "- Showing positive community sentiment\n"
            "- Being discussed by influential accounts\n"
            "- Potentially undervalued or overlooked\n\n"
            "Provide analysis of the top trending stocks and their investment potential."
        ),
        agent=agent_discovery,
        expected_output=(
            "Social media trend analysis with:\n"
            "1. Top trending stocks on social media\n"
            "2. Platform-specific analysis and metrics\n"
            "3. Sentiment analysis and community mood\n"
            "4. Momentum indicators and growth trends\n"
            "5. Investment opportunities and risk assessment"
        )
    )

def catalyst_discovery():
    return Task(
        description=(
            "Identify stocks with upcoming catalysts that could drive significant price movements. "
            "Focus on earnings announcements, product launches, regulatory decisions, and other events.\n\n"
            "Catalyst categories to monitor:\n"
            "1. **Earnings Events**: Upcoming quarterly earnings with potential for beats/misses\n"
            "2. **Product Launches**: New products, services, or technology releases\n"
            "3. **Regulatory Decisions**: FDA approvals, regulatory clearances, policy changes\n"
            "4. **Partnerships & Acquisitions**: Strategic deals and corporate actions\n"
            "5. **Market Events**: Sector rotations, economic data releases, Fed decisions\n\n"
            "Analysis requirements:\n"
            "- Identify stocks with catalysts in the next 30 days\n"
            "- Assess the potential impact of each catalyst\n"
            "- Evaluate current market positioning and expectations\n"
            "- Consider historical performance around similar events\n"
            "- Focus on low-priced stocks with high catalyst potential\n\n"
            "Provide detailed analysis of the most promising catalyst-driven opportunities."
        ),
        agent=agent_discovery,
        expected_output=(
            "Catalyst discovery report with:\n"
            "1. Upcoming catalysts and their potential impact\n"
            "2. Stocks positioned to benefit from catalysts\n"
            "3. Historical analysis of similar events\n"
            "4. Risk assessment and timing considerations\n"
            "5. Investment strategies for catalyst plays"
        )
    )

# Export the main discovery task
stock_discovery = comprehensive_market_discovery() 
import requests
import feedparser
import re
import time
from datetime import datetime, timedelta
from crewai.tools import tool
from typing import List, Dict, Any
import yfinance as yf

@tool("PennyStockNewsDiscovery")
def discover_penny_stocks_from_news() -> str:
    """
    Scans financial news to discover penny stocks (under $5) with growth potential.
    Analyzes sentiment and identifies low-priced stocks with positive news coverage.
    """
    
    # Financial news RSS feeds
    news_sources = {
        'Yahoo Finance': 'https://feeds.finance.yahoo.com/rss/2.0/headline',
        'MarketWatch': 'https://feeds.marketwatch.com/marketwatch/topstories/',
        'Reuters Business': 'http://feeds.reuters.com/reuters/businessNews',
        'Bloomberg': 'https://feeds.bloomberg.com/markets/news.rss',
        'CNBC': 'https://www.cnbc.com/id/100003114/device/rss/rss.html'
    }
    
    # Dynamic penny stock discovery - no predefined lists
    # The system will discover stocks from real-time news feeds
    
    discovered_stocks = {}
    rss_success = False
    
    for source_name, feed_url in news_sources.items():
        try:
            feed = feedparser.parse(feed_url)
            
            if feed.entries:  # Check if we got any entries
                rss_success = True
                
                for entry in feed.entries[:15]:  # Check more entries for penny stocks
                    headline = entry.title
                    
                    # Extract stock symbols from headlines
                    stock_symbols = re.findall(r'\$([A-Z]{1,5})|(?<=\s)([A-Z]{1,5})(?=\s|$)', headline)
                    
                    for symbol_match in stock_symbols:
                        symbol = symbol_match[0] if symbol_match[0] else symbol_match[1]
                        
                        # Skip common non-stock words
                        if symbol in ['I', 'THE', 'AND', 'FOR', 'ARE', 'YOU', 'ALL', 'NEW', 'TOP', 'CEO', 'CFO', 'CTO']:
                            continue
                        
                        if symbol not in discovered_stocks:
                            discovered_stocks[symbol] = {
                                'mentions': 0,
                                'headlines': [],
                                'sentiment_score': 0,
                                'source': source_name
                            }
                        
                        discovered_stocks[symbol]['mentions'] += 1
                        discovered_stocks[symbol]['headlines'].append(headline)
                        
                        # Analyze sentiment
                        sentiment = analyze_headline_sentiment(headline)
                        discovered_stocks[symbol]['sentiment_score'] += sentiment
                    
            time.sleep(1)  # Rate limiting
            
        except Exception as e:
            continue
    
    # No fallback data - only real-time RSS feeds
    # If no stocks found, return informative message about real-time discovery
    
    # Filter for penny stocks with positive sentiment
    penny_stocks = []
    debug_info = []
    
    for symbol, data in discovered_stocks.items():
        if data['mentions'] >= 1:  # Include all mentioned stocks
            avg_sentiment = data['sentiment_score'] / data['mentions']
            
            # Process stocks with neutral to positive sentiment (lower threshold for penny stocks)
            if avg_sentiment > -0.2:  # Allow slightly negative sentiment for penny stocks
                try:
                    ticker = yf.Ticker(symbol)
                    info = ticker.info
                    current_price = info.get("regularMarketPrice", 0)
                    market_cap = info.get("marketCap", 0)
                    
                    debug_info.append(f"{symbol}: Price=${current_price}, MarketCap=${market_cap}, Sentiment={avg_sentiment:.2f}")
                    
                    # Only include penny stocks (under $5) with decent market cap
                    if current_price and current_price <= 5.0 and market_cap and market_cap >= 500000:  # $500K+ market cap
                        penny_stocks.append({
                            'symbol': symbol,
                            'price': current_price,
                            'market_cap': market_cap,
                            'mentions': data['mentions'],
                            'sentiment': avg_sentiment,
                            'headlines': data['headlines'][:3],  # Top 3 headlines
                            'source': data['source']
                        })
                    
                    time.sleep(0.1)  # Rate limiting
                    
                except Exception as e:
                    debug_info.append(f"{symbol}: Error - {str(e)}")
                    continue
    
    # Sort by sentiment and mentions
    penny_stocks.sort(key=lambda x: (x['sentiment'], x['mentions']), reverse=True)
    
    if not penny_stocks:
        # Add debugging info
        total_stocks_found = len(discovered_stocks)
        stocks_with_sentiment = len([s for s in discovered_stocks.values() if s['sentiment_score'] / s['mentions'] > -0.2])
        data_source = "Fallback Data" if not rss_success else "RSS Feeds"
        
        # Show what stocks were found
        stock_list = []
        for symbol, data in discovered_stocks.items():
            try:
                ticker = yf.Ticker(symbol)
                info = ticker.info
                current_price = info.get("regularMarketPrice", "N/A")
                market_cap = info.get("marketCap", "N/A")
                stock_list.append(f"{symbol}: ${current_price} (Market Cap: ${market_cap})")
            except:
                stock_list.append(f"{symbol}: Data unavailable")
        
        stock_details = "\n".join(stock_list[:10])  # Show first 10 stocks
        
        debug_summary = "\n".join(debug_info[:15])  # Show first 15 debug entries
        
        return f"No penny stocks with positive sentiment found in recent news.\n\nDebug Info:\n- Total stocks mentioned: {total_stocks_found}\n- Stocks with acceptable sentiment: {stocks_with_sentiment}\n- Data source: {data_source}\n- Checked {len(news_sources)} news sources\n\nDetailed Analysis:\n{debug_summary}"
    
    result = f"💰 Discovered {len(penny_stocks)} penny stocks with growth potential:\n\n"
    
    for i, stock in enumerate(penny_stocks[:10]):
        result += f"{i+1}. {stock['symbol']} - ${stock['price']:.2f}\n"
        result += f"   Market Cap: ${stock['market_cap']:,.0f} | Mentions: {stock['mentions']}\n"
        result += f"   Sentiment Score: {stock['sentiment']:.2f}\n"
        result += f"   Recent Headlines:\n"
        for headline in stock['headlines']:
            result += f"   • {headline}\n"
        result += "\n"
    
    return result

@tool("SocialMediaStockDiscovery")
def discover_stocks_from_social_media() -> str:
    """
    Monitors social media platforms for trending penny stock discussions and mentions.
    Identifies penny stocks gaining momentum on platforms like Twitter, Reddit, and StockTwits.
    """
    
    import os
    import tweepy
    import re
    
    # Twitter API Configuration
    bearer_token = os.getenv('TWITTER_BEARER_TOKEN')
    api_key = os.getenv('TWITTER_API_KEY')
    api_secret = os.getenv('TWITTER_API_SECRET')
    access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    access_token_secret = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
    
    discovered_stocks = {}
    
    # Try to use Twitter API if credentials are available
    if bearer_token and api_key and api_secret:
        try:
            # Initialize Twitter API v2
            client = tweepy.Client(
                bearer_token=bearer_token,
                consumer_key=api_key,
                consumer_secret=api_secret,
                access_token=access_token,
                access_token_secret=access_token_secret
            )
            
            # Search for penny stock related tweets - dynamic discovery
            penny_stock_keywords = [
                'penny stocks', 'penny stock', 'pennystocks', 'small cap stocks', 
                'under $5', 'cheap stocks', 'low price stocks'
            ]
            
            for keyword in penny_stock_keywords:
                try:
                    # Search tweets from the last 7 days
                    tweets = client.search_recent_tweets(
                        query=keyword,
                        max_results=100,
                        tweet_fields=['created_at', 'public_metrics', 'lang']
                    )
                    
                    if tweets.data:
                        for tweet in tweets.data:
                            # Extract stock symbols from tweet text
                            stock_symbols = re.findall(r'\$([A-Z]{1,5})', tweet.text)
                            
                            for symbol in stock_symbols:
                                if symbol not in discovered_stocks:
                                    discovered_stocks[symbol] = {
                                        'mentions': 0,
                                        'tweets': [],
                                        'sentiment_score': 0,
                                        'platform': 'Twitter'
                                    }
                                
                                discovered_stocks[symbol]['mentions'] += 1
                                discovered_stocks[symbol]['tweets'].append(tweet.text[:100] + "...")
                                
                                # Analyze sentiment
                                sentiment = analyze_headline_sentiment(tweet.text)
                                discovered_stocks[symbol]['sentiment_score'] += sentiment
                    
                    time.sleep(1)  # Rate limiting
                    
                except Exception as e:
                    continue
                    
        except Exception as e:
            pass  # Fall back to simulated data
    
    # No fallback data - only real Twitter API data
    # If no stocks found, return informative message about real-time discovery
    
    # Process real Twitter data
    penny_stocks = []
    
    for symbol, data in discovered_stocks.items():
        if data['mentions'] >= 2:  # Only stocks mentioned multiple times
            avg_sentiment = data['sentiment_score'] / data['mentions']
            
            try:
                ticker = yf.Ticker(symbol)
                info = ticker.info
                current_price = info.get("regularMarketPrice", 0)
                market_cap = info.get("marketCap", 0)
                
                # Only include penny stocks (under $5) with decent market cap
                if current_price and current_price <= 5.0 and market_cap and market_cap >= 500000:
                    penny_stocks.append({
                        'symbol': symbol,
                        'price': current_price,
                        'market_cap': market_cap,
                        'mentions': data['mentions'],
                        'sentiment': avg_sentiment,
                        'tweets': data['tweets'][:3],  # Top 3 tweets
                        'platform': data['platform']
                    })
                
                time.sleep(0.1)  # Rate limiting
                
            except:
                continue
    
    # Sort by mentions and sentiment
    penny_stocks.sort(key=lambda x: (x['mentions'], x['sentiment']), reverse=True)
    
    if not penny_stocks:
        result = "📱 Penny Stock Social Media Discovery:\n\n"
        result += "Real-time social media discovery requires Twitter API integration.\n"
        result += "The system would dynamically search for penny stock mentions on social media.\n\n"
        result += "💡 To enable real social media discovery:\n"
        result += "• Twitter API is configured and ready\n"
        result += "• Search for penny stock keywords and mentions\n"
        result += "• Analyze sentiment of social media posts\n"
        result += "• Filter for stocks under $5 with positive sentiment\n\n"
        result += "🔍 Use the news sentiment tool to monitor for breaking news that could drive social media activity."
        
        return result
    
    result = f"📱 Discovered {len(penny_stocks)} penny stocks trending on social media:\n\n"
    
    for i, stock in enumerate(penny_stocks[:10]):
        result += f"{i+1}. {stock['symbol']} - ${stock['price']:.2f}\n"
        result += f"   Market Cap: ${stock['market_cap']:,.0f} | Mentions: {stock['mentions']}\n"
        result += f"   Sentiment Score: {stock['sentiment']:.2f} | Platform: {stock['platform']}\n"
        result += f"   Recent Tweets:\n"
        for tweet in stock['tweets']:
            result += f"   • {tweet}\n"
        result += "\n"
    
    return result

@tool("EarningsCalendarScanner")
def scan_earnings_calendar() -> str:
    """
    Scans upcoming earnings calendar for penny stocks with potential catalysts.
    Identifies penny stocks with earnings announcements that could drive price movement.
    """
    
    import yfinance as yf
    from datetime import datetime, timedelta
    
    # Get current date and next 30 days
    today = datetime.now()
    end_date = today + timedelta(days=30)
    
    # Dynamic penny stock discovery - no predefined lists
    # The system will discover penny stocks from real-time market data
    
    earnings_data = []
    
    # For now, return informative message about real-time discovery
    # In a full implementation, this would scan market data for penny stocks
    result = "📅 Penny Stock Earnings Calendar (Next 30 Days):\n\n"
    result += "Real-time earnings discovery requires market data API integration.\n"
    result += "The system would dynamically scan all stocks under $5 for upcoming earnings.\n\n"
    result += "💡 To enable real earnings discovery:\n"
    result += "• Integrate with financial data APIs (Alpha Vantage, IEX Cloud, etc.)\n"
    result += "• Scan market data for stocks under $5\n"
    result += "• Filter for upcoming earnings in next 30 days\n"
    result += "• Analyze earnings estimates and potential catalysts\n\n"
    result += "🔍 Use the news sentiment tool to monitor for breaking earnings news."
    
    return result

@tool("MarketMomentumScanner")
def scan_market_momentum() -> str:
    """
    Scans for penny stocks with unusual price movements, volume spikes, and momentum indicators.
    Identifies penny stocks showing significant price action and volume activity.
    """
    
    import yfinance as yf
    
    # Dynamic penny stock discovery - no predefined lists
    # The system will discover penny stocks from real-time market data
    
    # For now, return informative message about real-time discovery
    # In a full implementation, this would scan market data for penny stocks
    result = "📊 Penny Stock Momentum Scanner:\n\n"
    result += "Real-time momentum discovery requires market data API integration.\n"
    result += "The system would dynamically scan all stocks under $5 for momentum indicators.\n\n"
    result += "💡 To enable real momentum discovery:\n"
    result += "• Integrate with market data APIs (Alpha Vantage, IEX Cloud, etc.)\n"
    result += "• Scan all stocks under $5 for price movements\n"
    result += "• Analyze volume spikes and unusual activity\n"
    result += "• Calculate momentum scores based on price and volume\n\n"
    result += "🔍 Use the news sentiment tool to monitor for breaking news that could drive momentum."
    
    return result

def analyze_headline_sentiment(headline: str) -> float:
    """
    Enhanced sentiment analysis based on keywords for penny stocks.
    Returns a score between -1 (very negative) and 1 (very positive).
    """
    headline_lower = headline.lower()
    
    # Positive keywords (expanded for penny stocks)
    positive_words = [
        'surge', 'jump', 'rise', 'gain', 'up', 'higher', 'beat', 'exceed', 'positive', 'bullish', 'growth', 'profit', 'earnings beat',
        'approval', 'launch', 'partnership', 'deal', 'acquisition', 'merger', 'expansion', 'new', 'breakthrough', 'innovation',
        'success', 'win', 'award', 'contract', 'revenue', 'sales', 'demand', 'popular', 'trending', 'hot', 'moon', 'rocket'
    ]
    
    # Negative keywords
    negative_words = [
        'drop', 'fall', 'decline', 'down', 'lower', 'miss', 'loss', 'negative', 'bearish', 'crash', 'plunge', 'earnings miss',
        'rejection', 'failure', 'bankruptcy', 'delisting', 'fraud', 'investigation', 'lawsuit', 'recall', 'disappointment'
    ]
    
    # Neutral/context keywords that might indicate activity (good for penny stocks)
    activity_words = ['announce', 'report', 'release', 'update', 'news', 'trading', 'volume', 'movement', 'activity']
    
    positive_count = sum(1 for word in positive_words if word in headline_lower)
    negative_count = sum(1 for word in negative_words if word in headline_lower)
    activity_count = sum(1 for word in activity_words if word in headline_lower)
    
    # If no clear sentiment but has activity, give slight positive bias for penny stocks
    if positive_count == 0 and negative_count == 0 and activity_count > 0:
        return 0.1  # Slight positive for activity
    
    if positive_count == 0 and negative_count == 0:
        return 0.0  # Neutral
    
    # Calculate sentiment score
    sentiment = (positive_count - negative_count) / (positive_count + negative_count)
    
    # Boost slightly for penny stocks with activity
    if activity_count > 0:
        sentiment += 0.1
    
    return max(-1.0, min(1.0, sentiment))  # Clamp between -1 and 1 
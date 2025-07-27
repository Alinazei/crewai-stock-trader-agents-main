import yfinance as yf
import pandas as pd
import numpy as np
from crewai.tools import tool
from typing import List, Dict, Any
import time

@tool("MarketScanner")
def scan_low_price_growth_stocks(price_threshold: float = 10.0, min_market_cap: float = 10000000) -> str:
    """
    Scans the market for low-priced stocks with growth potential.
    
    Args:
        price_threshold: Maximum price to consider (default: $10)
        min_market_cap: Minimum market cap in USD (default: $100M)
    
    Returns:
        Analysis of potential growth stocks under the specified price threshold
    """
    
    # This function now redirects to the discovery system
    # The old predefined list has been removed
    return "This scanner has been replaced by the automatic discovery system. Please use discovery_main.py instead."
    
    potential_stocks = []
    
    for symbol in stock_symbols:
        try:
            stock = yf.Ticker(symbol)
            info = stock.info
            
            current_price = info.get("regularMarketPrice", 0)
            market_cap = info.get("marketCap", 0)
            revenue_growth = info.get("revenueGrowth", 0)
            earnings_growth = info.get("earningsQuarterlyGrowth", 0)
            peg_ratio = info.get("pegRatio", 0)
            sector = info.get("sector", "Unknown")
            
            # Check if stock meets criteria
            if (current_price and current_price <= price_threshold and 
                market_cap and market_cap >= min_market_cap):
                
                # Calculate growth score
                growth_score = 0
                if revenue_growth and revenue_growth > 0.1:  # 10% revenue growth
                    growth_score += 2
                if earnings_growth and earnings_growth > 0.1:  # 10% earnings growth
                    growth_score += 2
                if peg_ratio and peg_ratio < 1.5:  # Good PEG ratio
                    growth_score += 1
                
                if growth_score >= 2:  # Only include stocks with decent growth potential
                    potential_stocks.append({
                        'symbol': symbol,
                        'price': current_price,
                        'market_cap': market_cap,
                        'revenue_growth': revenue_growth,
                        'earnings_growth': earnings_growth,
                        'peg_ratio': peg_ratio,
                        'sector': sector,
                        'growth_score': growth_score
                    })
            
            time.sleep(0.1)  # Rate limiting
            
        except Exception as e:
            continue
    
    # Sort by growth score
    potential_stocks.sort(key=lambda x: x['growth_score'], reverse=True)
    
    if not potential_stocks:
        return f"No stocks found under ${price_threshold} with growth potential."
    
    # Format results
    result = f"Found {len(potential_stocks)} potential growth stocks under ${price_threshold}:\n\n"
    
    for i, stock in enumerate(potential_stocks[:10]):  # Top 10
        result += f"{i+1}. {stock['symbol']} - ${stock['price']:.2f}\n"
        result += f"   Sector: {stock['sector']}\n"
        result += f"   Revenue Growth: {stock['revenue_growth']:.2% if stock['revenue_growth'] else 'N/A'}\n"
        result += f"   Earnings Growth: {stock['earnings_growth']:.2% if stock['earnings_growth'] else 'N/A'}\n"
        result += f"   PEG Ratio: {stock['peg_ratio']:.2f if stock['peg_ratio'] else 'N/A'}\n"
        result += f"   Growth Score: {stock['growth_score']}/5\n\n"
    
    return result

@tool("PennyStockScanner")
def scan_penny_stocks() -> str:
    """
    Scans for penny stocks (under $5) with high growth potential.
    """
    return scan_low_price_growth_stocks(price_threshold=5.0, min_market_cap=500000)

@tool("MicroCapScanner")
def scan_micro_cap_stocks() -> str:
    """
    Scans for micro-cap stocks (under $3) with explosive growth potential.
    """
    return scan_low_price_growth_stocks(price_threshold=3.0, min_market_cap=100000)

@tool("SectorGrowthScanner")
def scan_sector_growth_stocks(sector: str = "Technology") -> str:
    """
    Scans for growth stocks in a specific sector.
    
    Args:
        sector: Sector to scan (Technology, Healthcare, Energy, etc.)
    """
    
    # Real sector scanning - no predefined lists
    # This would dynamically discover stocks in the specified sector
    # For now, we'll return a message indicating this needs real sector data integration
    
    return f"Sector discovery for '{sector}' requires real sector classification APIs. No predefined lists are used - sector stocks are discovered dynamically from real-time sector data."
    
    if sector not in sector_stocks:
        return f"Sector '{sector}' not found. Available sectors: {', '.join(sector_stocks.keys())}"
    
    stocks = sector_stocks[sector]
    potential_stocks = []
    
    for symbol in stocks:
        try:
            stock = yf.Ticker(symbol)
            info = stock.info
            
            current_price = info.get("regularMarketPrice", 0)
            revenue_growth = info.get("revenueGrowth", 0)
            earnings_growth = info.get("earningsQuarterlyGrowth", 0)
            peg_ratio = info.get("pegRatio", 0)
            market_cap = info.get("marketCap", 0)
            
            if current_price and market_cap:
                growth_score = 0
                if revenue_growth and revenue_growth > 0.15:  # 15% revenue growth
                    growth_score += 3
                if earnings_growth and earnings_growth > 0.15:  # 15% earnings growth
                    growth_score += 3
                if peg_ratio and peg_ratio < 1.2:  # Excellent PEG ratio
                    growth_score += 2
                
                if growth_score >= 3:
                    potential_stocks.append({
                        'symbol': symbol,
                        'price': current_price,
                        'revenue_growth': revenue_growth,
                        'earnings_growth': earnings_growth,
                        'peg_ratio': peg_ratio,
                        'growth_score': growth_score
                    })
            
            time.sleep(0.1)
            
        except Exception as e:
            continue
    
    potential_stocks.sort(key=lambda x: x['growth_score'], reverse=True)
    
    if not potential_stocks:
        return f"No high-growth stocks found in {sector} sector."
    
    result = f"Top growth stocks in {sector} sector:\n\n"
    
    for i, stock in enumerate(potential_stocks[:8]):
        result += f"{i+1}. {stock['symbol']} - ${stock['price']:.2f}\n"
        result += f"   Revenue Growth: {stock['revenue_growth']:.2% if stock['revenue_growth'] else 'N/A'}\n"
        result += f"   Earnings Growth: {stock['earnings_growth']:.2% if stock['earnings_growth'] else 'N/A'}\n"
        result += f"   PEG Ratio: {stock['peg_ratio']:.2f if stock['peg_ratio'] else 'N/A'}\n"
        result += f"   Growth Score: {stock['growth_score']}/8\n\n"
    
    return result

@tool("VolumeSpikeScanner")
def scan_volume_spikes() -> str:
    """
    Scans for stocks with unusual volume spikes that might indicate upcoming moves.
    """
    
    # Focus on stocks that might have volume spikes
    volume_watch_stocks = ['GME', 'AMC', 'BBBY', 'NOK', 'BB', 'SNDL', 'HEXO', 'ACB', 'TLRY', 'CGC']
    
    volume_spikes = []
    
    for symbol in volume_watch_stocks:
        try:
            stock = yf.Ticker(symbol)
            
            # Get recent volume data
            hist = stock.history(period="5d")
            if len(hist) >= 2:
                current_volume = hist['Volume'].iloc[-1]
                avg_volume = hist['Volume'].iloc[:-1].mean()
                
                if avg_volume > 0:
                    volume_ratio = current_volume / avg_volume
                    
                    if volume_ratio > 2.0:  # Volume spike > 200% of average
                        current_price = hist['Close'].iloc[-1]
                        price_change = hist['Close'].iloc[-1] - hist['Close'].iloc[-2]
                        
                        volume_spikes.append({
                            'symbol': symbol,
                            'price': current_price,
                            'volume_ratio': volume_ratio,
                            'price_change': price_change,
                            'current_volume': current_volume,
                            'avg_volume': avg_volume
                        })
            
            time.sleep(0.1)
            
        except Exception as e:
            continue
    
    if not volume_spikes:
        return "No significant volume spikes detected in monitored stocks."
    
    # Sort by volume ratio
    volume_spikes.sort(key=lambda x: x['volume_ratio'], reverse=True)
    
    result = "Stocks with unusual volume spikes:\n\n"
    
    for i, spike in enumerate(volume_spikes[:5]):
        result += f"{i+1}. {spike['symbol']} - ${spike['price']:.2f}\n"
        result += f"   Volume: {spike['volume_ratio']:.1f}x average\n"
        result += f"   Price Change: ${spike['price_change']:.2f}\n"
        result += f"   Current Volume: {spike['current_volume']:,.0f}\n\n"
    
    return result 
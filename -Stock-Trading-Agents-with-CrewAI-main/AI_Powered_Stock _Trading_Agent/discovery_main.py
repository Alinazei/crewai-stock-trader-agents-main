from dotenv import load_dotenv
import config  # Import config to set NVIDIA API environment variables

from discovery_crew import run_comprehensive_discovery, run_news_discovery, run_social_media_discovery, run_catalyst_discovery

load_dotenv()

def main():
    print("🔍 AI-Powered Stock Discovery System")
    print("=" * 50)
    print("Automatically discovers stocks from news, social media, and market data")
    print("=" * 50)
    
    while True:
        print("\nChoose your discovery method:")
        print("1. 🔍 Comprehensive Discovery (All Sources)")
        print("2. 💰 Penny Stock News Analysis")
        print("3. 📱 Social Media Trend Analysis")
        print("4. ⚡ Catalyst Discovery")
        print("5. 🚪 Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            print("\n🔍 Running comprehensive market discovery...")
            print("This will scan news, social media, earnings, and market momentum...")
            run_comprehensive_discovery()
            
        elif choice == "2":
            print("\n💰 Scanning financial news for penny stocks with growth potential...")
            print("Monitoring: Yahoo Finance, MarketWatch, Reuters, Bloomberg, CNBC...")
            print("Focus: Stocks under $5 with positive sentiment...")
            run_news_discovery()
            
        elif choice == "3":
            print("\n📱 Analyzing social media trends...")
            print("Monitoring: Twitter, Reddit, StockTwits...")
            run_social_media_discovery()
            
        elif choice == "4":
            print("\n⚡ Scanning for upcoming catalysts...")
            print("Looking for earnings, product launches, regulatory decisions...")
            run_catalyst_discovery()
            
        elif choice == "5":
            print("\n👋 Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1-5.")
        
        print("\n" + "="*50)
        print("Discovery completed! Check the results above.")
        print("="*50)

if __name__ == "__main__":
    main() 
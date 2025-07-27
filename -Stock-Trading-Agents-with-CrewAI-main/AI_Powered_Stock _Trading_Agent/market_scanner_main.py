from dotenv import load_dotenv
import config  # Import config to set NVIDIA API environment variables

from market_scan_crew import run_market_scan, run_sector_scan, run_penny_stock_scan

load_dotenv()

def main():
    print("🚀 AI-Powered Market Scanner for Low-Price Growth Stocks")
    print("=" * 60)
    
    while True:
        print("\nChoose your scanning option:")
        print("1. Comprehensive Market Scan (All categories)")
        print("2. Sector-Specific Scan")
        print("3. Penny Stock Analysis")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            print("\n🔍 Running comprehensive market scan...")
            run_market_scan()
            
        elif choice == "2":
            print("\n📊 Available sectors: Technology, Healthcare, Energy, Financial, Consumer")
            sector = input("Enter sector name: ").strip().title()
            if sector:
                print(f"\n🔍 Scanning {sector} sector...")
                run_sector_scan(sector)
            else:
                print("Invalid sector name.")
                
        elif choice == "3":
            print("\n💰 Running penny stock analysis...")
            run_penny_stock_scan()
            
        elif choice == "4":
            print("\n👋 Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main() 
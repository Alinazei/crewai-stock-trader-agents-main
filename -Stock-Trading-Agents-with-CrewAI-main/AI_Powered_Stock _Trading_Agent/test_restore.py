#!/usr/bin/env python3
"""
Test script to verify that all restored files are working correctly
"""

import sys
import os

def test_imports():
    """Test that all modules can be imported successfully"""
    print("🔍 Testing imports...")
    
    try:
        # Test config import
        from config import DEFAULT_WATCHLIST
        print("✅ Config imported successfully")
        print(f"   Default watchlist: {DEFAULT_WATCHLIST}")
        
        # Test agent imports
        from agents.analyst_agent import agent_analyst
        print("✅ Analyst agent imported successfully")
        
        from agents.trader_agent import agent_trader
        print("✅ Trader agent imported successfully")
        
        from agents.scanner_agent import agent_scanner
        print("✅ Scanner agent imported successfully")
        
        from agents.discovery_agent import agent_discovery
        print("✅ Discovery agent imported successfully")
        
        # Test task imports
        from tasks.analyse_task import stock_analysis
        print("✅ Analysis task imported successfully")
        
        from tasks.trade_task import trade_execution
        print("✅ Trade task imported successfully")
        
        from tasks.scan_task import market_scan
        print("✅ Scan task imported successfully")
        
        from tasks.discovery_task import stock_discovery
        print("✅ Discovery task imported successfully")
        
        # Test tool imports
        from tools.stock_research_tool import stock_price
        print("✅ Stock research tool imported successfully")
        
        print("\n🎉 All imports successful! Files have been restored correctly.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_agent_zero():
    """Test the main Agent Zero chat interface"""
    print("\n🤖 Testing Agent Zero chat interface...")
    
    try:
        from agent_zero_chat import AgentZero
        print("✅ AgentZero class imported successfully")
        
        # Test instantiation
        agent_zero = AgentZero()
        print("✅ AgentZero instantiated successfully")
        print(f"   Watchlist: {agent_zero.watchlist}")
        print(f"   Agents available: {list(agent_zero.agents.keys())}")
        print(f"   Tasks available: {list(agent_zero.tasks.keys())}")
        
        print("🎉 Agent Zero chat interface is ready!")
        return True
        
    except Exception as e:
        print(f"❌ Agent Zero test failed: {e}")
        return False

def main():
    """Main test function"""
    print("🚀 Testing Stock Trading Agents Restoration")
    print("=" * 50)
    
    # Test imports
    imports_ok = test_imports()
    
    if imports_ok:
        # Test Agent Zero
        agent_zero_ok = test_agent_zero()
        
        if agent_zero_ok:
            print("\n🎉 SUCCESS: All files have been restored successfully!")
            print("\n💡 You can now run the trading system with:")
            print("   python agent_zero_chat.py")
            print("\n📋 Available commands:")
            print("   @analyst - Market analysis")
            print("   @trader - Trading decisions")
            print("   @scanner - Market scanning")
            print("   @discovery - Stock discovery")
            print("   Make $500 profit today - Team collaboration")
        else:
            print("\n❌ Agent Zero test failed")
            return 1
    else:
        print("\n❌ Import tests failed")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main()) 
#!/usr/bin/env python3
"""
Agent Zero - AI-Powered Stock Trading System
Interactive chat interface for trading agents
"""

import os
import sys
import asyncio
from datetime import datetime
from crewai import Crew, Process
from agents.analyst_agent import agent_analyst
from agents.trader_agent import agent_trader
from agents.scanner_agent import agent_scanner
from agents.discovery_agent import agent_discovery
from tasks.analyse_task import stock_analysis
from tasks.trade_task import trade_execution
from tasks.scan_task import market_scan
from tasks.discovery_task import stock_discovery
from config import DEFAULT_WATCHLIST

class AgentZero:
    def __init__(self):
        self.agents = {
            'analyst': agent_analyst,
            'trader': agent_trader,
            'scanner': agent_scanner,
            'discovery': agent_discovery
        }
        self.tasks = {
            'analyse': stock_analysis,
            'trade': trade_execution,
            'scan': market_scan,
            'discovery': stock_discovery
        }
        self.watchlist = DEFAULT_WATCHLIST
        self.session_start = datetime.now()
        
    def display_header(self):
        """Display the Agent Zero header"""
        print("╔══════════════════════════════════════════════════════════════════════════════╗")
        print("║                       🤖 AGENT ZERO                             ║")
        print("║                          Trading Agents                           ║")
        print("╚══════════════════════════════════════════════════════════════════════════════╝")
        print()
        print("🟢 SYSTEM STATUS")
        print(f"├─ Trading Mode: LIVE")
        print(f"├─ Live Trading: 🟢 ENABLED")
        print(f"├─ Auto-Execute: 🟢 ENABLED")
        print(f"└─ Session: {self.session_start.strftime('%H:%M:%S')}")
        print()
        print("🤖 AGENTS ONLINE")
        print("├─ 📊 analyst - Market Analysis")
        print("├─ ⚡ trader - Trading Execution")
        print("├─ 🛡️  risk - Risk Management")
        print("├─ 💼 portfolio - Portfolio Manager")
        print("├─ 📰 news - News & Sentiment")
        print("├─ 📈 performance - Performance Tracking")
        print("├─ 🎯 order_leader - Order Management")
        print("└─ 🌟 team - All Agents Collaboration")
        print()
        print("📋 WATCHLIST")
        print(f"└─ {self.watchlist}")
        print()
        print("💡 QUICK START")
        print("   @team Check my portfolio and optimize")
        print("   @analyst Analyze NIO technical signals")
        print("   Make $500 profit today")
        print("   @risk What are my current risks?")
        print()
        print("─" * 80)
        print("Type your message or @agent for specific agent. Press Ctrl+C to interrupt.")
        print("─" * 80)
        print()

    async def process_message(self, message):
        """Process user message and delegate to appropriate agents"""
        try:
            if message.lower() == 'e':
                return "exit"
                
            # Check for agent-specific commands
            if message.startswith('@'):
                agent_name = message[1:].split()[0].lower()
                if agent_name in self.agents:
                    return await self.handle_agent_command(agent_name, message)
                else:
                    return f"❌ Unknown agent: {agent_name}"
            
            # Default to team collaboration
            return await self.handle_team_command(message)
            
        except Exception as e:
            return f"❌ Error processing message: {str(e)}"

    async def handle_agent_command(self, agent_name, message):
        """Handle commands for specific agents"""
        agent = self.agents[agent_name]
        task = self.tasks.get(agent_name, stock_analysis)
        
        # Create crew with single agent
        crew = Crew(
            agents=[agent],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )
        
        result = await crew.kickoff()
        return f"🤖 {agent_name.upper()} AGENT RESPONSE:\n{result}"

    async def handle_team_command(self, message):
        """Handle team collaboration commands"""
        # Create crew with all agents
        crew = Crew(
            agents=list(self.agents.values()),
            tasks=[stock_analysis, trade_execution, market_scan],
            process=Process.sequential,
            verbose=True
        )
        
        result = await crew.kickoff()
        return f"🌟 TEAM COLLABORATION RESPONSE:\n{result}"

    async def run(self):
        """Main chat loop"""
        self.display_header()
        
        while True:
            try:
                print("\nUser message ('e' to leave):")
                message = input("> ").strip()
                
                if not message:
                    continue
                    
                result = await self.process_message(message)
                
                if result == "exit":
                    print("👋 Goodbye! Trading session ended.")
                    break
                    
                print(f"\n{result}")
                
            except KeyboardInterrupt:
                print("\n\n👋 Session interrupted. Goodbye!")
                break
            except Exception as e:
                print(f"❌ Unexpected error: {str(e)}")

async def main():
    """Main entry point"""
    agent_zero = AgentZero()
    await agent_zero.run()

if __name__ == "__main__":
    asyncio.run(main()) 
"""Tool 5: Local Environmental Impact Monitor - Monitor environmental impact."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an environmental monitoring and sustainability expert."""

def run():
    console.print("[bold cyan]🌍 Local Environmental Impact Monitor[/bold cyan]\n")
    
    area = Prompt.ask("[green]Area to monitor (campus, community, etc.)[/green]")
    focus = Prompt.ask("[green]Focus[/green]",
                      choices=["waste", "energy", "water", "biodiversity", "all"],
                      default="all")
    
    prompt = f"""Environmental monitoring plan:

Area: {area}
Focus: {focus}

1. 📊 KEY INDICATORS
2. 🔧 MONITORING METHODS
3. 📅 DATA COLLECTION SCHEDULE
4. 📈 ANALYSIS & REPORTING
5. 🎯 IMPROVEMENT TARGETS
6. 💡 ACTION RECOMMENDATIONS"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🌍 Environmental Monitoring", result, "green")

if __name__ == "__main__":
    run()

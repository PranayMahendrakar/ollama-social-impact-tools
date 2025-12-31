#!/usr/bin/env python3
"""Ollama Social Impact & Innovation Tools - 15 AI-Powered Changemaker Tools"""

import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import IntPrompt

console = Console()

TOOLS = {
    1: ("Campus Accessibility Analyzer", "tools.accessibility_analyzer", "Assess campus accessibility"),
    2: ("Community Outreach Campaign Designer", "tools.outreach_designer", "Design outreach campaigns"),
    3: ("Diversity & Inclusion Planner", "tools.diversity_planner", "Plan D&I initiatives"),
    4: ("Social Innovation Project Advisor", "tools.innovation_advisor", "Guide social innovation"),
    5: ("Local Environmental Impact Monitor", "tools.environmental_monitor", "Monitor environmental impact"),
    6: ("Mental Health Resource Navigator", "tools.mental_health_navigator", "Find mental health resources"),
    7: ("Educational Equity Assessment Tool", "tools.equity_assessment", "Assess educational equity"),
    8: ("Sustainable Campus Initiative Generator", "tools.sustainability_generator", "Generate sustainability ideas"),
    9: ("Public Health Campaign Builder", "tools.health_campaign", "Build health campaigns"),
    10: ("Digital Literacy Program Developer", "tools.digital_literacy", "Develop digital literacy"),
    11: ("Civic Engagement Opportunity Finder", "tools.civic_engagement", "Find civic opportunities"),
    12: ("Peer Support Network Coordinator", "tools.peer_support", "Build peer support networks"),
    13: ("Cultural Exchange Program Designer", "tools.cultural_exchange", "Design exchange programs"),
    14: ("Ethics in Technology Discussion Generator", "tools.tech_ethics", "Generate tech ethics discussions"),
    15: ("Student Activism Resource Guide", "tools.activism_guide", "Guide for student activism"),
}

def show_menu():
    console.clear()
    console.print(Panel.fit("[bold cyan]🌍 Ollama Social Impact & Innovation Tools[/bold cyan]\n[dim]15 AI-Powered Changemaker Tools[/dim]", border_style="cyan"))
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("#", style="cyan", width=4)
    table.add_column("Tool", style="green", width=40)
    table.add_column("Description", style="dim")
    for num, (name, _, desc) in TOOLS.items():
        table.add_row(str(num), name, desc)
    table.add_row("0", "Exit", "Quit")
    console.print(table)

def run_tool(choice: int):
    if choice == 0:
        console.print("[yellow]Goodbye! Keep making an impact! 🌍[/yellow]")
        sys.exit(0)
    if choice not in TOOLS:
        console.print("[red]Invalid choice.[/red]")
        return
    name, module_path, _ = TOOLS[choice]
    console.print(f"\n[bold green]Starting {name}...[/bold green]\n")
    try:
        module = __import__(module_path, fromlist=['run'])
        module.run()
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
    console.print("\n[dim]Press Enter to continue...[/dim]")
    input()

def main():
    try:
        import ollama
        ollama.list()
    except:
        console.print("[red]Ollama not running. Run: ollama serve[/red]")
        sys.exit(1)
    while True:
        show_menu()
        try:
            choice = IntPrompt.ask("Select", default=0)
            run_tool(choice)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()

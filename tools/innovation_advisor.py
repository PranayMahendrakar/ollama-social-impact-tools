"""Tool 4: Social Innovation Project Advisor - Guide social innovation projects."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a social entrepreneurship and innovation expert."""

def run():
    console.print("[bold cyan]💡 Social Innovation Project Advisor[/bold cyan]\n")
    
    console.print("[yellow]Describe your social innovation idea:[/yellow]")
    idea = get_multiline_input("Enter idea (type 'END' when done):")
    
    prompt = f"""Advise on social innovation project:

Idea: {idea}

1. 🎯 PROBLEM DEFINITION
2. 💡 SOLUTION REFINEMENT
3. 👥 STAKEHOLDER ANALYSIS
4. 📊 IMPACT MEASUREMENT
5. 💰 SUSTAINABILITY MODEL
6. 📋 IMPLEMENTATION ROADMAP
7. ⚠️ RISKS & MITIGATION"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("💡 Social Innovation", result, "cyan")

if __name__ == "__main__":
    run()

"""Tool 13: Cultural Exchange Program Designer - Design cultural exchange programs."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in cultural exchange and international education."""

def run():
    console.print("[bold cyan]🌍 Cultural Exchange Program Designer[/bold cyan]\n")
    
    program_type = Prompt.ask("[green]Program type[/green]",
                             choices=["virtual", "in-person", "hybrid"],
                             default="hybrid")
    scope = Prompt.ask("[green]Scope[/green]",
                      choices=["campus", "community", "international"],
                      default="campus")
    
    prompt = f"""Design cultural exchange program:

Type: {program_type}
Scope: {scope}

1. 🎯 PROGRAM GOALS
2. 👥 PARTICIPANT SELECTION
3. 📋 ACTIVITIES & EVENTS
4. 🤝 PARTNERSHIP BUILDING
5. 📅 TIMELINE
6. 📊 SUCCESS METRICS
7. 💡 CULTURAL SENSITIVITY GUIDELINES"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🌍 Cultural Exchange", result, "cyan")

if __name__ == "__main__":
    run()

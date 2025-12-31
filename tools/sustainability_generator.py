"""Tool 8: Sustainable Campus Initiative Generator - Generate sustainability initiatives."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a campus sustainability and green initiative expert."""

def run():
    console.print("[bold cyan]🌱 Sustainable Campus Initiative Generator[/bold cyan]\n")
    
    focus = Prompt.ask("[green]Focus area[/green]",
                      choices=["energy", "waste", "transportation", "food", "water", "all"],
                      default="all")
    scale = Prompt.ask("[green]Scale[/green]",
                      choices=["small", "medium", "large"],
                      default="medium")
    
    prompt = f"""Generate sustainability initiative:

Focus: {focus}
Scale: {scale}

1. 💡 INITIATIVE IDEAS (5)
   For each: description, impact, feasibility

2. 📋 IMPLEMENTATION PLAN
   - Steps
   - Timeline
   - Resources needed

3. 👥 STAKEHOLDER ENGAGEMENT
4. 📊 IMPACT METRICS
5. 💰 FUNDING IDEAS"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🌱 Sustainability Initiative", result, "green")

if __name__ == "__main__":
    run()

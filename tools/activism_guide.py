"""Tool 15: Student Activism Resource Guide - Guide for student activism."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in student activism, organizing, and social movements."""

def run():
    console.print("[bold cyan]✊ Student Activism Resource Guide[/bold cyan]\n")
    
    mode = Prompt.ask("[green]Mode[/green]",
                     choices=["start-campaign", "organize-event", "build-coalition", "learn-history"],
                     default="start-campaign")
    
    if mode == "start-campaign":
        cause = Prompt.ask("[green]Cause or issue[/green]")
        prompt = f"""Start activism campaign for: {cause}

1. 🎯 DEFINING YOUR GOALS
2. 📋 STRATEGY DEVELOPMENT
3. 👥 BUILDING SUPPORT
4. 📢 MESSAGING & OUTREACH
5. 🗓️ ACTION PLANNING
6. ⚖️ LEGAL CONSIDERATIONS
7. 💪 SUSTAINING MOMENTUM"""

    elif mode == "organize-event":
        prompt = """Organize activist event:

1. 📋 EVENT TYPES
2. 📅 PLANNING CHECKLIST
3. 📢 PROMOTION
4. ⚖️ PERMITS & LEGALITY
5. 🛡️ SAFETY PLANNING
6. 📊 MEASURING IMPACT"""

    elif mode == "build-coalition":
        prompt = """Build activist coalition:

1. 🔍 IDENTIFYING ALLIES
2. 🤝 PARTNERSHIP STRATEGIES
3. 📋 COALITION STRUCTURE
4. 💬 COMMUNICATION
5. 🎯 SHARED GOALS
6. ⚠️ NAVIGATING DIFFERENCES"""

    else:
        prompt = """Learn activism history:

1. 📚 KEY MOVEMENTS
2. 🎯 SUCCESSFUL TACTICS
3. 👤 INFLUENTIAL FIGURES
4. 💡 LESSONS LEARNED
5. 🔗 MODERN APPLICATIONS"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("✊ Activism Guide", result, "red")

if __name__ == "__main__":
    run()

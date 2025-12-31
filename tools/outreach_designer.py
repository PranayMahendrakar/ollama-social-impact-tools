"""Tool 2: Community Outreach Campaign Designer - Design outreach campaigns."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a community engagement and campaign design expert."""

def run():
    console.print("[bold cyan]📢 Community Outreach Campaign Designer[/bold cyan]\n")
    
    mode = Prompt.ask("[green]What would you like?[/green]",
                     choices=["design-campaign", "engagement-strategy", "messaging", "evaluation"],
                     default="design-campaign")
    
    cause = Prompt.ask("[green]Cause or issue[/green]")
    
    if mode == "design-campaign":
        audience = Prompt.ask("[green]Target audience[/green]")
        prompt = f"""Design outreach campaign:

Cause: {cause}
Audience: {audience}

1. 🎯 CAMPAIGN GOALS
2. 📋 KEY MESSAGES
3. 📱 CHANNELS
4. 📅 TIMELINE
5. 👥 VOLUNTEER ROLES
6. 📊 SUCCESS METRICS"""

    elif mode == "engagement-strategy":
        prompt = f"""Create engagement strategy for: {cause}

1. 👥 STAKEHOLDER MAPPING
2. 🤝 PARTNERSHIP OPPORTUNITIES
3. 📣 OUTREACH TACTICS
4. 🔄 SUSTAINED ENGAGEMENT"""

    elif mode == "messaging":
        prompt = f"""Develop messaging for: {cause}

1. 📝 KEY MESSAGES
2. 🎭 EMOTIONAL APPEALS
3. 📊 FACTS & DATA
4. 📣 CALLS TO ACTION"""

    else:
        prompt = f"""Evaluate campaign for: {cause}

1. 📊 METRICS TO TRACK
2. 🔍 DATA COLLECTION
3. 📈 ANALYSIS METHODS
4. 🔄 ITERATION"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("📢 Campaign Design", result, "green")

if __name__ == "__main__":
    run()

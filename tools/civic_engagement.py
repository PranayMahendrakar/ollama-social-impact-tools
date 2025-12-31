"""Tool 11: Civic Engagement Opportunity Finder - Find civic engagement opportunities."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a civic engagement and community involvement expert."""

def run():
    console.print("[bold cyan]🗳️ Civic Engagement Opportunity Finder[/bold cyan]\n")
    
    interests = Prompt.ask("[green]Your interests[/green]")
    time_available = Prompt.ask("[green]Time available[/green]",
                               choices=["1-2 hrs/week", "3-5 hrs/week", "5+ hrs/week"],
                               default="3-5 hrs/week")
    
    prompt = f"""Find civic engagement opportunities:

Interests: {interests}
Time: {time_available}

1. 🗳️ VOTING & ELECTIONS
2. 🤝 COMMUNITY SERVICE
3. 📢 ADVOCACY
4. 🏛️ LOCAL GOVERNMENT
5. 👥 CAMPUS ENGAGEMENT
6. 💡 GETTING STARTED TIPS"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🗳️ Civic Engagement", result, "magenta")

if __name__ == "__main__":
    run()

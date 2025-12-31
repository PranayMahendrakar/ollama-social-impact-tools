"""Tool 6: Mental Health Resource Navigator - Navigate mental health resources."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a mental health resource advisor. Always recommend professional help for serious concerns."""

def run():
    console.print("[bold cyan]🧠 Mental Health Resource Navigator[/bold cyan]")
    console.print("[yellow]For emergencies, contact crisis services immediately.[/yellow]\n")
    
    mode = Prompt.ask("[green]Mode[/green]",
                     choices=["find-resources", "wellness-tips", "support-others", "reduce-stigma"],
                     default="find-resources")
    
    if mode == "find-resources":
        need = Prompt.ask("[green]What type of support?[/green]")
        prompt = f"""Mental health resources for: {need}

1. 🏥 PROFESSIONAL RESOURCES
2. 📱 APPS & DIGITAL TOOLS
3. 👥 PEER SUPPORT
4. 📚 EDUCATIONAL RESOURCES
5. 🆘 CRISIS RESOURCES"""

    elif mode == "wellness-tips":
        prompt = """Daily mental wellness tips:

1. 🧘 MINDFULNESS
2. 🏃 PHYSICAL WELLNESS
3. 👥 SOCIAL CONNECTION
4. 📝 COPING STRATEGIES
5. 😴 SLEEP HYGIENE"""

    elif mode == "support-others":
        prompt = """Supporting others' mental health:

1. 👂 ACTIVE LISTENING
2. 🚩 RECOGNIZING SIGNS
3. 💬 STARTING CONVERSATIONS
4. 🔗 CONNECTING TO RESOURCES
5. 💚 SELF-CARE WHILE HELPING"""

    else:
        prompt = """Reduce mental health stigma:

1. 📢 AWARENESS CAMPAIGNS
2. 💬 LANGUAGE MATTERS
3. 📚 EDUCATION STRATEGIES
4. 🤝 NORMALIZING HELP-SEEKING"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🧠 Mental Health Resources", result, "blue")

if __name__ == "__main__":
    run()

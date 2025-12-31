"""Tool 14: Ethics in Technology Discussion Generator - Generate tech ethics discussions."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in technology ethics and digital philosophy."""

def run():
    console.print("[bold cyan]⚖️ Ethics in Technology Discussion Generator[/bold cyan]\n")
    
    topic = Prompt.ask("[green]Technology topic[/green]",
                      choices=["AI", "privacy", "social-media", "automation", "surveillance", "other"],
                      default="AI")
    
    prompt = f"""Generate ethics discussion on: {topic}

1. 🎯 KEY ETHICAL QUESTIONS
2. 📚 BACKGROUND CONTEXT
3. ⚖️ MULTIPLE PERSPECTIVES
4. 📋 DISCUSSION PROMPTS
5. 🔍 CASE STUDIES
6. 💡 REFLECTION QUESTIONS
7. 📖 FURTHER READING"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("⚖️ Tech Ethics Discussion", result, "yellow")

if __name__ == "__main__":
    run()

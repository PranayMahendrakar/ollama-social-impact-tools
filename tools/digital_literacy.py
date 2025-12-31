"""Tool 10: Digital Literacy Program Developer - Develop digital literacy programs."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a digital literacy and education technology expert."""

def run():
    console.print("[bold cyan]💻 Digital Literacy Program Developer[/bold cyan]\n")
    
    audience = Prompt.ask("[green]Target audience[/green]")
    focus = Prompt.ask("[green]Focus area[/green]",
                      choices=["basic-skills", "online-safety", "media-literacy", "coding", "all"],
                      default="all")
    
    prompt = f"""Develop digital literacy program:

Audience: {audience}
Focus: {focus}

1. 📚 LEARNING OBJECTIVES
2. 📋 CURRICULUM OUTLINE
3. 🎯 KEY SKILLS
4. 📱 TOOLS & RESOURCES
5. 📊 ASSESSMENT METHODS
6. 🔄 IMPLEMENTATION PLAN"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("💻 Digital Literacy Program", result, "blue")

if __name__ == "__main__":
    run()

"""Tool 9: Public Health Awareness Campaign Builder - Build health campaigns."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a public health communication expert."""

def run():
    console.print("[bold cyan]🏥 Public Health Awareness Campaign Builder[/bold cyan]\n")
    
    topic = Prompt.ask("[green]Health topic[/green]")
    audience = Prompt.ask("[green]Target audience[/green]", default="students")
    
    prompt = f"""Build health awareness campaign:

Topic: {topic}
Audience: {audience}

1. 📋 KEY MESSAGES
2. 📱 COMMUNICATION CHANNELS
3. 🎨 CREATIVE CONCEPTS
4. 📅 CAMPAIGN TIMELINE
5. 👥 PARTNERSHIPS
6. 📊 EVALUATION METRICS"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🏥 Health Campaign", result, "cyan")

if __name__ == "__main__":
    run()

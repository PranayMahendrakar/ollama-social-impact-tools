"""Tool 12: Peer Support Network Coordinator - Build peer support networks."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an expert in peer support programs and community building."""

def run():
    console.print("[bold cyan]🤝 Peer Support Network Coordinator[/bold cyan]\n")
    
    focus = Prompt.ask("[green]Support focus[/green]",
                      choices=["academic", "mental-health", "career", "social", "general"],
                      default="general")
    
    prompt = f"""Design peer support network:

Focus: {focus}

1. 📋 PROGRAM STRUCTURE
2. 👥 PEER SELECTION & TRAINING
3. 🤝 MATCHING SYSTEM
4. 📞 SUPPORT PROTOCOLS
5. 📊 EVALUATION
6. 🔄 SUSTAINABILITY"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🤝 Peer Support Network", result, "green")

if __name__ == "__main__":
    run()

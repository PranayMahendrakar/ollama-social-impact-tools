"""Tool 7: Educational Equity Assessment Tool - Assess educational equity."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an educational equity and access expert."""

def run():
    console.print("[bold cyan]📚 Educational Equity Assessment Tool[/bold cyan]\n")
    
    context = Prompt.ask("[green]Context (school, program, institution)[/green]")
    
    prompt = f"""Assess educational equity for: {context}

1. 📊 EQUITY INDICATORS
   - Access metrics
   - Outcome gaps
   - Resource distribution

2. 🔍 ASSESSMENT FRAMEWORK
   - Data to collect
   - Analysis methods

3. ⚠️ EQUITY GAPS
   - Potential areas of concern

4. 💡 RECOMMENDATIONS
   - Priority interventions
   - Best practices

5. 📋 ACTION PLAN
   - Implementation steps"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("📚 Equity Assessment", result, "yellow")

if __name__ == "__main__":
    run()

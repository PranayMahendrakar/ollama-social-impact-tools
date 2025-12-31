"""Tool 1: Campus Accessibility Analyzer - Assess campus accessibility."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are an accessibility expert helping improve campus inclusivity."""

def run():
    console.print("[bold cyan]♿ Campus Accessibility Analyzer[/bold cyan]\n")
    
    mode = Prompt.ask("[green]What would you like?[/green]",
                     choices=["audit-space", "recommendations", "policy-review", "learn"],
                     default="audit-space")
    
    if mode == "audit-space":
        console.print("\n[yellow]Describe the space to audit:[/yellow]")
        space = get_multiline_input("Enter description (type 'END' when done):")
        
        prompt = f"""Audit accessibility of: {space}

1. ♿ PHYSICAL ACCESS
2. 👁️ VISUAL ACCESSIBILITY
3. 👂 AUDITORY ACCESSIBILITY  
4. 🧠 COGNITIVE ACCESSIBILITY
5. ⚠️ ISSUES FOUND
6. 🔧 RECOMMENDATIONS"""

    elif mode == "recommendations":
        area = Prompt.ask("[green]Area to improve[/green]")
        prompt = f"""Accessibility recommendations for: {area}

1. 🎯 PRIORITY IMPROVEMENTS
2. 💰 LOW-COST OPTIONS
3. 📋 IMPLEMENTATION STEPS"""

    elif mode == "policy-review":
        prompt = """Review accessibility policy:

1. 📋 KEY REQUIREMENTS
2. ✅ COMPLIANCE CHECKLIST
3. 🔧 IMPROVEMENT AREAS"""

    else:
        prompt = """Learn about accessibility:

1. 📚 KEY CONCEPTS
2. ⚖️ LEGAL REQUIREMENTS
3. 💡 BEST PRACTICES"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("♿ Accessibility Analysis", result, "blue")

if __name__ == "__main__":
    run()

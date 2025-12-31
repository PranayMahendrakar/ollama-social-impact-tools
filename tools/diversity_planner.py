"""Tool 3: Diversity & Inclusion Initiative Planner - Plan D&I initiatives."""

from .base import console, chat, get_multiline_input, display_result, Prompt

SYSTEM_PROMPT = """You are a diversity, equity, and inclusion expert."""

def run():
    console.print("[bold cyan]🌈 Diversity & Inclusion Initiative Planner[/bold cyan]\n")
    
    mode = Prompt.ask("[green]Mode[/green]",
                     choices=["plan-initiative", "assess-needs", "training-design", "metrics"],
                     default="plan-initiative")
    
    context = Prompt.ask("[green]Context (organization/campus)[/green]")
    
    if mode == "plan-initiative":
        focus = Prompt.ask("[green]Focus area[/green]")
        prompt = f"""Plan D&I initiative:
Context: {context}
Focus: {focus}

1. 🎯 GOALS
2. 👥 STAKEHOLDERS
3. 📋 ACTION ITEMS
4. 📅 TIMELINE
5. 📊 SUCCESS METRICS
6. ⚠️ POTENTIAL CHALLENGES"""

    elif mode == "assess-needs":
        prompt = f"""Assess D&I needs for: {context}

1. 🔍 ASSESSMENT METHODS
2. ❓ KEY QUESTIONS
3. 📊 DATA TO COLLECT
4. 💡 ANALYSIS APPROACH"""

    elif mode == "training-design":
        prompt = f"""Design D&I training for: {context}

1. 📚 LEARNING OBJECTIVES
2. 📋 CONTENT OUTLINE
3. 🎯 ACTIVITIES
4. 📊 EVALUATION"""

    else:
        prompt = f"""D&I metrics for: {context}

1. 📊 KEY METRICS
2. 📈 DATA COLLECTION
3. 🎯 BENCHMARKS
4. 📋 REPORTING"""

    result = chat(prompt, SYSTEM_PROMPT)
    display_result("🌈 D&I Planning", result, "magenta")

if __name__ == "__main__":
    run()

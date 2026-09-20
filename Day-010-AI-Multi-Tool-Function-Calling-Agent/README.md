# Day 010 — AI Multi-Tool Function Calling Agent

**Difficulty:** 🟡 Intermediate Foundations  
**Focus:** function calling, tool registry, argument schemas, dispatch, observations, graceful failure

Day 009 executed one calculator tool. Day 010 closes the foundations phase by giving an agent a **toolbox** and teaching it to select the right function and arguments.

## Agent loop

`User → Choose tool → Validate call → Dispatch → Observe → Ground answer`

Available tools:
- `calculator(expression)` — safe AST arithmetic
- `word_count(text)` — deterministic text statistics
- `none` — graceful response when no tool applies

With `OPENAI_API_KEY`, the model selects a function using a constrained tool contract. Without a key, deterministic routing keeps the project runnable.

## Run

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py "calculate 24 * (8 + 2)"
python app.py "word count for AI agents can choose tools"
pytest -q
```

## Why this matters

Useful agents need more than prompts: they need explicit capabilities with narrow contracts. A registry separates reasoning from execution and makes adding, testing, auditing, and restricting tools easier.

## Study

Function calling, tool schemas, registries, dispatch, least privilege, argument validation, observations, graceful failure, and grounding answers in deterministic tool results.

## Extension challenge

Add weather and date/time tools, give each a Pydantic argument model, and record a trace for every decision and observation.

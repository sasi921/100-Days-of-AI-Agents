# Day 006 — AI Support Ticket Triage Bot

**Difficulty:** Beginner+  
**Topic:** Classification, routing, structured outputs

A runnable bot that turns customer support tickets into consistent routing decisions.

## What it does

For each ticket it returns structured JSON containing category, priority, sentiment, summary, next action, and whether human review is recommended.

This introduces an important agent pattern: **classify → route → act**.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py examples/sample_ticket.txt
```

The app works without an API key using a deterministic fallback. To use the LLM path, configure the variables shown in `.env.example`.

## Tests

```bash
pytest -q
```

## Concepts to study

- Classification as an AI primitive
- Strict structured outputs and JSON Schema
- Routing policies and escalation
- Separating trusted policy from untrusted customer text
- Deterministic fallbacks
- Human review for high-impact cases

## Extension challenge

Add SLA rules based on priority, then add a queue adapter that writes triaged tickets to SQLite.

## Next step

Later projects can turn routing recommendations into real tool calls and workflows.

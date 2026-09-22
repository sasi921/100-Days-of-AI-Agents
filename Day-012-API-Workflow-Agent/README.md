# Day 012 — API Workflow Agent

**Difficulty:** 🟡 Intermediate  
**Focus:** multi-step workflows, API tools, structured observations, aggregation, deterministic actions, error propagation

Day 011 crossed the network boundary. Day 012 turns a network tool into a **workflow**: fetch structured tasks, validate them, calculate status, and select the next action.

## Flow
`User ID → API tool → validate todos → aggregate status → choose next action → structured result`

The demo uses JSONPlaceholder, a public fake REST API, so no key is required.

## Run
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py 1
python app.py 1 --show-items
pytest -q
```

## Why this matters
Useful agents rarely make one isolated tool call. They execute **ordered steps**, pass observations between steps, enforce contracts, and stop cleanly when a dependency fails. This project keeps the policy deterministic so learners can see the workflow mechanics before model-driven planning is introduced.

## Study
Workflow decomposition, API adapters, Pydantic validation, aggregation, state passed between steps, deterministic action selection, network timeouts, and error propagation.

## Extension challenge
Add a second tool that persists the highest-priority pending item locally, then make the workflow require explicit approval before writing.

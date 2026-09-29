# Day 014 — SQL Data Analyst Agent

**Difficulty:** 🟡 Intermediate  
**Focus:** database tools, natural-language-to-SQL, read-only guardrails, structured observations

Day 013 introduced approval gates for writes. Day 014 adds a database tool while deliberately keeping the agent **read-only**.

## Architecture
`Question → SQL planner → read-only validator → SQLite tool → rows → structured observation`

The project seeds a tiny local sales dataset automatically. With `OPENAI_API_KEY`, an LLM can translate questions to SQL. Without a key, deterministic mappings keep the project runnable.

## Run
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py "Show sales by region"
python app.py "Who are the top customers by revenue?"
pytest -q
```

## Safety boundary
The SQL validator accepts only one `SELECT`/CTE statement and blocks mutation/admin keywords. This is intentionally defense-in-depth: model output is treated as untrusted until validated.

> For production, also use a database account with database-enforced read-only permissions, query timeouts, row limits, and an allowlisted schema.

## Study
Natural-language-to-SQL, database tool contracts, least privilege, schema grounding, SQL validation, structured observations, and why application checks should not be your only security boundary.

## Extension challenge
Add an `EXPLAIN QUERY PLAN` step and a maximum-row policy before execution.

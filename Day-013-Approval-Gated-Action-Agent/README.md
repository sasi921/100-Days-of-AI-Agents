# Day 013 — Approval-Gated Action Agent

**Difficulty:** 🟡 Intermediate  
**Focus:** human-in-the-loop, approval gates, state-changing tools, least privilege, audit-friendly execution

Day 012 chained API steps into a workflow. Day 013 adds a critical boundary: **planning an action is not permission to execute it**.

## Flow

`Request → Action proposal → Validation → Approval gate → Execute or deny → Record`

The agent proposes a local task creation action, but it cannot mutate state until the caller supplies explicit approval.

## Why this matters

As agents gain access to email, calendars, databases, browsers, GitHub, and infrastructure, a correct plan can still have costly consequences. Production systems need explicit boundaries between **reasoning**, **authorization**, and **execution**.

This project is deterministic on purpose: learners can inspect the permission architecture without hiding it behind an LLM.

## Run

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Propose only — no file is changed
python app.py "create task Review the production deployment"

# Explicitly approve execution
python app.py "create task Review the production deployment" --approve

# Explicitly deny
python app.py "create task Review the production deployment" --deny

pytest -q
```

Approved actions are stored in `tasks.json`.

## Safety properties

- **Deny by default:** absence of approval never executes.
- **Plan/execution separation:** proposal creation has no side effects.
- **Explicit authorization:** only `--approve` crosses the write boundary.
- **Validated contracts:** Pydantic constrains action shape and title length.
- **Auditable result:** every outcome returns `awaiting_approval`, `denied`, or `executed`.

## Concepts to study

Human-in-the-loop design, least privilege, approval gates, state-changing tools, action schemas, side-effect isolation, auditability, and why authorization must be separate from model reasoning.

## Extension challenge

Add multiple risk levels. Auto-allow read-only tools, require approval for writes, and require a second approver for high-risk actions.

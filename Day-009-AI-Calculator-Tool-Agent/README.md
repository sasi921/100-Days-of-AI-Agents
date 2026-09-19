# Day 009 — AI Calculator Tool Agent

**Difficulty:** 🟡 Intermediate Foundations  
**Focus:** tool contracts, tool selection, execution loops, observations, safe expression evaluation

Day 008 learned to route a request. Day 009 takes the next step: **choose a tool, execute it, observe the result, and answer from the tool output.**

## Agent loop

`User → Decide tool → Validate arguments → Execute tool → Observe result → Answer`

This intentionally uses a deterministic tool selector so the mechanics are visible before model-driven function calling is introduced.

## Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py "calculate 18 * (7 + 3)"
pytest -q
```

No API key is required.

## Safety detail

The calculator does **not** use Python `eval()`. It parses the expression with `ast` and allows only numeric constants and a small arithmetic operator allowlist.

## Example

```json
{
  "decision": {"tool": "calculator", "arguments": {"expression": "18 * (7 + 3)"}, "reason": "The request contains an arithmetic expression."},
  "observation": {"tool": "calculator", "input": "18 * (7 + 3)", "result": 180},
  "answer": "The result is 180."
}
```

## Study

Tool contracts, argument validation, dispatch, execution/observation loops, least privilege, deterministic tools, and why tool outputs should ground final answers.

## Extension challenge

Add unit-conversion and date tools, then build a registry that lets the agent select among all three.

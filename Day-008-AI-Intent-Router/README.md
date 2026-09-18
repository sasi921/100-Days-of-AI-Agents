# Day 008 — AI Intent Router

**Difficulty:** 🟡 Intermediate Foundations  
**Focus:** intent classification, confidence thresholds, routing, structured outputs, deterministic fallback

A practical agent primitive: turn one natural-language entry point into a reliable routing decision.

## Why this matters

Real assistants rarely have one capability. Before an agent can choose tools or workflows, it must decide **what the user is trying to do**. This project routes requests to `summarize`, `extract_tasks`, `answer_question`, `draft_reply`, or `unknown`.

The output includes an intent, confidence score, reason, handler name, and whether clarification is needed.

## Architecture

`User request → intent classifier → validated RouteDecision → confidence gate → handler`

With an API key, the router uses an LLM and validates its JSON with Pydantic. Without a key, deterministic regex rules make the demo fully runnable.

## Run

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py "Summarize this report into five bullets"
pytest -q
```

Optional: copy `.env.example`, set `OPENAI_API_KEY`, and export/load those variables in your shell.

Try:

```bash
python app.py "Extract action items from this meeting"
python app.py "How does RAG work?"
python app.py "Draft a reply confirming Friday"
python app.py "banana telescope purple"
```

## Example output

```json
{"intent":"summarize","confidence":0.82,"reason":"Matched a deterministic intent rule.","handler":"summary_handler","needs_clarification":false}
```

## Concepts to study

Study intent classification, dispatch tables, confidence thresholds, schema validation, deterministic fallbacks, and the difference between **routing** and **executing**. The router intentionally does not perform the downstream action yet; later days will connect routing decisions to real tools and workflows.

## Extension challenge

Add a `search_web` route, log routing accuracy on a labeled dataset, and tune the confidence threshold using measured false-route rates.

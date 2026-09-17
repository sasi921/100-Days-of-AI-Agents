# Day 007 — AI Prompt Guardrail & Safety Gateway 🛡️

**Difficulty:** 🟡 Intermediate Foundations  
**Topics:** guardrails, prompt injection, PII detection, moderation, deterministic policy, human review

Before an AI agent gets tools, memory, or permission to act, it needs a safety boundary. This project builds a small **guardrail gateway** that inspects untrusted input and returns a structured decision: `allow`, `review`, or `block`.

## Architecture

```text
User / external input
        ↓
Deterministic policy checks
        ↓
Optional provider moderation
        ↓
Structured decision
   allow | review | block
        ↓
Your future AI agent
```

The deterministic layer catches configured instruction-override patterns, credential-like content, and sensitive identifiers. When `OPENAI_API_KEY` is present, otherwise-safe text can also pass through provider moderation. The application falls back to local checks if that optional service is unavailable.

> This is an educational starter guardrail, not a complete security product. Production systems need context-aware policies, authorization, audit logs, red-team testing, and defense in depth.

## Files

- `app.py` — CLI gateway
- `guardrail.py` — policy engine + optional moderation
- `models.py` — validated output schema
- `tests/test_guardrail.py` — deterministic tests
- `examples/sample_input.txt` — sample input
- `.env.example` — optional provider configuration

## Run

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py "Summarize my meeting notes"
python app.py --file examples/sample_input.txt
pytest -q
```

An API key is optional. To enable provider moderation, copy `.env.example` and set `OPENAI_API_KEY` in your environment.

## Example decision

```json
{
  "decision": "allow",
  "categories": [],
  "confidence": 0.8,
  "reason": "No configured guardrail pattern matched.",
  "safe_response": null
}
```

## What to study

1. **Deterministic vs probabilistic controls** — security-critical rules should not rely only on an LLM.
2. **Prompt injection** — external text may contain instructions designed to override your application.
3. **PII boundaries** — sensitive data may need redaction or human review.
4. **Structured policy decisions** — downstream code should consume predictable states.
5. **Fail-safe design** — provider failures should not silently disable baseline controls.
6. **Human-in-the-loop** — uncertainty is often better routed to review than automatically allowed or blocked.

## Challenge

Add configurable policies from YAML, redact sensitive values before model calls, and write an audit event for every decision.

## Next step in the series

The remaining foundation projects will turn these reliable building blocks into simple workflows before the series moves into tool-calling agents.

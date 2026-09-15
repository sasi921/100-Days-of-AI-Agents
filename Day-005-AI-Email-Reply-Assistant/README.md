# Day 005 — AI Email Reply Assistant

**Difficulty:** 🟢 Beginner+  
**Focus:** System prompts, instruction hierarchy, tone control, prompt boundaries, safe fallbacks

Build an assistant that turns an incoming email plus your reply goal into a polished draft. The important lesson is not email itself — it is **how to separate trusted developer instructions from untrusted user-provided content**.

## What it teaches

```text
Incoming email (untrusted data)
          ↓
System prompt + boundaries
          ↓
Goal + tone controls
          ↓
LLM
          ↓
Draft reply
```

The project tells the model not to invent facts, commitments, dates, prices, or attachments. Missing details become `[NEEDS INPUT: ...]` placeholders instead.

## Features

- three tones: professional, friendly, concise
- explicit system/user message separation
- untrusted-email delimiters
- optional OpenAI generation
- deterministic no-key fallback
- tests for prompt construction, validation, and fallback behavior
- sample email and prompt ideas

## Setup

```bash
cd Day-005-AI-Email-Reply-Assistant
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Add `OPENAI_API_KEY` to `.env` for model-generated replies. Without a key, the project uses a deterministic fallback.

## Run

```bash
python app.py examples/sample_email.txt \
  --goal "Confirm receipt and say I need to verify the delivery date before committing" \
  --tone professional
```

## Tests

```bash
pytest -q
```

## Key ideas to study

1. **Instruction hierarchy** — stable behavior belongs in the system message; task context belongs in the user message.
2. **Data vs. instructions** — an email can contain malicious or irrelevant instructions, so the app labels it as untrusted data.
3. **Prompt constraints** — explicit non-invention rules reduce a common business-drafting failure mode.
4. **Tone as a parameter** — reusable prompts expose behavior as inputs instead of copy-pasted prompt variants.
5. **Graceful degradation** — the CLI remains demonstrable when the external model is unavailable.

## Challenge

Add a `--length short|medium|long` option, then test that the selected length reaches the model prompt.

---

⭐ Star the main **100 Days of AI Agents** repository and follow the progression from beginner bots to production agent systems.

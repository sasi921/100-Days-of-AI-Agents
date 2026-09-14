# Day 004 — AI Meeting Action Item Extractor 📝🤖

Turn messy meeting transcripts into **structured JSON** containing a summary, decisions, action items, owners, due dates, and open questions.

## Why this project?

Day 1 introduced prompting, Day 2 introduced API/tool data, and Day 3 introduced grounded web research. Day 4 focuses on another core production skill: **structured outputs you can reliably feed into other software**.

Instead of asking an LLM for free-form prose, this project validates the result against a Pydantic schema.

## Architecture

```text
Transcript
   ↓
Prompt + JSON schema
   ↓
LLM (optional)
   ↓
JSON parsing
   ↓
Pydantic validation
   ↓
Structured meeting record
```

If `OPENAI_API_KEY` is not set, the app still runs using a deterministic local fallback extractor so learners can test the workflow without API cost.

## Features

- CLI that accepts a meeting transcript file
- Optional OpenAI-powered extraction
- Deterministic no-key fallback
- Pydantic schema validation
- JSON output suitable for APIs, databases, Slack bots, or task systems
- Unit tests
- Sample meeting transcript

## Project structure

```text
Day-004-AI-Meeting-Action-Item-Extractor/
├── README.md
├── SOCIAL_POST.md
├── app.py
├── agent.py
├── models.py
├── requirements.txt
├── .env.example
├── examples/
│   └── sample_meeting.txt
└── tests/
    └── test_agent.py
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env           # Windows: copy .env.example .env
```

Add your OpenAI API key to `.env` if you want LLM extraction. It is optional.

## Run

```bash
python app.py examples/sample_meeting.txt
```

Save the structured result to a file:

```bash
python app.py examples/sample_meeting.txt --output meeting.json
```

Example output shape:

```json
{
  "summary": "...",
  "decisions": ["..."],
  "action_items": [
    {
      "task": "prepare the launch checklist",
      "owner": "Maya",
      "due_date": "Thursday"
    }
  ],
  "open_questions": ["Should we invite the design team to the launch review?"]
}
```

## Test

```bash
pytest -q
```

## What to study today

1. **Structured outputs** — why machine-readable JSON is more useful than prose for automation.
2. **Schemas** — how Pydantic defines and validates the contract between an LLM and your app.
3. **Validation** — never trust model output until it is parsed and checked.
4. **Fallbacks** — production systems should degrade gracefully when a model or API is unavailable.
5. **Separation of concerns** — CLI, extraction logic, and data models live in separate files.

## Extension challenge

Add one of these:

- export action items to CSV
- create calendar-ready due dates
- add a confidence score per action item
- accept pasted text in addition to files
- build a Streamlit UI

## Progression

Day 004 stays in the **foundations** stage, but it creates a building block we will reuse later in workflow agents, memory systems, tool calling, and multi-agent pipelines.

---

⭐ Star the main repository to follow all 100 builds.

# Day 003/100 — AI Web Research Agent 🔎🤖

**Difficulty:** 🟢 Beginner+  
**Focus:** webpage tools, grounding, extraction, question answering, safe fallbacks

Day 1 taught structured LLM output. Day 2 connected an agent to a live API. **Day 3 teaches an agent to gather evidence from a webpage before reasoning.**

Give it a public URL and, optionally, a question. The agent fetches the page, removes navigation/scripts, extracts readable text, and creates a grounded research briefing.

## Architecture

```text
URL + optional question
        │
        ▼
URL safety validation
        │
        ▼
HTTP fetch tool
        │
        ▼
HTML → readable text
        │
        ▼
Grounded reasoning
   ┌────┴────┐
   │         │
OpenAI   Extractive fallback
   │         │
   └────┬────┘
        ▼
Markdown research briefing
```

## What you will learn

- how agents use webpages as tools instead of relying only on model memory
- basic HTTP fetching with timeouts and size limits
- HTML parsing and content cleaning with Beautiful Soup
- grounding prompts in retrieved evidence
- safe handling of local/private URLs
- deterministic fallbacks when an LLM key is unavailable
- testing parsing and agent logic without hitting the network

## Project structure

```text
Day-003-AI-Web-Research-Agent/
├── app.py
├── agent.py
├── web_tool.py
├── requirements.txt
├── .env.example
├── README.md
├── SOCIAL_POST.md
├── examples/
│   └── sample_article.html
└── tests/
    ├── conftest.py
    ├── test_agent.py
    └── test_web_tool.py
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env            # Windows: copy .env.example .env
```

Adding an OpenAI API key is optional. Without one, the app still runs using a deterministic extractive summarizer.

## Run it

Summarize a webpage:

```bash
python app.py "https://example.com/article"
```

Ask a grounded question:

```bash
python app.py "https://example.com/article" --question "What are the three main recommendations?"
```

The LLM is instructed to use **only** the fetched page. If the page does not support an answer, it should say so.

## Run the tests

```bash
pytest -q
```

The tests are intentionally offline: they validate HTML cleaning, URL safety, and fallback summarization without spending API credits or depending on a website being online.

## Important limitations

This is an educational beginner agent, not a full crawler. It does not execute JavaScript, bypass paywalls, scrape login-protected pages, or crawl multiple links. Some sites may block automated requests.

## Extension challenge ⭐

Turn this single-page researcher into a **multi-source research agent**:

1. accept 3–5 URLs,
2. extract each source independently,
3. ask the model to compare claims,
4. preserve source attribution per claim,
5. flag disagreements between sources.

That naturally leads toward retrieval and RAG patterns later in the series.

## Key idea

A useful agent should not simply "know things." It should be able to **collect evidence, reason over it, and show where the answer came from.**

---

⭐ If this project helps you learn, star the main **100 Days of AI Agents** repository and build the extension challenge.

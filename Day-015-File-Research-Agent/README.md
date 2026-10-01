# Day 015 — File Research Agent

**Difficulty:** 🟡 Intermediate  
**Focus:** retrieval, evidence grounding, file tools, citations, hallucination resistance

Day 014 gave the agent a guarded database tool. Day 015 introduces the core pattern that later becomes RAG: **retrieve evidence before answering**.

## Architecture

`Question → file search tool → ranked evidence → grounded answer → source:line citations`

This project searches a local text file, returns the most relevant lines, and answers only from those observations. It runs without an API key; adding `OPENAI_API_KEY` enables model-generated synthesis constrained to retrieved evidence.

## Run

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python app.py examples/company_notes.txt "What action requires human approval?"
pytest -q
```

## Why this matters

Agents should not answer document questions from model memory when the source of truth is available. Retrieval creates an explicit evidence boundary and gives users something they can verify.

## Study

Retrieval before generation, tool observations, evidence ranking, grounding, source-line citations, insufficient-evidence behavior, and the difference between keyword retrieval and embedding-based semantic retrieval.

## Extension challenge

Replace lexical matching with embeddings and compare retrieval quality on paraphrased questions. That is the bridge into the upcoming RAG phase.

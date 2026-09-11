# Day 001 — AI Resume Analyzer Agent 🧠📄

**Difficulty:** 🟢 Beginner  
**Build:** A command-line AI agent that compares a resume with a job description and returns a match score, strengths, gaps, improvements, and interview questions.

## What you will learn

- how to call an LLM from Python
- how to separate system instructions from user input
- how to ask a model for machine-readable JSON
- how to validate model output before using it
- how to keep API keys out of Git
- how to turn an AI idea into a small reusable CLI tool

## Architecture

```text
Resume.txt ─┐
            ├─> Prompt Builder ─> OpenAI Responses API ─> JSON Validator ─> Report
Job.txt ────┘
```

## Project structure

```text
Day-001-AI-Resume-Analyzer/
├── app.py
├── analyzer.py
├── prompts.py
├── requirements.txt
├── .env.example
├── examples/
│   ├── resume.txt
│   └── job_description.txt
└── tests/
    └── test_analyzer.py
```

## Setup

### 1. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**macOS/Linux**

```bash
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add your API key

Copy the example environment file:

```bash
cp .env.example .env
```

On Windows Command Prompt:

```bat
copy .env.example .env
```

Then edit `.env`:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5.6-luna
```

Never commit your `.env` file.

## Run it

From inside this folder:

```bash
python app.py --resume examples/resume.txt --job examples/job_description.txt
```

To get raw JSON:

```bash
python app.py --resume examples/resume.txt --job examples/job_description.txt --json
```

## Example output

```text
=== AI Resume Analyzer ===
Match score: 82/100

Matched skills:
- Python
- REST APIs
- SQL
- Docker

Missing skills:
- Kubernetes
```

Exact results vary because model outputs can vary.

## Run tests

```bash
pytest -q
```

The tests do not call the API. They verify JSON parsing and result validation.

## How it works

1. `app.py` reads the two text files and handles the CLI.
2. `prompts.py` defines the agent instructions and analysis prompt.
3. `analyzer.py` sends the request to the model.
4. The model is instructed to return JSON only.
5. The program parses and validates the JSON before displaying it.

## Beginner challenge

Add a `--save report.json` option that saves the analysis to a file.

## Advanced challenge

Add PDF/DOCX extraction and a small Streamlit interface so users can upload files instead of converting them to text first.

## Why this repo is worth starring

This project is intentionally small enough to understand in one sitting but uses patterns that carry into larger agents: instruction design, model calls, structured data, validation, secrets management, testing, and clean project organization.

---

**Next:** Day 002 will add another building block and continue toward full agentic systems.

⭐ Star the main repo to follow all 100 days.

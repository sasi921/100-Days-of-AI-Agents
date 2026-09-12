# Day 002 — AI Weather Briefing Agent 🌦️🤖

**Difficulty:** 🟢 Beginner+  
**Focus:** External APIs, tool-style data flow, graceful AI fallback

Day 1 taught us how to send structured text to an LLM. Day 2 adds a new idea: **an agent can gather fresh information from an external tool before it answers.**

This project takes a city name, resolves it to coordinates, fetches a 3-day forecast from Open-Meteo, normalizes the result, and then turns the data into a concise weather briefing. If `OPENAI_API_KEY` is available, the LLM writes the briefing. If not, the project still works with a deterministic fallback.

## What it does

```text
User city
   ↓
Geocoding API
   ↓
Latitude + longitude
   ↓
Weather Forecast API
   ↓
Normalized tool data
   ↓
AI Weather Briefing Agent
   ↓
Readable weather advice
```

## What you'll learn

- Calling a real external REST API with `requests`
- Separating **tool/data code** from **agent/reasoning code**
- Normalizing third-party API responses
- Passing trusted tool data to an LLM
- Designing a graceful fallback when an AI service is unavailable
- Testing transformation logic without making live API calls

## Project files

```text
Day-002-AI-Weather-Briefing-Agent/
├── README.md
├── app.py
├── agent.py
├── weather_api.py
├── requirements.txt
├── .env.example
├── examples/
│   └── sample_weather.json
└── tests/
    ├── conftest.py
    ├── test_agent.py
    └── test_weather_api.py
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Adding an OpenAI key is optional:

```env
OPENAI_API_KEY=your_key_here
```

## Run it

```bash
python app.py "Austin"
```

Use Fahrenheit/mph:

```bash
python app.py "Austin" --fahrenheit
```

See the normalized API/tool payload too:

```bash
python app.py "Hyderabad" --json
```

## Example output

```text
=== AI Weather Briefing ===
Weather briefing for Austin, United States: currently 88°F and mainly clear, feels like 91°F. Today's high is 94°F with a low of 73°F. Peak precipitation chance is 10%. Maximum wind is around 16 mph.
```

With an OpenAI key configured, the briefing becomes a more natural 4–6 sentence summary with practical advice and a short outlook.

## Run the tests

```bash
pytest -q
```

The tests use sample dictionaries instead of live HTTP requests, so they remain fast and repeatable.

## Why this is an "agent" step

The important progression is not just "call an LLM." The application first **uses an external information source**, converts that source into predictable tool data, and only then lets the model reason over it. This tool → data → reasoning pattern is the foundation of more advanced agents we'll build later.

## Extension challenges

1. Add severe-weather thresholds and warnings.
2. Let users compare two cities.
3. Add an hourly forecast tool.
4. Cache API results for 10 minutes.
5. Replace the manual weather call with formal LLM function/tool calling in a future version.

## Privacy & reliability notes

- The weather APIs used here require no API key.
- Never commit `.env` or real secret keys.
- The LLM is instructed to use only provided weather data.
- The deterministic fallback ensures the CLI still works if the AI service is unavailable.

---

⭐ If this helped you learn how agents use external tools, star the main **100 Days of AI Agents** repository and follow Day 003.

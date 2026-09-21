# Day 011 — Live Weather Tool Agent

**Difficulty:** 🟡 Intermediate  
**Focus:** external API tools, geocoding, live observations, normalization, timeouts, grounded responses

Welcome to the **Tool-Using Agents** phase. Day 010 taught a local multi-tool registry; Day 011 crosses the network boundary and lets an agent retrieve real-world data from a public API.

## Agent flow

`City → Geocoding tool → coordinates → Weather API → normalized observation → grounded briefing`

The project uses Open-Meteo, so no API key is required.

## Run

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py "Austin"
pytest -q
```

Because weather changes, values are never hard-coded.

## What makes this an agent building block?

The network response is treated as an **observation**, normalized into a Pydantic model, then converted into an answer. Tool errors remain errors rather than being replaced by invented weather.

## Study

External API contracts, geocoding, URL encoding, timeouts, normalization, tool observations, grounding, deterministic business rules, and failure handling.

## Extension challenge

Add forecast support and a second provider adapter, then compare both providers before producing a final briefing.

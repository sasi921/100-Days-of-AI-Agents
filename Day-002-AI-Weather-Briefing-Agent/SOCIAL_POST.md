# Day 002/100 — AI Weather Briefing Agent 🌦️🤖

Day 2 of **100 Days of AI Agents** is live.

Today we built an AI agent that does more than answer from a prompt: it first calls real external APIs, turns the response into clean tool data, and then creates a useful weather briefing.

What it learns to do:
- resolve a city to coordinates
- fetch a live 3-day forecast
- normalize third-party API data
- pass trusted tool data to an LLM
- fall back gracefully if the AI service is unavailable

This introduces one of the most important agent patterns:

**Tool → Data → Reasoning → Answer**

The full runnable code, tests, sample data, and setup guide are on GitHub.

⭐ Star the repo and follow the series if you want to learn AI engineering by building one project at a time.

#AIAgents #GenerativeAI #Python #OpenAI #APIs #100DaysOfAI #BuildInPublic

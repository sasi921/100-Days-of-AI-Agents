# Day 016 — GitHub Repository Insight Agent

**Difficulty:** 🟡 Intermediate  
**Focus:** multi-tool API orchestration, API authentication, structured observations, repository health signals

Day 015 introduced evidence retrieval from local files. Day 016 expands the tool-using phase with a practical agent that coordinates **multiple GitHub API calls** and turns them into one structured repository insight report.

## Architecture

`owner/repo → metadata API → languages API → issues API → normalized snapshot → health analysis`

The agent inspects a public GitHub repository and returns:

- stars, forks, watchers, and open-issue count
- default branch and archived status
- language breakdown
- recent open issue titles
- a simple deterministic health score
- strengths and watch items

Public repositories work without a token. Adding `GITHUB_TOKEN` raises API rate limits.

## Run

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

python app.py openai/openai-python
pytest -q
```

## Study

Multi-tool orchestration, REST APIs, optional authentication, timeouts, error handling, Pydantic models, deterministic scoring, and why external API responses should be normalized before downstream reasoning.

## Extension challenge

Add a pull-request endpoint and compute a richer activity score using recently merged PRs and commit recency.

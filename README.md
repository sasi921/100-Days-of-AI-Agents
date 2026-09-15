<p align="center">
  <img src="assets/hero.svg" alt="100 Days of AI Agents — 100 practical projects from beginner to production" width="100%" />
</p>

<p align="center">
  <a href="https://github.com/sasi921/100-Days-of-AI-Agents/stargazers"><img src="https://img.shields.io/github/stars/sasi921/100-Days-of-AI-Agents?style=for-the-badge&logo=github&label=Stars" alt="GitHub stars" /></a>
  <a href="https://github.com/sasi921/100-Days-of-AI-Agents/network/members"><img src="https://img.shields.io/github/forks/sasi921/100-Days-of-AI-Agents?style=for-the-badge&logo=github&label=Forks" alt="GitHub forks" /></a>
  <img src="https://img.shields.io/badge/Progress-4%2F100-1f6feb?style=for-the-badge" alt="Progress 4/100" />
  <img src="https://img.shields.io/badge/Python-AI%20Engineering-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python AI Engineering" />
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/Contributions-Welcome-2ea44f?style=for-the-badge" alt="Contributions welcome" /></a>
</p>

<h3 align="center">Learn AI engineering by building — one useful project every day.</h3>

<p align="center">
  <b>Prompting → APIs → Tools → RAG → Memory → Planning → MCP → Multi-Agent Systems → Evaluation → Production</b>
</p>

<p align="center">
  ⭐ <b>If this learning path is useful, star the repository so you can follow all 100 builds.</b>
</p>

---

## 🚀 What is this?

**100 Days of AI Agents** is a progressive, hands-on learning series built around one idea:

> The fastest way to understand modern AI engineering is to build real systems, not only watch tutorials.

Every day adds a **runnable project** with complete source code, setup instructions, examples, tests or smoke checks, concepts to study, and ideas for extending the build.

This repository starts with beginner-friendly LLM applications and gradually moves toward production-grade agent systems.

### Why follow this repo?

- ✅ **Real projects** instead of isolated code snippets
- ✅ **Progressive difficulty** from beginner to production
- ✅ **Complete source code** you can clone and modify
- ✅ **Tests / smoke checks** so examples are reproducible
- ✅ **Practical architecture patterns** used in real AI applications
- ✅ **No secrets committed** — environment variables and `.env.example` files are used when needed
- ✅ **Beginner explanations + extension challenges** for deeper learning

---

## 🔥 Latest build

### Day 004 — AI Meeting Action Item Extractor

Turn an unstructured meeting transcript into validated, machine-readable data:

**Transcript → Prompt + Schema → JSON → Pydantic Validation → Reliable Data**

It extracts summaries, decisions, action items, owners, due dates, and open questions.

➡️ **[Explore Day 004](Day-004-AI-Meeting-Action-Item-Extractor/)**

---

## ⚡ Start here in 60 seconds

Clone the full learning series:

```bash
git clone https://github.com/sasi921/100-Days-of-AI-Agents.git
cd 100-Days-of-AI-Agents
```

Start with Day 001:

```bash
cd Day-001-AI-Resume-Analyzer
python -m venv .venv
```

Activate the environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Then follow that project's `README.md` for dependencies and the run command.

> New to AI agents? Start at Day 001 and move in order. Each project introduces concepts that later builds reuse.

---

## 📚 Project index

| Day | Project | Difficulty | What you learn |
|---:|---|---|---|
| 001 | **[AI Resume Analyzer](Day-001-AI-Resume-Analyzer/)** | 🟢 Beginner | LLM API, prompt design, JSON parsing, CLI apps |
| 002 | **[AI Weather Briefing Agent](Day-002-AI-Weather-Briefing-Agent/)** | 🟢 Beginner+ | External APIs, tool data, normalization, graceful fallback |
| 003 | **[AI Web Research Agent](Day-003-AI-Web-Research-Agent/)** | 🟢 Beginner+ | Web tools, HTML extraction, grounding, source-aware Q&A |
| 004 | **[AI Meeting Action Item Extractor](Day-004-AI-Meeting-Action-Item-Extractor/)** | 🟢 Beginner+ | Structured outputs, Pydantic schemas, validation, graceful fallback |

### Current progress

**4 / 100 projects complete** — Foundations phase in progress.

`████░░░░░░░░░░░░░░░░` **4%**

---

## 🧠 The learning path

### Days 1–10 — Foundations
Prompt engineering, structured outputs, CLI/web interfaces, API basics, validation, and dependable AI application patterns.

### Days 11–25 — Tool-using agents
Function/tool calling, search, external APIs, databases, workflows, and agents that can take useful actions.

### Days 26–45 — RAG
Embeddings, chunking, retrieval, vector databases, document assistants, citation patterns, and retrieval evaluation.

### Days 46–65 — Agent systems
Memory, state, planning, approvals, orchestration, durable workflows, and long-running tasks.

### Days 66–80 — Multi-agent systems
Specialized agents, delegation, coordination, reviewer/critic patterns, and shared state.

### Days 81–90 — MCP & integrations
MCP servers and clients plus integrations with GitHub, email, calendars, databases, and enterprise tools.

### Days 91–100 — Production AI
Evaluation, observability, guardrails, Docker, deployment, reliability, cost control, security, and scaling.

---

## 🧩 How each day is designed

A daily project aims to contain:

```text
Day-XXX-Project-Name/
├── README.md              # what it does + how to learn from it
├── app/source files       # runnable implementation
├── requirements.txt       # dependencies
├── .env.example           # safe configuration template when needed
├── examples/              # sample inputs / prompts
├── tests/                 # tests or smoke checks
└── SOCIAL_POST.md         # shareable build-in-public update
```

The goal is not to create 100 disconnected demos. The projects deliberately build toward increasingly capable agent systems.

---

## 🛠️ Build with us

Have an idea for a future agent? Found a bug? Want to improve an explanation?

Contributions are welcome.

1. Read **[CONTRIBUTING.md](CONTRIBUTING.md)**.
2. Open an issue with a project idea or improvement.
3. Fork the repo and submit a focused pull request.

Good contributions include better tests, additional providers/models, improved prompts, clearer docs, reliability fixes, evaluation examples, and useful project ideas.

---

## 🎯 Who this is for

This series is for:

- students learning AI engineering
- software engineers moving into AI
- data / ML engineers learning agentic systems
- career switchers building a public portfolio
- developers who learn best by building
- anyone curious about how AI agents progress from demos to production systems

You do **not** need to understand every advanced concept before starting. Begin with Day 001 and learn as the architecture evolves.

---

## 🌟 Help this project grow

Open-source learning projects grow through people sharing them.

If you find something useful here:

- ⭐ **Star** the repository
- 🍴 **Fork** it and experiment
- 🧑‍💻 **Build** one of the projects yourself
- 💡 **Open an issue** with a future agent idea
- 🔁 **Share** a project with someone learning AI
- 🤝 **Contribute** an improvement

<p align="center">
  <b>100 projects. One progressive path. Learn AI agents by building them.</b>
</p>

<p align="center">
  ⭐ <a href="https://github.com/sasi921/100-Days-of-AI-Agents">Star 100 Days of AI Agents</a> •
  🍴 <a href="https://github.com/sasi921/100-Days-of-AI-Agents/fork">Fork the repo</a> •
  💡 <a href="https://github.com/sasi921/100-Days-of-AI-Agents/issues">Suggest an idea</a>
</p>

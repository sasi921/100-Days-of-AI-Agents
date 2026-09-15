# Contributing to 100 Days of AI Agents

Thanks for helping make this series more useful for people learning AI engineering.

## Ways to contribute

You can help by:

- fixing bugs or broken setup steps
- improving explanations or examples
- adding tests
- suggesting a future daily project
- improving prompts, evaluation, or reliability
- adding support for another model/provider
- improving accessibility or developer experience

## Contribution principles

Each daily project should stay:

1. **Runnable** — a learner should be able to clone it and run it.
2. **Focused** — one main concept per day whenever possible.
3. **Practical** — prefer a real use case over a toy demo.
4. **Learnable** — explain why the architecture works, not only what to copy.
5. **Safe by default** — never commit secrets, tokens, or personal data.
6. **Testable** — include tests or at least a reproducible smoke check.

## Suggest a project

Open an issue with:

- project title
- problem it solves
- difficulty level
- concepts learners will practice
- suggested tech stack
- what makes it useful or shareable

## Submit a pull request

1. Fork the repository.
2. Create a focused branch.
3. Make your change.
4. Run the relevant tests.
5. Keep secrets out of commits.
6. Open a pull request explaining what changed and why.

For a new daily project, include at minimum:

```text
Day-XXX-Project-Name/
├── README.md
├── app/source files
├── requirements.txt or equivalent
├── .env.example when needed
├── examples/
└── tests/ or a smoke test
```

## Style

- Prefer clear code over clever code.
- Keep setup instructions copy-paste friendly.
- Use environment variables for secrets.
- Explain important tradeoffs in the README.
- Avoid unnecessary dependencies.

## Community goal

The goal is not to race through 100 folders. The goal is to build a public learning path that someone can follow from their first LLM app to production-grade agent systems.

If you improve something, thank you — you are helping the next learner move faster.
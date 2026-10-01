import os
from models import ResearchResult
from tools import search_lines

def research(path: str, question: str) -> ResearchResult:
    evidence = search_lines(path, question)
    if not evidence:
        return ResearchResult(
            question=question,
            answer="I could not find supporting evidence in the file.",
            evidence=[],
        )

    context = "\n".join(f"{e.source}:{e.line}: {e.text}" for e in evidence)

    if os.getenv("OPENAI_API_KEY"):
        from openai import OpenAI

        client = OpenAI()
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            input=[
                {
                    "role": "system",
                    "content": (
                        "Answer only from supplied evidence. "
                        "If evidence is insufficient, say so. Cite source:line."
                    ),
                },
                {
                    "role": "user",
                    "content": f"Question: {question}\nEvidence:\n{context}",
                },
            ],
        )
        answer = response.output_text
    else:
        answer = "Relevant evidence: " + " | ".join(
            f"{e.source}:{e.line} — {e.text}" for e in evidence
        )

    return ResearchResult(question=question, answer=answer, evidence=evidence)

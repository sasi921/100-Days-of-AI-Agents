from __future__ import annotations

import os
import re
from collections import Counter

from dotenv import load_dotenv

load_dotenv()

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "if", "then", "than", "to", "of", "in", "on", "for",
    "with", "as", "at", "by", "from", "is", "are", "was", "were", "be", "been", "being", "it", "its",
    "this", "that", "these", "those", "you", "your", "we", "our", "they", "their", "he", "she", "i",
    "not", "can", "could", "will", "would", "should", "may", "might", "about", "into", "over", "after",
}


def _sentences(text: str) -> list[str]:
    cleaned = re.sub(r"\s+", " ", text).strip()
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", cleaned) if len(s.strip()) >= 35]


def extractive_summary(text: str, max_sentences: int = 5) -> str:
    sentences = _sentences(text)
    if not sentences:
        return text[:900].strip()

    words = re.findall(r"[A-Za-z][A-Za-z'-]{2,}", text.lower())
    frequencies = Counter(word for word in words if word not in STOPWORDS)
    if not frequencies:
        return " ".join(sentences[:max_sentences])

    scored: list[tuple[float, int, str]] = []
    for index, sentence in enumerate(sentences):
        sentence_words = re.findall(r"[A-Za-z][A-Za-z'-]{2,}", sentence.lower())
        if not sentence_words:
            continue
        score = sum(frequencies[word] for word in sentence_words if word in frequencies) / len(sentence_words)
        scored.append((score, index, sentence))

    top = sorted(scored, reverse=True)[:max_sentences]
    return " ".join(item[2] for item in sorted(top, key=lambda item: item[1]))


def research_page(title: str, url: str, text: str, question: str | None = None) -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        summary = extractive_summary(text)
        question_note = f"\n\n**Question:** {question}\n**Answer:** Add `OPENAI_API_KEY` for question-aware reasoning." if question else ""
        return (
            f"# {title}\n\n"
            f"**Source:** {url}\n\n"
            f"## Extractive briefing\n{summary}"
            f"{question_note}\n\n"
            "_Deterministic fallback used because no OpenAI API key was configured._"
        )

    from openai import OpenAI

    client = OpenAI(api_key=api_key)
    model = os.getenv("OPENAI_MODEL", "gpt-5-mini")
    clipped_text = text[:24000]
    user_question = question or "What are the most important ideas on this page?"

    prompt = f"""You are a careful web research assistant. Use ONLY the supplied webpage text.
Do not invent facts. If the answer is not supported by the page, say so.

PAGE TITLE: {title}
SOURCE URL: {url}
QUESTION: {user_question}

WEBPAGE TEXT:
{clipped_text}

Return concise Markdown with these headings:
## Answer
## Key points
## Evidence from the page
## Caveats

In 'Evidence from the page', paraphrase the supporting passages rather than fabricating quotations.
End with: Source: {url}
"""

    response = client.responses.create(model=model, input=prompt)
    return response.output_text.strip()

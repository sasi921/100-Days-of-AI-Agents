from __future__ import annotations

import json
import os
import re
from typing import Iterable

from dotenv import load_dotenv
from models import ActionItem, MeetingSummary

load_dotenv()


def _sentences(text: str) -> list[str]:
    chunks = re.split(r"(?<=[.!?])\s+|\n+", text.strip())
    return [c.strip(" -\t") for c in chunks if c.strip()]


def fallback_extract(transcript: str) -> MeetingSummary:
    sentences = _sentences(transcript)
    if not sentences:
        raise ValueError("Transcript is empty.")

    decisions: list[str] = []
    actions: list[ActionItem] = []
    questions: list[str] = []

    decision_words = ("decided", "agreed", "approved", "will use", "we'll use", "selected")
    action_patterns: Iterable[re.Pattern[str]] = (
        re.compile(r"^(?P<owner>[A-Z][a-z]+)\s+(?:will|to|should)\s+(?P<task>.+?)(?:\s+by\s+(?P<due>[^.]+))?$", re.I),
        re.compile(r"^(?:action item:\s*)?(?P<task>.+?)(?:\s+owner:\s*(?P<owner>[^,]+))?(?:,?\s*due:\s*(?P<due>[^.]+))?$", re.I),
    )

    for s in sentences:
        lower = s.lower()
        if s.endswith("?"):
            questions.append(s)
        if any(word in lower for word in decision_words):
            decisions.append(s)
        if (" will " in lower) or (" should " in lower) or lower.startswith("action item"):
            for pattern in action_patterns:
                match = pattern.match(s)
                if match:
                    task = (match.groupdict().get("task") or "").strip()
                    owner = (match.groupdict().get("owner") or "").strip() or None
                    due = (match.groupdict().get("due") or "").strip() or None
                    if len(task) >= 4:
                        actions.append(ActionItem(task=task.rstrip("."), owner=owner, due_date=due))
                        break

    summary = " ".join(sentences[:2])
    return MeetingSummary(
        summary=summary,
        decisions=list(dict.fromkeys(decisions)),
        action_items=actions,
        open_questions=list(dict.fromkeys(questions)),
    )


def llm_extract(transcript: str, model: str = "gpt-4.1-mini") -> MeetingSummary:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return fallback_extract(transcript)

    from openai import OpenAI

    client = OpenAI(api_key=api_key)
    schema = MeetingSummary.model_json_schema()
    prompt = f"""Extract a concise meeting summary from the transcript below.
Return ONLY valid JSON matching this schema exactly:
{json.dumps(schema, indent=2)}

Rules:
- Do not invent owners or dates.
- Keep action items concrete and short.
- Put unresolved questions in open_questions.
- If a field has no items, return an empty list.

Transcript:
{transcript}
"""
    response = client.responses.create(model=model, input=prompt)
    data = json.loads(response.output_text)
    return MeetingSummary.model_validate(data)

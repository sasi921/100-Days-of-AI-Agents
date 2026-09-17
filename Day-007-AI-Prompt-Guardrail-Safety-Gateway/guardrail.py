import os
import re

from models import ModerationResult

BLOCK = {
    "credentials": [r"password\s*[:=]", r"api[_ -]?key\s*[:=]", r"secret\s*[:=]"],
    "prompt_injection": [
        r"ignore (all |the )?(previous|prior) instructions",
        r"reveal (the )?(system|developer) prompt",
    ],
}
REVIEW = {
    "pii": [r"\b\d{3}-\d{2}-\d{4}\b", r"\b(?:\d[ -]*?){13,16}\b"],
}


def deterministic_check(text: str) -> ModerationResult:
    categories = []
    for category, patterns in BLOCK.items():
        if any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns):
            categories.append(category)
    if categories:
        return ModerationResult(
            decision="block",
            categories=categories,
            confidence=0.95,
            reason="Potential secret exposure or prompt-injection attempt detected.",
            safe_response=(
                "I can help with the legitimate task, but I won't expose credentials "
                "or hidden instructions."
            ),
        )

    for category, patterns in REVIEW.items():
        if any(re.search(pattern, text, re.IGNORECASE) for pattern in patterns):
            categories.append(category)
    if categories:
        return ModerationResult(
            decision="review",
            categories=categories,
            confidence=0.85,
            reason="Potential sensitive personal data detected; human review recommended.",
        )

    return ModerationResult(
        decision="allow",
        confidence=0.80,
        reason="No configured guardrail pattern matched.",
    )


def check(text: str) -> ModerationResult:
    # Keep a predictable, testable baseline instead of depending entirely on an LLM.
    base = deterministic_check(text)
    if base.decision != "allow" or not os.getenv("OPENAI_API_KEY"):
        return base

    try:
        from openai import OpenAI

        client = OpenAI()
        response = client.moderations.create(
            model=os.getenv("MODERATION_MODEL", "omni-moderation-latest"), input=text
        )
        result = response.results[0]
        flagged = [
            key for key, value in result.categories.model_dump().items() if value
        ]
        if result.flagged:
            return ModerationResult(
                decision="review",
                categories=flagged,
                confidence=0.90,
                reason="Provider moderation flagged this input for review.",
            )
    except Exception:
        # Local policy remains available if optional provider moderation fails.
        pass

    return base

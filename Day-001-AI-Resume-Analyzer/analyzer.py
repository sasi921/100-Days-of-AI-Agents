import json
import os
import re
from typing import Any

from prompts import SYSTEM_INSTRUCTIONS, build_analysis_prompt


REQUIRED_KEYS = {
    "match_score",
    "summary",
    "matched_skills",
    "missing_skills",
    "resume_improvements",
    "interview_questions",
}


class ResumeAnalyzer:
    def __init__(self, model: str | None = None) -> None:
        self.model = model or os.getenv("OPENAI_MODEL", "gpt-5.6-luna")
        self.client = None

    def analyze(self, resume_text: str, job_description: str) -> dict[str, Any]:
        if not resume_text.strip():
            raise ValueError("Resume text cannot be empty.")
        if not job_description.strip():
            raise ValueError("Job description cannot be empty.")

        if self.client is None:
            from openai import OpenAI

            self.client = OpenAI()

        response = self.client.responses.create(
            model=self.model,
            instructions=SYSTEM_INSTRUCTIONS,
            input=build_analysis_prompt(resume_text, job_description),
        )

        result = parse_model_json(response.output_text)
        return validate_result(result)


def parse_model_json(raw_text: str) -> dict[str, Any]:
    """Parse JSON even if the model accidentally wraps it in a code fence."""
    text = raw_text.strip()

    fenced = re.fullmatch(r"```(?:json)?\s*(.*?)\s*```", text, flags=re.DOTALL)
    if fenced:
        text = fenced.group(1).strip()

    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Model returned invalid JSON: {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError("Model response must be a JSON object.")

    return data


def validate_result(data: dict[str, Any]) -> dict[str, Any]:
    missing = REQUIRED_KEYS - data.keys()
    if missing:
        raise ValueError(f"Model response is missing keys: {sorted(missing)}")

    try:
        score = int(data["match_score"])
    except (TypeError, ValueError) as exc:
        raise ValueError("match_score must be an integer.") from exc

    data["match_score"] = max(0, min(100, score))

    for key in (
        "matched_skills",
        "missing_skills",
        "resume_improvements",
        "interview_questions",
    ):
        if not isinstance(data[key], list):
            raise ValueError(f"{key} must be a list.")

    if not isinstance(data["summary"], str):
        raise ValueError("summary must be a string.")

    return data

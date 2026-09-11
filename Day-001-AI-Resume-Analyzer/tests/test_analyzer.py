import json

import pytest

from analyzer import parse_model_json, validate_result


def valid_payload():
    return {
        "match_score": 84,
        "summary": "Strong overall fit.",
        "matched_skills": ["Python", "SQL"],
        "missing_skills": ["Kubernetes"],
        "resume_improvements": ["Quantify API performance improvements."],
        "interview_questions": ["How have you optimized a slow API?"],
    }


def test_parses_plain_json():
    payload = valid_payload()
    parsed = parse_model_json(json.dumps(payload))
    assert parsed["match_score"] == 84


def test_parses_fenced_json():
    payload = valid_payload()
    raw = "```json\n" + json.dumps(payload) + "\n```"
    parsed = parse_model_json(raw)
    assert parsed["matched_skills"] == ["Python", "SQL"]


def test_clamps_score_to_100():
    payload = valid_payload()
    payload["match_score"] = 120
    validated = validate_result(payload)
    assert validated["match_score"] == 100


def test_missing_key_fails():
    payload = valid_payload()
    del payload["summary"]
    with pytest.raises(ValueError):
        validate_result(payload)

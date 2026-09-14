import pytest

from agent import fallback_extract


def test_fallback_extracts_fields():
    transcript = "Team agreed to launch Friday. Maya will prepare checklist by Thursday. What remains open?"
    result = fallback_extract(transcript)
    assert result.decisions
    assert result.action_items[0].owner == "Maya"
    assert "prepare checklist" in result.action_items[0].task.lower()
    assert result.open_questions == ["What remains open?"]


def test_empty_transcript_rejected():
    with pytest.raises(ValueError):
        fallback_extract("   ")

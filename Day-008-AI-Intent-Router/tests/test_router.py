import pytest
from router import fallback_route, route

@pytest.mark.parametrize("text,intent",[("Summarize this report","summarize"),("Extract action items from this meeting","extract_tasks"),("Draft an email reply to Alex","draft_reply"),("How does RAG work?","answer_question")])
def test_known_routes(text,intent):
    assert fallback_route(text).intent == intent

def test_unknown_requests_clarification():
    d=fallback_route("banana telescope purple")
    assert d.intent == "unknown"
    assert d.needs_clarification is True

def test_empty_input(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY",raising=False)
    with pytest.raises(ValueError): route("   ")

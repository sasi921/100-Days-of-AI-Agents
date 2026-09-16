import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from agent import triage_ticket

def test_billing_fallback(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    r=triage_ticket("I was charged twice. Please refund the duplicate charge.")
    assert r.category=="billing" and r.priority=="high"

def test_urgent_technical(monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    r=triage_ticket("Production is down with an error and customers cannot access it.")
    assert r.category=="technical" and r.priority=="urgent" and r.needs_human

def test_empty_rejected():
    import pytest
    with pytest.raises(ValueError): triage_ticket("   ")

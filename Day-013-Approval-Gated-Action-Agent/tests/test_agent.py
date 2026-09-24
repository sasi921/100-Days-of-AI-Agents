import json
import pytest
from agent import propose, run

def test_proposal_requires_approval():
    p = propose("create task Review deployment")
    assert p.title == "Review deployment"
    assert p.requires_approval is True

def test_no_approval_does_not_write(tmp_path):
    store = tmp_path / "tasks.json"
    r = run("create task Review deployment", None, str(store))
    assert r.status == "awaiting_approval"
    assert not store.exists()

def test_denial_does_not_write(tmp_path):
    store = tmp_path / "tasks.json"
    r = run("create task Review deployment", False, str(store))
    assert r.status == "denied"
    assert not store.exists()

def test_approval_writes(tmp_path):
    store = tmp_path / "tasks.json"
    r = run("create task Review deployment", True, str(store))
    assert r.status == "executed"
    assert r.record_id
    assert json.loads(store.read_text())[0]["title"] == "Review deployment"

def test_append_preserves_records(tmp_path):
    store = tmp_path / "tasks.json"
    run("create task First", True, str(store))
    run("create task Second", True, str(store))
    assert len(json.loads(store.read_text())) == 2

def test_empty_request_rejected():
    with pytest.raises(ValueError):
        propose("   ")

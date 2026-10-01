from tools import search_lines
from agent import research

def test_search_returns_matching_line(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_text("Alpha builds agents.\nBeta sells coffee.\n")
    assert search_lines(str(path), "Who builds agents?")[0].line == 1

def test_research_is_grounded_without_key(tmp_path, monkeypatch):
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    path = tmp_path / "notes.txt"
    path.write_text("Atlas requires human approval.\n")
    result = research(str(path), "Does Atlas require human approval?")
    assert result.evidence
    assert "Atlas requires human approval" in result.answer

def test_no_evidence(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_text("Cats sleep.\n")
    result = research(str(path), "quantum networking")
    assert result.evidence == []
    assert "could not find" in result.answer

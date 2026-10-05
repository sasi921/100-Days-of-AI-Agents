import github_tool

class FakeResponse:
    def __init__(self, payload):
        self.payload = payload
    def raise_for_status(self):
        return None
    def json(self):
        return self.payload

def test_fetch_repo_snapshot(monkeypatch):
    payloads = [
        {
            "full_name": "demo/repo",
            "description": "Demo repo",
            "stargazers_count": 10,
            "forks_count": 2,
            "open_issues_count": 1,
            "subscribers_count": 3,
            "default_branch": "main",
            "archived": False,
        },
        {"Python": 1000},
        [{"title": "Bug report"}],
    ]

    def fake_get(*args, **kwargs):
        return FakeResponse(payloads.pop(0))

    monkeypatch.setattr(github_tool.requests, "get", fake_get)
    snapshot = github_tool.fetch_repo_snapshot("demo", "repo")

    assert snapshot.full_name == "demo/repo"
    assert snapshot.language_bytes["Python"] == 1000
    assert snapshot.recent_issue_titles == ["Bug report"]

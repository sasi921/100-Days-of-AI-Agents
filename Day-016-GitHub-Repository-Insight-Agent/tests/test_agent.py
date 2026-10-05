from models import RepoSnapshot
from agent import analyze_snapshot, score_repo

def sample_snapshot(**overrides):
    data = dict(
        full_name="demo/repo",
        description="Demo",
        stars=25,
        forks=4,
        open_issues=3,
        watchers=2,
        default_branch="main",
        archived=False,
        language_bytes={"Python": 1200},
        recent_issue_titles=["Improve docs"],
    )
    data.update(overrides)
    return RepoSnapshot(**data)

def test_score_is_bounded():
    assert 0 <= score_repo(sample_snapshot()) <= 100

def test_archived_repo_scores_lower():
    assert score_repo(sample_snapshot(archived=True)) < score_repo(sample_snapshot(archived=False))

def test_analysis_includes_language_strength():
    result = analyze_snapshot(sample_snapshot())
    assert any("Python" in item for item in result.strengths)

def test_zero_star_repo_gets_watch_item():
    result = analyze_snapshot(sample_snapshot(stars=0))
    assert any("No stars yet" in item for item in result.watch_items)

def test_high_issue_count_gets_watch_item():
    result = analyze_snapshot(sample_snapshot(open_issues=50))
    assert any("relatively high" in item for item in result.watch_items)

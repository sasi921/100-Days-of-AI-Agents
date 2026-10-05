from models import RepoInsight, RepoSnapshot
from github_tool import fetch_repo_snapshot

def score_repo(snapshot: RepoSnapshot) -> int:
    score = 50
    score += -35 if snapshot.archived else 10

    if snapshot.stars >= 100:
        score += 15
    elif snapshot.stars >= 10:
        score += 8
    elif snapshot.stars > 0:
        score += 3

    if snapshot.forks >= 20:
        score += 10
    elif snapshot.forks > 0:
        score += 4

    if snapshot.language_bytes:
        score += 5

    if snapshot.open_issues > 100:
        score -= 10
    elif snapshot.open_issues > 25:
        score -= 5

    return max(0, min(100, score))

def analyze_snapshot(snapshot: RepoSnapshot) -> RepoInsight:
    strengths = []
    watch_items = []

    if snapshot.language_bytes:
        top_language = max(snapshot.language_bytes, key=snapshot.language_bytes.get)
        strengths.append(f"Primary implementation language: {top_language}.")
    else:
        watch_items.append("No language data was returned by GitHub.")

    if snapshot.stars > 0:
        strengths.append(f"Community interest: {snapshot.stars} stars.")
    else:
        watch_items.append("No stars yet; improve discoverability and sharing.")

    if snapshot.forks > 0:
        strengths.append(f"Reuse signal: {snapshot.forks} forks.")

    if snapshot.open_issues > 25:
        watch_items.append(f"Open issue count is relatively high: {snapshot.open_issues}.")

    if snapshot.archived:
        watch_items.append("Repository is archived and read-only.")

    if not snapshot.recent_issue_titles:
        watch_items.append("No recent open issue titles were available.")

    score = score_repo(snapshot)
    summary = (
        f"{snapshot.full_name} has a health score of {score}/100, "
        f"{snapshot.stars} stars, {snapshot.forks} forks, and "
        f"{snapshot.open_issues} open issues."
    )

    return RepoInsight(
        repository=snapshot.full_name,
        health_score=score,
        summary=summary,
        strengths=strengths,
        watch_items=watch_items,
        snapshot=snapshot,
    )

def inspect_repository(owner: str, repo: str) -> RepoInsight:
    return analyze_snapshot(fetch_repo_snapshot(owner, repo))

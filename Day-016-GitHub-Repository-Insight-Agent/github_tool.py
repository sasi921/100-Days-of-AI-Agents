import os
import requests
from models import RepoSnapshot

API_ROOT = "https://api.github.com"

class GitHubToolError(RuntimeError):
    pass

def _headers() -> dict[str, str]:
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "100-days-ai-agents-day-016",
    }
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    return headers

def _get(url: str, *, params=None, timeout: float = 8.0):
    try:
        response = requests.get(url, headers=_headers(), params=params, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except (requests.RequestException, ValueError) as exc:
        raise GitHubToolError(f"GitHub API request failed: {exc}") from exc

def fetch_repo_snapshot(owner: str, repo: str) -> RepoSnapshot:
    if not owner.strip() or not repo.strip():
        raise ValueError("owner and repo are required")

    base = f"{API_ROOT}/repos/{owner}/{repo}"
    metadata = _get(base)
    languages = _get(f"{base}/languages")
    issues = _get(f"{base}/issues", params={"state": "open", "sort": "updated", "per_page": 5})

    issue_titles = [
        item["title"] for item in issues
        if "pull_request" not in item and item.get("title")
    ]

    return RepoSnapshot(
        full_name=metadata["full_name"],
        description=metadata.get("description"),
        stars=metadata.get("stargazers_count", 0),
        forks=metadata.get("forks_count", 0),
        open_issues=metadata.get("open_issues_count", 0),
        watchers=metadata.get("subscribers_count", metadata.get("watchers_count", 0)),
        default_branch=metadata.get("default_branch", "main"),
        archived=metadata.get("archived", False),
        language_bytes=languages,
        recent_issue_titles=issue_titles,
    )

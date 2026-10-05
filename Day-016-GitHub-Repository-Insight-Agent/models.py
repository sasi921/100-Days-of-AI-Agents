from pydantic import BaseModel, Field

class RepoSnapshot(BaseModel):
    full_name: str
    description: str | None = None
    stars: int = Field(ge=0)
    forks: int = Field(ge=0)
    open_issues: int = Field(ge=0)
    watchers: int = Field(ge=0)
    default_branch: str
    archived: bool
    language_bytes: dict[str, int]
    recent_issue_titles: list[str]

class RepoInsight(BaseModel):
    repository: str
    health_score: int = Field(ge=0, le=100)
    summary: str
    strengths: list[str]
    watch_items: list[str]
    snapshot: RepoSnapshot

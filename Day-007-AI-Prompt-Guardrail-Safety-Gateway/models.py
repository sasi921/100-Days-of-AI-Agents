from typing import Literal
from pydantic import BaseModel, Field


class ModerationResult(BaseModel):
    decision: Literal["allow", "review", "block"]
    categories: list[str] = Field(default_factory=list)
    confidence: float = Field(ge=0, le=1)
    reason: str
    safe_response: str | None = None

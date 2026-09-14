from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field


class ActionItem(BaseModel):
    task: str = Field(..., min_length=1)
    owner: Optional[str] = None
    due_date: Optional[str] = None


class MeetingSummary(BaseModel):
    summary: str = Field(..., min_length=1)
    decisions: List[str] = Field(default_factory=list)
    action_items: List[ActionItem] = Field(default_factory=list)
    open_questions: List[str] = Field(default_factory=list)

from typing import Literal
from pydantic import BaseModel, Field

Intent = Literal["summarize", "extract_tasks", "answer_question", "draft_reply", "unknown"]

class RouteDecision(BaseModel):
    intent: Intent
    confidence: float = Field(ge=0.0, le=1.0)
    reason: str
    handler: str
    needs_clarification: bool = False

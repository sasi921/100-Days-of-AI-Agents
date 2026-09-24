from typing import Literal
from pydantic import BaseModel, Field

class ActionProposal(BaseModel):
    action: Literal["create_task"]
    title: str = Field(min_length=1, max_length=200)
    reason: str
    risk: Literal["low", "medium", "high"] = "low"
    requires_approval: bool = True

class ExecutionResult(BaseModel):
    status: Literal["awaiting_approval", "denied", "executed"]
    proposal: ActionProposal
    record_id: str | None = None
    message: str

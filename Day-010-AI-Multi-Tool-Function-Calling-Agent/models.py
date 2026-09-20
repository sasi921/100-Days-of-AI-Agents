from typing import Literal, Any
from pydantic import BaseModel, Field
class ToolCall(BaseModel):
    tool: Literal["calculator","word_count","none"]
    arguments: dict[str, Any] = Field(default_factory=dict)
    reason: str
class AgentResult(BaseModel):
    tool_call: ToolCall
    observation: dict[str, Any] | None = None
    answer: str

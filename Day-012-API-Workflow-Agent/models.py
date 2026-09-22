from pydantic import BaseModel, Field
class Todo(BaseModel):
    id: int
    title: str
    completed: bool
class WorkflowResult(BaseModel):
    user_id: int
    total: int = Field(ge=0)
    completed: int = Field(ge=0)
    pending: int = Field(ge=0)
    next_action: str
    todos: list[Todo]

from pydantic import BaseModel, Field

class Evidence(BaseModel):
    source: str
    line: int = Field(ge=1)
    text: str

class ResearchResult(BaseModel):
    question: str
    answer: str
    evidence: list[Evidence]

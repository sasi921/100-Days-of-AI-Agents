import re
from models import ActionProposal, ExecutionResult
from tools import create_task

def propose(request: str) -> ActionProposal:
    text = request.strip()
    if not text:
        raise ValueError("request cannot be empty")
    cleaned = re.sub(r"^(please\s+)?(create|add|make)\s+(a\s+)?task\s*(to|for|:)?\s*", "", text, flags=re.I).strip()
    title = cleaned or text
    return ActionProposal(action="create_task", title=title[:200], reason="The request asks for a state-changing task creation action.", risk="low", requires_approval=True)

def run(request: str, approval: bool | None = None, store: str = "tasks.json") -> ExecutionResult:
    proposal = propose(request)
    if approval is None:
        return ExecutionResult(status="awaiting_approval", proposal=proposal, message="Action proposed but not executed. Re-run with explicit approval.")
    if approval is False:
        return ExecutionResult(status="denied", proposal=proposal, message="Action denied. No state was changed.")
    record_id = create_task(proposal.title, store)
    return ExecutionResult(status="executed", proposal=proposal, record_id=record_id, message="Approved action executed and recorded.")

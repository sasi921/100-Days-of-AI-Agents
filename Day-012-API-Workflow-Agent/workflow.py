from models import WorkflowResult
from todo_tool import fetch_todos
def run_workflow(user_id:int)->WorkflowResult:
    todos=fetch_todos(user_id)
    completed=sum(t.completed for t in todos)
    pending=len(todos)-completed
    pending_items=[t for t in todos if not t.completed]
    next_action=(f"Start with: {pending_items[0].title}" if pending_items else "All tasks are complete.")
    return WorkflowResult(user_id=user_id,total=len(todos),completed=completed,pending=pending,next_action=next_action,todos=todos)

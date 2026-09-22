from models import Todo
import workflow
def test_workflow_aggregates(monkeypatch):
    monkeypatch.setattr(workflow,"fetch_todos",lambda uid:[Todo(id=1,title="Ship docs",completed=True),Todo(id=2,title="Add tests",completed=False)])
    r=workflow.run_workflow(7)
    assert (r.total,r.completed,r.pending)==(2,1,1)
    assert r.next_action=="Start with: Add tests"
def test_all_complete(monkeypatch):
    monkeypatch.setattr(workflow,"fetch_todos",lambda uid:[Todo(id=1,title="Done",completed=True)])
    assert workflow.run_workflow(1).next_action=="All tasks are complete."
def test_invalid_user():
    from todo_tool import fetch_todos
    import pytest
    with pytest.raises(ValueError): fetch_todos(0)

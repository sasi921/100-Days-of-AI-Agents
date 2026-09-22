import requests
from models import Todo
BASE_URL="https://jsonplaceholder.typicode.com"
class TodoToolError(RuntimeError): pass
def fetch_todos(user_id:int, timeout:float=5.0)->list[Todo]:
    if user_id < 1: raise ValueError("user_id must be >= 1")
    try:
        r=requests.get(f"{BASE_URL}/todos",params={"userId":user_id},timeout=timeout)
        r.raise_for_status()
        data=r.json()
    except (requests.RequestException, ValueError) as exc:
        raise TodoToolError(f"Todo API failed: {exc}") from exc
    return [Todo.model_validate(x) for x in data]

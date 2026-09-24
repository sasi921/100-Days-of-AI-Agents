import json, uuid
from pathlib import Path

def create_task(title: str, store: str = "tasks.json") -> str:
    path = Path(store)
    records = []
    if path.exists():
        records = json.loads(path.read_text(encoding="utf-8"))
    record_id = str(uuid.uuid4())
    records.append({"id": record_id, "title": title, "status": "open"})
    path.write_text(json.dumps(records, indent=2), encoding="utf-8")
    return record_id

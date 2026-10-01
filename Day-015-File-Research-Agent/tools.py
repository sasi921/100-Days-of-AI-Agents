from pathlib import Path
from models import Evidence

def read_text(path: str) -> list[str]:
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(path)
    return p.read_text(encoding="utf-8").splitlines()

def search_lines(path: str, query: str, limit: int = 5) -> list[Evidence]:
    terms = {t.lower().strip(".,?!") for t in query.split() if len(t) > 2}
    scored = []
    for n, line in enumerate(read_text(path), 1):
        words = set(line.lower().replace(",", " ").replace(".", " ").split())
        score = len(terms & words)
        if score:
            scored.append((score, n, line.strip()))
    scored.sort(key=lambda x: (-x[0], x[1]))
    return [Evidence(source=path, line=n, text=text) for _, n, text in scored[:limit]]

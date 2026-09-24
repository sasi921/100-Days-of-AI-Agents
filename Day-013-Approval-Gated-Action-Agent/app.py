import argparse, json
from agent import run

def main():
    p = argparse.ArgumentParser(description="Approval-gated task action agent")
    p.add_argument("request")
    gate = p.add_mutually_exclusive_group()
    gate.add_argument("--approve", action="store_true")
    gate.add_argument("--deny", action="store_true")
    p.add_argument("--store", default="tasks.json")
    a = p.parse_args()
    approval = True if a.approve else False if a.deny else None
    print(json.dumps(run(a.request, approval, a.store).model_dump(), indent=2))

if __name__ == "__main__":
    main()

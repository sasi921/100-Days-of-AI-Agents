import argparse,json
from agent import run_agent
p=argparse.ArgumentParser(description="A tiny tool-using AI agent")
p.add_argument("request",nargs="+")
a=p.parse_args()
print(json.dumps(run_agent(" ".join(a.request)),indent=2))

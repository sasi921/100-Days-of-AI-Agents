import argparse, json
from agent import run
def main():
    p=argparse.ArgumentParser(description="AI function-calling agent with a small tool registry")
    p.add_argument("request",nargs="+")
    a=p.parse_args()
    print(json.dumps(run(" ".join(a.request)).model_dump(),indent=2))
if __name__=="__main__": main()

import argparse, json
from workflow import run_workflow
def main():
    p=argparse.ArgumentParser(description="Run a multi-step API workflow over a user's todos.")
    p.add_argument("user_id",type=int)
    p.add_argument("--show-items",action="store_true")
    a=p.parse_args()
    result=run_workflow(a.user_id)
    data=result.model_dump()
    if not a.show_items: data.pop("todos")
    print(json.dumps(data,indent=2))
if __name__=="__main__": main()

import argparse,json
from db import connect,seed
from agent import ask
def main():
 p=argparse.ArgumentParser(description="Ask questions of a local SQLite dataset using guarded read-only SQL.")
 p.add_argument("question"); p.add_argument("--db",default="demo.db")
 a=p.parse_args(); con=connect(a.db); seed(con)
 print(json.dumps(ask(con,a.question),indent=2))
if __name__=="__main__": main()

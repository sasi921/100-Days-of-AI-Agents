import argparse, json
from dataclasses import asdict
from agent import triage_ticket

def main():
    p=argparse.ArgumentParser(description="AI Support Ticket Triage Bot")
    p.add_argument("ticket", help="Path to a text support ticket")
    args=p.parse_args()
    with open(args.ticket, encoding="utf-8") as f: ticket=f.read()
    print(json.dumps(asdict(triage_ticket(ticket)), indent=2))

if __name__=="__main__": main()

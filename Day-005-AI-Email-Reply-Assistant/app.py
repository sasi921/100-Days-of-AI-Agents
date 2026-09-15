from __future__ import annotations
import argparse
from pathlib import Path
from dotenv import load_dotenv
from reply_agent import ReplyRequest, generate_reply

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Draft a safe, tone-controlled email reply.")
    p.add_argument("email_file", type=Path, help="Text file containing the received email")
    p.add_argument("--goal", required=True, help="What the reply should accomplish")
    p.add_argument("--tone", choices=["professional", "friendly", "concise"], default="professional")
    return p.parse_args()

def main() -> None:
    load_dotenv()
    args = parse_args()
    email = args.email_file.read_text(encoding="utf-8")
    print(generate_reply(ReplyRequest(email=email, goal=args.goal, tone=args.tone)))

if __name__ == "__main__":
    main()

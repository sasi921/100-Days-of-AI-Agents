import argparse
import json
from pathlib import Path
from router import route

parser = argparse.ArgumentParser(description="AI intent router")
parser.add_argument("text", nargs="?")
parser.add_argument("--file")
args = parser.parse_args()
text = Path(args.file).read_text(encoding="utf-8") if args.file else args.text
if not text:
    parser.error("Provide text or --file")
print(json.dumps(route(text).model_dump(), indent=2))

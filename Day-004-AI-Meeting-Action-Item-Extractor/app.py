from __future__ import annotations

import argparse
import json
from pathlib import Path

from agent import llm_extract


def main() -> None:
    parser = argparse.ArgumentParser(description="Turn a meeting transcript into structured action items.")
    parser.add_argument("transcript", help="Path to a .txt transcript")
    parser.add_argument("--model", default="gpt-4.1-mini", help="OpenAI model when OPENAI_API_KEY is set")
    parser.add_argument("--output", help="Optional JSON output path")
    args = parser.parse_args()

    transcript_path = Path(args.transcript)
    transcript = transcript_path.read_text(encoding="utf-8")
    result = llm_extract(transcript, model=args.model)
    payload = result.model_dump()
    rendered = json.dumps(payload, indent=2)
    print(rendered)

    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

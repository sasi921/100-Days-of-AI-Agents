from __future__ import annotations

import argparse
import sys

from agent import research_page
from web_tool import fetch_page


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Research a public webpage and produce a grounded AI briefing."
    )
    parser.add_argument("url", help="Public http(s) webpage to research")
    parser.add_argument("--question", "-q", help="Optional question to answer using only the page")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        page = fetch_page(args.url)
        print(research_page(page.title, page.url, page.text, args.question))
        return 0
    except (ValueError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"Unexpected error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

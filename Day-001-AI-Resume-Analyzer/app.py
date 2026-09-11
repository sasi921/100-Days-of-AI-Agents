import argparse
import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

from analyzer import ResumeAnalyzer


def read_text_file(path: str) -> str:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    return file_path.read_text(encoding="utf-8")


def print_report(result: dict) -> None:
    print("\n=== AI Resume Analyzer ===")
    print(f"Match score: {result['match_score']}/100")
    print(f"\nSummary:\n{result['summary']}")

    sections = [
        ("Matched skills", "matched_skills"),
        ("Missing skills", "missing_skills"),
        ("Resume improvements", "resume_improvements"),
        ("Interview questions", "interview_questions"),
    ]

    for title, key in sections:
        print(f"\n{title}:")
        items = result.get(key, [])
        if not items:
            print("- None")
            continue
        for item in items:
            print(f"- {item}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compare a resume with a job description using an LLM."
    )
    parser.add_argument("--resume", required=True, help="Path to a plain-text resume.")
    parser.add_argument(
        "--job",
        required=True,
        help="Path to a plain-text job description.",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Print raw JSON instead of the formatted report.",
    )
    return parser


def main() -> int:
    load_dotenv()

    parser = build_parser()
    args = parser.parse_args()

    if not os.getenv("OPENAI_API_KEY"):
        print(
            "Error: OPENAI_API_KEY is not set. Copy .env.example to .env and add your key.",
            file=sys.stderr,
        )
        return 2

    try:
        resume_text = read_text_file(args.resume)
        job_text = read_text_file(args.job)
        result = ResumeAnalyzer().analyze(resume_text, job_text)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_report(result)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

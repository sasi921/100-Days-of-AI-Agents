import argparse
import json

from guardrail import check


def main() -> None:
    parser = argparse.ArgumentParser(description="Guardrail gateway for AI application inputs")
    parser.add_argument("text", nargs="?", help="Text to inspect")
    parser.add_argument("--file", help="Read input from a UTF-8 file")
    args = parser.parse_args()

    text = open(args.file, encoding="utf-8").read() if args.file else args.text
    if not text:
        parser.error("provide text or --file")

    print(json.dumps(check(text).model_dump(), indent=2))


if __name__ == "__main__":
    main()

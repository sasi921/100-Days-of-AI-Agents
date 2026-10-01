import argparse
import json
from agent import research

def main():
    parser = argparse.ArgumentParser(
        description="Ground answers in evidence retrieved from a local text file."
    )
    parser.add_argument("file")
    parser.add_argument("question")
    args = parser.parse_args()

    print(json.dumps(research(args.file, args.question).model_dump(), indent=2))

if __name__ == "__main__":
    main()

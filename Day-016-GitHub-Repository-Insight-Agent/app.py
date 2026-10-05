import argparse
import json
from agent import inspect_repository

def main():
    parser = argparse.ArgumentParser(
        description="Inspect a public GitHub repository using multiple GitHub API tools."
    )
    parser.add_argument("repository", help="Repository in owner/name form")
    args = parser.parse_args()

    if "/" not in args.repository:
        parser.error("repository must be in owner/name form")

    owner, repo = args.repository.split("/", 1)
    result = inspect_repository(owner, repo)
    print(json.dumps(result.model_dump(), indent=2))

if __name__ == "__main__":
    main()

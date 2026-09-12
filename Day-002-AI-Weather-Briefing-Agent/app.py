from __future__ import annotations

import argparse
import json

from agent import run_weather_agent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="AI Weather Briefing Agent")
    parser.add_argument("city", help="City to check, e.g. 'Austin' or 'Hyderabad'")
    parser.add_argument("--fahrenheit", action="store_true", help="Use Fahrenheit and mph")
    parser.add_argument("--json", action="store_true", help="Print normalized weather data as JSON")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    data, briefing = run_weather_agent(args.city, fahrenheit=args.fahrenheit)

    print("\n=== AI Weather Briefing ===")
    print(briefing)
    if args.json:
        print("\n=== Normalized Tool Data ===")
        print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()

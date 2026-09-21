import argparse, json
from agent import build_briefing
def main():
    p=argparse.ArgumentParser(description="Weather tool agent using live Open-Meteo data")
    p.add_argument("city")
    a=p.parse_args()
    try: print(json.dumps(build_briefing(a.city).model_dump(),indent=2))
    except Exception as e: raise SystemExit(f"Weather lookup failed: {e}")
if __name__=="__main__": main()

from __future__ import annotations

import json
import os
from typing import Any

from dotenv import load_dotenv

from weather_api import fetch_forecast, geocode_city, normalize_forecast

load_dotenv()

WEATHER_CODES = {
    0: "clear sky",
    1: "mainly clear",
    2: "partly cloudy",
    3: "overcast",
    45: "fog",
    48: "rime fog",
    51: "light drizzle",
    53: "drizzle",
    55: "heavy drizzle",
    61: "light rain",
    63: "rain",
    65: "heavy rain",
    71: "light snow",
    73: "snow",
    75: "heavy snow",
    80: "rain showers",
    81: "rain showers",
    82: "heavy rain showers",
    95: "thunderstorms",
}


def _code_to_text(code: int) -> str:
    return WEATHER_CODES.get(code, f"weather code {code}")


def deterministic_briefing(data: dict[str, Any]) -> str:
    current = data["current"]
    units = data["units"]
    first_day = data["daily"][0] if data["daily"] else {}
    return (
        f"Weather briefing for {data['location']}: "
        f"currently {current['temperature']}{units['temperature']} and {_code_to_text(current['weather_code'])}, "
        f"feels like {current['feels_like']}{units['temperature']}. "
        f"Today's high is {first_day.get('high', '?')}{units['temperature']} with a low of "
        f"{first_day.get('low', '?')}{units['temperature']}. "
        f"Peak precipitation chance is {first_day.get('precipitation_probability', '?')}%. "
        f"Maximum wind is around {first_day.get('max_wind', '?')} {units['wind']}."
    )


def llm_briefing(data: dict[str, Any], model: str = "gpt-4o-mini") -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return deterministic_briefing(data)

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model=model,
            input=[
                {
                    "role": "system",
                    "content": (
                        "You are a concise weather briefing agent. Use only the provided weather data. "
                        "Return 4-6 short sentences: current conditions, today's range, rain/wind risk, "
                        "one practical suggestion, and a brief next-two-days outlook. Never invent data."
                    ),
                },
                {"role": "user", "content": json.dumps(data)},
            ],
        )
        return response.output_text.strip()
    except Exception as exc:
        fallback = deterministic_briefing(data)
        return f"{fallback}\n\n[AI summary unavailable: {exc.__class__.__name__}]"


def run_weather_agent(city: str, fahrenheit: bool = False) -> tuple[dict[str, Any], str]:
    location = geocode_city(city)
    raw_forecast = fetch_forecast(location, fahrenheit=fahrenheit)
    normalized = normalize_forecast(location, raw_forecast)
    summary = llm_briefing(normalized)
    return normalized, summary

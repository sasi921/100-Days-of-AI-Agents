from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import requests


GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"


@dataclass(frozen=True)
class Location:
    name: str
    country: str
    latitude: float
    longitude: float
    timezone: str


class WeatherAPIError(RuntimeError):
    """Raised when a weather API request cannot be completed."""


def geocode_city(city: str, timeout: int = 10) -> Location:
    city = city.strip()
    if not city:
        raise ValueError("City cannot be empty.")

    response = requests.get(
        GEOCODING_URL,
        params={"name": city, "count": 1, "language": "en", "format": "json"},
        timeout=timeout,
    )
    response.raise_for_status()
    payload = response.json()
    results = payload.get("results") or []
    if not results:
        raise WeatherAPIError(f"No location found for '{city}'.")

    item = results[0]
    return Location(
        name=item["name"],
        country=item.get("country", ""),
        latitude=float(item["latitude"]),
        longitude=float(item["longitude"]),
        timezone=item.get("timezone", "auto"),
    )


def fetch_forecast(location: Location, fahrenheit: bool = False, timeout: int = 10) -> dict[str, Any]:
    params = {
        "latitude": location.latitude,
        "longitude": location.longitude,
        "current": "temperature_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m",
        "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,wind_speed_10m_max",
        "timezone": "auto",
        "forecast_days": 3,
    }
    if fahrenheit:
        params.update({"temperature_unit": "fahrenheit", "wind_speed_unit": "mph"})

    response = requests.get(FORECAST_URL, params=params, timeout=timeout)
    response.raise_for_status()
    payload = response.json()
    if "current" not in payload or "daily" not in payload:
        raise WeatherAPIError("Weather API response was missing required fields.")
    return payload


def normalize_forecast(location: Location, payload: dict[str, Any]) -> dict[str, Any]:
    current = payload["current"]
    daily = payload["daily"]
    days = []
    for index, date in enumerate(daily.get("time", [])):
        days.append(
            {
                "date": date,
                "weather_code": daily["weather_code"][index],
                "high": daily["temperature_2m_max"][index],
                "low": daily["temperature_2m_min"][index],
                "precipitation_probability": daily["precipitation_probability_max"][index],
                "max_wind": daily["wind_speed_10m_max"][index],
            }
        )

    return {
        "location": f"{location.name}, {location.country}".strip(", "),
        "timezone": payload.get("timezone", location.timezone),
        "current": {
            "temperature": current["temperature_2m"],
            "feels_like": current["apparent_temperature"],
            "precipitation": current["precipitation"],
            "weather_code": current["weather_code"],
            "wind_speed": current["wind_speed_10m"],
        },
        "daily": days,
        "units": {
            "temperature": payload.get("current_units", {}).get("temperature_2m", "°C"),
            "wind": payload.get("current_units", {}).get("wind_speed_10m", "km/h"),
            "precipitation": payload.get("current_units", {}).get("precipitation", "mm"),
        },
    }

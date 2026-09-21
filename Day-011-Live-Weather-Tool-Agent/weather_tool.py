import json
from urllib.parse import urlencode
from urllib.request import urlopen
from models import WeatherObservation

GEO="https://geocoding-api.open-meteo.com/v1/search"
FORECAST="https://api.open-meteo.com/v1/forecast"

def _get(url, params):
    with urlopen(url+"?"+urlencode(params), timeout=10) as r:
        return json.load(r)

def get_weather(city: str) -> WeatherObservation:
    city=city.strip()
    if not city: raise ValueError("city is required")
    geo=_get(GEO, {"name":city,"count":1,"language":"en","format":"json"})
    if not geo.get("results"): raise ValueError(f"City not found: {city}")
    p=geo["results"][0]
    data=_get(FORECAST, {"latitude":p["latitude"],"longitude":p["longitude"],"current":"temperature_2m,wind_speed_10m,weather_code"})
    c=data["current"]
    return WeatherObservation(city=f'{p["name"]}, {p.get("country","")}'.strip(", "), temperature_c=c["temperature_2m"], wind_kph=c["wind_speed_10m"], weather_code=c["weather_code"], source="Open-Meteo")

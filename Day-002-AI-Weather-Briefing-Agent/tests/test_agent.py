from agent import deterministic_briefing


def test_deterministic_briefing_contains_actionable_weather_details():
    data = {
        "location": "Austin, United States",
        "current": {
            "temperature": 80,
            "feels_like": 82,
            "precipitation": 0,
            "weather_code": 1,
            "wind_speed": 7,
        },
        "daily": [
            {
                "date": "2026-09-12",
                "weather_code": 1,
                "high": 90,
                "low": 70,
                "precipitation_probability": 10,
                "max_wind": 15,
            }
        ],
        "units": {"temperature": "°F", "wind": "mph", "precipitation": "inch"},
    }
    text = deterministic_briefing(data)
    assert "Austin" in text
    assert "90°F" in text
    assert "10%" in text
    assert "15 mph" in text

from weather_api import Location, normalize_forecast


def test_normalize_forecast_builds_expected_shape():
    location = Location("Austin", "United States", 30.26, -97.74, "America/Chicago")
    payload = {
        "timezone": "America/Chicago",
        "current": {
            "temperature_2m": 80,
            "apparent_temperature": 82,
            "precipitation": 0,
            "weather_code": 1,
            "wind_speed_10m": 7,
        },
        "current_units": {"temperature_2m": "°F", "wind_speed_10m": "mph", "precipitation": "inch"},
        "daily": {
            "time": ["2026-09-12"],
            "weather_code": [1],
            "temperature_2m_max": [90],
            "temperature_2m_min": [70],
            "precipitation_probability_max": [10],
            "wind_speed_10m_max": [15],
        },
    }
    result = normalize_forecast(location, payload)
    assert result["location"] == "Austin, United States"
    assert result["current"]["temperature"] == 80
    assert result["daily"][0]["high"] == 90
    assert result["units"]["temperature"] == "°F"

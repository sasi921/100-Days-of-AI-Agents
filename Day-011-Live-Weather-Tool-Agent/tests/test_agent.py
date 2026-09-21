from models import WeatherObservation
import agent
def fake(city):
    return WeatherObservation(city="Austin, United States",temperature_c=32,wind_kph=12,weather_code=0,source="test")
def test_briefing(monkeypatch):
    monkeypatch.setattr(agent,"get_weather",fake)
    b=agent.build_briefing("Austin")
    assert "32.0°C" in b.message and "hydration" in b.message
def test_weather_description():
    assert agent.describe(0)=="clear"
    assert agent.describe(95)=="stormy"
def test_cold(monkeypatch):
    monkeypatch.setattr(agent,"get_weather",lambda c: WeatherObservation(city=c,temperature_c=2,wind_kph=35,weather_code=71,source="test"))
    m=agent.build_briefing("Oslo").message
    assert "cold" in m and "strong winds" in m

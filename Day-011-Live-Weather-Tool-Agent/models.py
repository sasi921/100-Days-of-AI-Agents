from pydantic import BaseModel, Field
class WeatherRequest(BaseModel):
    city: str = Field(min_length=1)
class WeatherObservation(BaseModel):
    city: str
    temperature_c: float
    wind_kph: float
    weather_code: int
    source: str
class Briefing(BaseModel):
    observation: WeatherObservation
    message: str

from models import Briefing
from weather_tool import get_weather

def describe(code:int)->str:
    if code==0:return "clear"
    if code in (1,2,3):return "partly cloudy"
    if code in (45,48):return "foggy"
    if code in range(51,68) or code in range(80,83):return "rainy"
    if code in range(71,78) or code in (85,86):return "snowy"
    if code in (95,96,99):return "stormy"
    return "mixed conditions"

def build_briefing(city:str)->Briefing:
    o=get_weather(city)
    msg=f"{o.city}: {o.temperature_c:.1f}°C, {describe(o.weather_code)}, wind {o.wind_kph:.1f} km/h."
    if o.temperature_c >= 30: msg += " Plan for heat and hydration."
    elif o.temperature_c <= 5: msg += " Dress for cold conditions."
    if o.wind_kph >= 30: msg += " Expect strong winds."
    return Briefing(observation=o,message=msg)

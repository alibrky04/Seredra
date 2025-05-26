from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from seredra.models.weather_models import CityQuery, WeatherReport
from seredra.services.weather_service import get_weather
from seredra.db.database import get_session
from seredra.utils.logger import log_error

router = APIRouter()

@router.get("/weather", response_model=WeatherReport)
def weather(city: str, unit: str = "metric", session: Session = Depends(get_session)) -> WeatherReport:
	city_query = CityQuery(city=city, unit=unit)
	try:
		return get_weather(session, city_query)
	except Exception as e:
		log_error(f"Error fetching weather for {city}: {e}")
		raise HTTPException(status_code=500, detail="Failed to retrieve weather data")

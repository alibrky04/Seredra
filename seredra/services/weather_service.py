from typing import Optional
from sqlmodel import select, Session
import time
from seredra.core.weather_fetcher import fetch_weather
from seredra.core.data_processor import process_raw_api_data
from seredra.models.weather_models import WeatherReport, CityQuery
from seredra.models.sql_models import WeatherEntry
from seredra.utils.logger import log_info

CACHE_TTL_SECONDS = 900

def get_cached_weather(session: Session, city: str) -> Optional[WeatherEntry]:
	result = session.exec(
		select(WeatherEntry).where(WeatherEntry.city == city).order_by(WeatherEntry.timestamp.desc())
	)
	return result.first()

def save_weather_to_db(session: Session, weather_report: WeatherReport) -> None:
	entry = WeatherEntry(
		city=weather_report.city,
		temperature=weather_report.temperature.current,
		feels_like=weather_report.temperature.feels_like,
		humidity=weather_report.temperature.humidity,
		weather_main=weather_report.conditions[0].main if weather_report.conditions else "",
		weather_desc=weather_report.conditions[0].description if weather_report.conditions else "",
		wind_speed=weather_report.wind.speed,
		wind_deg=weather_report.wind.degree,
		timestamp=weather_report.timestamp,
	)
	session.add(entry)
	session.commit()

def get_weather(session: Session, city_query: CityQuery) -> WeatherReport:
	city = city_query.city
	unit = city_query.unit
	
	cached = get_cached_weather(session, city)
	now = int(time.time())

	if cached and (now - cached.timestamp) < CACHE_TTL_SECONDS:
		log_info(f"Serving cached weather for {city}")
		return WeatherReport(
			city=cached.city,
			temperature={
				"temp": cached.temperature,
				"feels_like": cached.feels_like,
				"temp_min": cached.temperature,
				"temp_max": cached.temperature,
				"humidity": cached.humidity,
			},
			conditions=[{"main": cached.weather_main, "description": cached.weather_desc}],
			wind={"speed": cached.wind_speed, "degree": cached.wind_deg},
			timestamp=cached.timestamp,
		)

	log_info(f"Fetching fresh weather for {city} from API")
	raw_data = fetch_weather(city, unit)  # must be sync
	processed = process_raw_api_data(raw_data)
	weather_report = WeatherReport.parse_obj(processed)

	save_weather_to_db(session, weather_report)
	return weather_report
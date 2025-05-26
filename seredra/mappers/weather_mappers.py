from seredra.models.weather_models import (
	WeatherReport,
	Temperature,
	Wind,
	WeatherCondition
)
from seredra.models.sql_models import WeatherEntry

def db_to_report(entry: WeatherEntry) -> WeatherReport:
	return WeatherReport(
		city=entry.city,
		temperature=Temperature(
			temp=entry.temperature,
			feels_like=entry.feels_like,
			temp_min=entry.temperature,
			temp_max=entry.temperature,
			humidity=entry.humidity
		),
		conditions=[
			WeatherCondition(
				main=entry.weather_main,
				description=entry.weather_desc
			)
		],
		wind=Wind(
			speed=entry.wind_speed,
			deg=entry.wind_deg
		),
		timestamp=entry.timestamp
	)

def report_to_db(report: WeatherReport) -> WeatherEntry:
	return WeatherEntry(
		city=report.city,
		temperature=report.temperature.current,
		feels_like=report.temperature.feels_like,
		humidity=report.temperature.humidity,
		weather_main=report.conditions[0].main,
		weather_desc=report.conditions[0].description,
		wind_speed=report.wind.speed,
		wind_deg=report.wind.degree,
		timestamp=report.timestamp
	)
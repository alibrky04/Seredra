from pydantic import BaseModel, Field
from typing import Literal

class CityQuery(BaseModel):
	"""Query input model for weather requests."""
	city: str = Field(..., description="Name of the city to get weather for")
	unit: Literal["metric", "imperial", "standard"] = Field(
		"default", description="Units for temperature and wind speed"
	)

class WeatherCondition(BaseModel):
	main: str
	description: str

class Temperature(BaseModel):
	current: float = Field(..., alias="temp")
	feels_like: float
	min: float = Field(..., alias="temp_min")
	max: float = Field(..., alias="temp_max")
	humidity: int

class Wind(BaseModel):
	speed: float
	degree: int = Field(..., alias="deg")

class WeatherReport(BaseModel):
	city: str
	temperature: Temperature
	conditions: list[WeatherCondition]
	wind: Wind
	timestamp: int

	class Config:
		frozen = True
		allow_population_by_field_name = True
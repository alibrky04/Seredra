from sqlmodel import SQLModel, Field
from typing import Optional

class WeatherEntry(SQLModel, table=True):
	id: Optional[int] = Field(default=None, primary_key=True)
	city: str
	temperature: float
	feels_like: float
	humidity: int
	weather_main: str
	weather_desc: str
	wind_speed: float
	wind_deg: int
	timestamp: int
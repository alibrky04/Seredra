import requests
import os
from seredra.utils.logger import log_info, log_error

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city: str, unit: str = "metric") -> dict:
    """
    Fetches weather data synchronously from the OpenWeatherMap API.
    
    Args:
        city (str): City name.
        unit (str): Units for temperature, one of 'metric', 'imperial', or 'standard'.
        
    Returns:
        dict: Raw JSON response from the API.
    """
    params = {
        "q": city,
        "units": unit,
        "appid": API_KEY,
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        log_info(f"Weather data fetched for city: {city}")
        return response.json()
    except requests.RequestException as e:
        log_error(f"Error fetching weather data for city '{city}': {e}")
        raise

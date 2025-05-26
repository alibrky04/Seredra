from typing import Dict, Any, List

def extract_main_weather(data: Dict[str, Any]) -> Dict[str, Any]:
	"""
	Pure function: Extract main weather info from API response.
	"""
	return {
		"temp": data["main"]["temp"],
		"feels_like": data["main"]["feels_like"],
		"temp_min": data["main"].get("temp_min", data["main"]["temp"]),
		"temp_max": data["main"].get("temp_max", data["main"]["temp"]),
		"humidity": data["main"]["humidity"],
	}

def extract_conditions(data: Dict[str, Any]) -> List[Dict[str, str]]:
	"""
	Pure function: Extract weather conditions list from API response.
	"""
	return [
		{"main": condition["main"], "description": condition["description"]}
		for condition in data.get("weather", [])
	]

def extract_wind(data: Dict[str, Any]) -> Dict[str, Any]:
	"""
	Pure function: Extract wind info from API response.
	"""
	return {
		"speed": data["wind"]["speed"],
		"deg": data["wind"]["deg"],
	}

def process_raw_api_data(data: Dict[str, Any]) -> Dict[str, Any]:
	"""
	Pure function: Transform raw API JSON data into clean dict.
	"""
	return {
		"city": data["name"],
		"temperature": extract_main_weather(data),
		"conditions": extract_conditions(data),
		"wind": extract_wind(data),
		"timestamp": data["dt"],
	}
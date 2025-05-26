from typing import Literal

UnitSystem = Literal["metric", "imperial", "standard"]

def celsius_to_fahrenheit(celsius: float) -> float:
	return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
	return (fahrenheit - 32) * 5 / 9

def mps_to_mph(mps: float) -> float:
	return mps * 2.23694

def mph_to_mps(mph: float) -> float:
	return mph / 2.23694

def convert_temperature(temp: float, from_unit: UnitSystem, to_unit: UnitSystem) -> float:
	if from_unit == to_unit:
		return temp
	elif from_unit == "metric" and to_unit == "imperial":
		return celsius_to_fahrenheit(temp)
	elif from_unit == "imperial" and to_unit == "metric":
		return fahrenheit_to_celsius(temp)
	elif from_unit == "standard" and to_unit == "metric":
		return temp - 273.15
	elif from_unit == "standard" and to_unit == "imperial":
		return celsius_to_fahrenheit(temp - 273.15)
	elif from_unit == "metric" and to_unit == "standard":
		return temp + 273.15
	elif from_unit == "imperial" and to_unit == "standard":
		return fahrenheit_to_celsius(temp) + 273.15
	raise ValueError(f"Unsupported temperature conversion: {from_unit} to {to_unit}")

def convert_wind_speed(speed: float, from_unit: UnitSystem, to_unit: UnitSystem) -> float:
	if from_unit == to_unit:
		return speed
	elif from_unit == "metric" and to_unit == "imperial":
		return mps_to_mph(speed)
	elif from_unit == "imperial" and to_unit == "metric":
		return mph_to_mps(speed)
	elif from_unit == "standard":
		if to_unit == "imperial":
			return mps_to_mph(speed)
		return speed
	elif from_unit == "metric" and to_unit == "standard":
		return speed
	elif from_unit == "imperial" and to_unit == "standard":
		return mph_to_mps(speed)
	raise ValueError(f"Unsupported wind speed conversion: {from_unit} to {to_unit}")
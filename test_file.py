import urllib.request
import json
import os  # To read environment variables
from datetime import datetime

def get_weather_data():
    """Fetch 5-day weather forecast for Rexburg, Idaho using urllib."""
    api_key = os.getenv("OPENWEATHER_API_KEY")  # Get API key from environment variable
    if not api_key:
        print("API Key is missing!")
        return None
    url = f"https://api.openweathermap.org/data/2.5/forecast?q=Rexburg&appid={api_key}&units=imperial"

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode()
            return json.loads(data)
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def analyze_weather(temp, weather):
    """Analyze weather conditions and determine the outfit type."""
    if "rain" in weather:
        return "Rainy", "Waterproof jacket, boots, and an umbrella."
    elif "snow" in weather:
        return "Snowy", "Warm coat, gloves, and waterproof boots."
    elif "fog" in weather:
        return "Foggy", "Bright or reflective clothing for visibility."
    elif temp < 50:
        return "Cold", "Heavy coat, scarf, and gloves."
    elif temp < 68:
        return "Cool", "Light jacket or sweater."
    else:
        return "Warm", "T-shirt, shorts, and sunglasses."

def suggest_color(condition):
    """Suggest colors based on weather conditions."""
    color_suggestions = {
        "Rainy": "Bright colors like yellow or red to counter the gloomy atmosphere.",
        "Snowy": "Darker colors to absorb heat and keep warm.",
        "Foggy": "Neon or reflective colors to increase visibility.",
        "Cold": "Earth tones or deep hues for a cozy feel.",
        "Cool": "Pastel shades or neutral colors for layering.",
        "Warm": "Light colors to reflect heat and stay cool."
    }
    return color_suggestions.get(condition, "Wear what makes you feel great!")

def display_forecast(data):
    """Display the 5-day weather forecast with outfit suggestions."""
    if not data or 'list' not in data:
        print("No forecast data available.")
        return

    print("5-Day Weather Forecast for Rexburg, Idaho:\n")
    forecast_list = data['list']
    daily_forecasts = {}

    for forecast in forecast_list:
        dt_txt = forecast['dt_txt']
        date = dt_txt.split()[0]
        time = dt_txt.split()[1]

        temp = forecast['main']['temp']
        weather = forecast['weather'][0]['main'].lower()
        description = forecast['weather'][0]['description'].capitalize()

        if date not in daily_forecasts:
            daily_forecasts[date] = []
        
        daily_forecasts[date].append((time, temp, description, weather))

    for date, forecasts in daily_forecasts.items():
        print(f"Date: {date}")
        daily_temps = [temp for _, temp, _, _ in forecasts]
        avg_temp = sum(daily_temps) / len(daily_temps)
        main_weather = forecasts[0][3]  # Get the first weather condition of the day
        condition, outfit = analyze_weather(avg_temp, main_weather)
        color_tip =_

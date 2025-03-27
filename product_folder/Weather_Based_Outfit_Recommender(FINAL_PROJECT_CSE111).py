import urllib.request
import json

def get_weather_data():
    """Fetch weather data for Rexburg, Idaho using urllib."""
    api_key = "d6571c0e55ad5107d043260f161d8419"  # Replace with your actual API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q=Rexburg&appid={api_key}&units=imperial"

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode()
            return json.loads(data)
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return None

def analyze_weather(data):
    """Analyze weather conditions and determine the outfit type."""
    temp = data["main"]["temp"]
    weather = data["weather"][0]["main"].lower()
    
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

def main():
    weather_data = get_weather_data()
    
    if weather_data:
        condition, outfit = analyze_weather(weather_data)
        color_tip = suggest_color(condition)
        
        print(f"Weather Condition in Rexburg: {condition}")
        print(f"Outfit Suggestion: {outfit}")
        print(f"Fashion Tip: {color_tip}")
    else:
        print("Error fetching weather data. Please try again later.")

if __name__ == "__main__":
    main()

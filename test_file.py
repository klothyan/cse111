import unittest
from unittest.mock import patch
from Weather_Based_Outfit_Recommender import analyze_weather, suggest_color

class TestWeatherFunctions(unittest.TestCase):

    @patch('Weather_Based_Outfit_Recommender.get_weather_data')
    def test_analyze_weather(self, mock_get_weather_data):
        mock_data = {
            "main": {"temp": 45},
            "weather": [{"main": "Rain"}]
        }
        
        weather = mock_data["weather"][0]["main"].lower()
        
        mock_get_weather_data.return_value = mock_data
        
        condition, outfit = analyze_weather(mock_data, weather)
        self.assertEqual(condition, "Rainy")
        self.assertEqual(outfit, "Waterproof jacket, boots, and an umbrella.")
    
    def test_suggest_color(self):
        self.assertEqual(suggest_color("Rainy"), "Bright colors like yellow or red to counter the gloomy atmosphere.")
        self.assertEqual(suggest_color("Warm"), "Light colors to reflect heat and stay cool.")

if __name__ == "__main__":
    unittest.main()

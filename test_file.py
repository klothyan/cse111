import unittest
from unittest.mock import patch
from Weather_Based_Outfit_Recommender import analyze_weather, suggest_color  # Import from your actual program file

class TestWeatherFunctions(unittest.TestCase):

    @patch('Weather_Based_Outfit_Recommender.get_weather_data')  # Mocking the get_weather_data function
    def test_analyze_weather(self, mock_get_weather_data):
        # Mocked weather data
        mock_data = {
            "main": {"temp": 45},
            "weather": [{"main": "Rain"}]
        }
        
        # Set the mock return value
        mock_get_weather_data.return_value = mock_data
        
        # Test the analyze_weather function
        condition, outfit = analyze_weather(mock_data)
        self.assertEqual(condition, "Rainy")
        self.assertEqual(outfit, "Waterproof jacket, boots, and an umbrella.")
    
    def test_suggest_color(self):
        # Test the suggest_color function
        self.assertEqual(suggest_color("Rainy"), "Bright colors like yellow or red to counter the gloomy atmosphere.")
        self.assertEqual(suggest_color("Warm"), "Light colors to reflect heat and stay cool.")

if __name__ == "__main__":
    unittest.main()  # This ensures tests are run when the file is executed

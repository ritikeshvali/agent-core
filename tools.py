TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "search_weather",
            "description": "Search for current weather information for a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city name to search weather for"
                    },
                    "date": {
                        "type": "string",
                        "description": "The date (e.g., 'tomorrow', 'today')"
                    }
                },
                "required": ["location", "date"]
            }
        }
    }
]

def search_weather(location: str, date: str) -> str:
    """
    Mock weather search tool.
    In reality, this would call a real weather API.
    """

    weather_data = {
        "delhi_today": "Sunny, 28°C, winds 10 km/h",
        "delhi_tomorrow": "Partly cloudy, 26°C, chance of rain 20%",
        "london_today": "Rainy, 12°C, winds 15 km/h",
        "london_tomorrow": "Cloudy, 10°C, no rain expected",
    }

    key = f"{location.lower()}_{date.lower()}"

    if key in weather_data:
        return weather_data[key]
    else:
        return f"Weather data for {location} on {date} not available in mock database"
"""
Travel Weather Tool
-------------------
Shows weather and country information for any city.

Usage:
    python day3_travel_info.py

Requirements:
    pip install requests python-dotenv
    OPENWEATHER_API_KEY in .env file
"""

import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENWEATHER_API_KEY")


def save_to_file(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {filename}")


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def get_country_info(country_code):
    url = f"https://countries.dev/alpha/{country_code}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def run_tool():
    print("Travel Weather Tool")
    print("-------------------")
    
    city = input("Enter a city name: ").strip()
    
    if not city:
        print("No city entered. Exiting.")
        return

    print(f"\nFetching data for {city}...")

    weather_data = get_weather(city)

    if not weather_data:
        print(f"Could not find weather data for '{city}'. Check the city name and try again.")
        return

    country_code = weather_data["sys"]["country"]
    country_data = get_country_info(country_code)

    # Display weather
    print(f"\n=== {city.title()}, {country_code} ===")
    print(f"Temperature : {weather_data['main']['temp']}°C")
    print(f"Condition   : {weather_data['weather'][0]['description'].title()}")
    print(f"Humidity    : {weather_data['main']['humidity']}%")
    print(f"Wind        : {weather_data['wind']['speed']} m/s")

    # Display country info
    if country_data:
        print(f"\n=== Country Info ===")
        print(f"Country     : {country_data.get('name', 'Unknown')}")
        print(f"Capital     : {country_data.get('capital', 'Unknown')}")
        print(f"Region      : {country_data.get('region', 'Unknown')}")
        print(f"Population  : {country_data.get('population', 0):,}")
        
        currencies = country_data.get("currencies", [])
        if currencies:
            currency_names = [c["code"] for c in currencies]
            print(f"Currency    : {', '.join(currency_names)}")

    # Optional: save the data
    save_to_file({
        "weather": weather_data,
        "country": country_data
    }, f"{city.lower()}_travel_data.json")


if __name__ == "__main__":
    run_tool()

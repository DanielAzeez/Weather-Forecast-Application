#!/usr/bin/env python3


import requests

def get_weather(city, api_key):
    # OpenWeatherMap API endpoint
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()
        # Extract relevant information
        city_name = data['name']
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        return city_name, temperature, weather_description
    else:
        print("Error: Unable to fetch data.")
        return None

def main():
    api_key = "669cfa44525e719ca7249f527965476f"  # Replace with your API key
    city = input("Enter the city name: ")
    weather = get_weather(city, api_key)

    if weather:
        city_name, temperature, description = weather
        print(f"Weather in {city_name}: {temperature}°C, {description}")

if __name__ == "__main__":
    main()

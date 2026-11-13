import os
from dotenv import load_dotenv
import requests

load_dotenv()

class Weather:
    def __init__(self, Weather_data):
        self.name = Weather_data['location']['name']
        self.country = Weather_data['location']['country']
        self.region = Weather_data['location']['region']
        self.temp_c = Weather_data['current']['temp_c']
        self.temp_f = Weather_data['current']['temp_f']
        self.humidity = Weather_data['current']['humidity']
        self.condition = Weather_data['current']['condition']['text']
    def display_info(self):
        print(f'Name: {self.name}')
        print(f'Country: {self.country}')
        print(f'Region: {self.region}')
        print(f'Temperature (C): {self.temp_c} °C')
        print(f'Temperature (F): {self.temp_f} °F')
        print(f'Humidity: {self.humidity}%')
        print(f'Condition: {self.condition}')


WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
params = {
    'key': WEATHER_API_KEY,
    'q': 'Cairo',
}

try:
    endpoint ='https://api.weatherapi.com/v1/current.json'
    #wait up to 10 seconds for the request before raising a timeout exception.
    response = requests.get(endpoint, params=params, timeout=10)
    data = response.json()
    weather = Weather(data)
    weather.display_info()
except requests.exceptions.Timeout:
    print("The request timed out. Please try again later.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
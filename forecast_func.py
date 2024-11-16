import requests
import pandas as pd


API_KEY = '36gepPHxgAQvHJQo005ntzieNfuS9m3w'

def get_temperature_data(place, days):
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={place}&apikey={API_KEY}"
    response = requests.get(url)
    content = response.json()
    nr_data_values = days * 24
    hourly_data = content['timelines']['hourly']
    filtered_hourly_data = hourly_data[:nr_data_values]
    temperature_data = [temp['values']['temperature'] for temp in filtered_hourly_data[::4]]
    time_data = [hour['time'] for hour in filtered_hourly_data[::4]]
    return temperature_data, time_data

def get_weather_data(place, days):
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={place}&apikey={API_KEY}"
    response = requests.get(url)
    content = response.json()
    weather_code_df = pd.read_json('weathercode.json')
    nr_data_values = days * 24
    hourly_data = content['timelines']['hourly']
    filtered_hourly_data = hourly_data[:nr_data_values]
    weather_codes = [temp['values']['weatherCode'] for temp in filtered_hourly_data[::4]]
    weather_code_converted = [weather_code_df['weatherCode'][weather] for weather in weather_codes]
    time_data = [hour['time'] for hour in filtered_hourly_data[::4]]
    return weather_code_converted, time_data

if __name__ == "__main__":
    print(get_temperature_data('Dagupan', 1))

import requests


API_KEY = '36gepPHxgAQvHJQo005ntzieNfuS9m3w'

def get_temperature_data(place, days):
    url = f"https://api.tomorrow.io/v4/weather/forecast?location={place}&apikey={API_KEY}"
    response = requests.get(url)
    content = response.json()
    nr_data_values = days * 24
    hourly_data = content['timelines']['hourly']
    filtered_hourly_data = hourly_data[:nr_data_values]
    temperature_data = [temp['values']['temperature'] for temp in filtered_hourly_data]
    time_data = [hour['time'][11:16] for hour in filtered_hourly_data]
    return temperature_data, time_data

if __name__ == "__main__":
    print(get_temperature_data('Dagupan', 1))
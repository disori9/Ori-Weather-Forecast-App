def get_temperature_data(days):
    temporary_dates = ["2020", "2021", "2022", "2023", "2024"]
    temporary_temperatures = [10, 12, 25, 23, 21]
    temporary_temperatures = [days * x for x in temporary_temperatures]
    return temporary_dates, temporary_temperatures
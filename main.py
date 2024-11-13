import streamlit as st
import plotly.express as px

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:", placeholder="Input a place to view data")
forecast_days = st.slider("Forecast Days", 1, 5, 1, help="Select the number of forecasted days")
data_choice = ["Temperature", "Weather"]
select_data = st.selectbox("Select data to view", data_choice, index=1, placeholder="What data you want to see?")
st.subheader(f"{select_data} for the next {forecast_days} day/s in {place}")

def get_data(days):
    temporary_dates = ["2020", "2021", "2022", "2023", "2024"]
    temporary_temperatures = [10, 12, 25, 23, 21]
    temporary_temperatures = [forecast_days * x for x in temporary_temperatures]
    return temporary_dates, temporary_temperatures

dates, temperatures = get_data(forecast_days)
temp_figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (c)"})
st.plotly_chart(temp_figure)
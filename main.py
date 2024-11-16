import streamlit as st
import plotly.express as px
import forecast_func as ff

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:", placeholder="Input a place to view data")
forecast_days = st.slider("Forecast Days", 1, 5, 1, help="Select the number of forecasted days")
data_choice = ["Temperature", "Weather"]
select_data = st.selectbox("Select data to view", data_choice, index=1, placeholder="What data you want to see?")

if place:
    st.subheader(f"{select_data} for the next {forecast_days} day/s in {place}")
    if select_data == "Temperature":
        temperatures, times = ff.get_temperature_data(place, forecast_days)
        temp_figure = px.line(x=times, y=temperatures, labels={"x": "Date", "y": "Temperature (c)"})
        st.plotly_chart(temp_figure)

    if select_data == "Weather":
        weather, times = ff.get_weather_data(place, forecast_days)
        temp_figure = px.line(x=times, y=weather, labels={"x": "Date", "y": "Temperature (c)"})
        st.plotly_chart(temp_figure)

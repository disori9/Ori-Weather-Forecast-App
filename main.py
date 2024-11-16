import streamlit as st
import plotly.express as px
import forecast_func as ff
from dateutil import parser


st.title("Ori's Weather Forecasting App")
place = st.text_input("Place:", placeholder="Input a place to view data")
forecast_days = st.slider("Forecast Days", 1, 5, 1, help="Select the number of forecasted days")
data_choice = ["Temperature", "Weather"]
select_data = st.selectbox("Select data to view", data_choice, index=1, placeholder="What data you want to see?")


# Unfortunately, because of API limits, there is a limit on how much you can request on the website, it could have
# errors based on that
if place:
    st.subheader(f"{select_data} for the next {forecast_days} day/s in {place}")

    if select_data == "Temperature":
         try:
            temperatures, times = ff.get_temperature_data(place, forecast_days)
            temp_figure = px.line(x=times, y=temperatures, labels={"x": "Date", "y": "Temperature (c)"})
            st.plotly_chart(temp_figure)
         except KeyError:
            st.write("That place does not exist | The API request limit has been reached, please try again in an hour.")

    if select_data == "Weather":
        try:
            weather, times = ff.get_weather_data(place, forecast_days)
            imgs_paths = [f"imgs/{img_path}.png" for img_path in weather]
            time = [parser.isoparse(dtime).strftime('%B %d, %Y %I:%M%p') for dtime in times]
            st.image(imgs_paths, caption=time)
        except KeyError:
            st.write("That place does not exist | The API request limit has been reached, please try again in an hour.")


import streamlit as st


st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:", placeholder="Input a place to view data")
forecast_days = st.slider("Forecast Days", 1, 5, 1, help="Select the number of forecasted days")
data_choice = ["Temperature", "Weather"]
select_data = st.selectbox("Select data to view", data_choice, index=1, placeholder="What data you want to see?")
st.subheader(f"{select_data} for the next {forecast_days} day/s in {place}")

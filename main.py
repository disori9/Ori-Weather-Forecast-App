import streamlit as st


st.title("Weather Forecast for the Next Days")
st.text_input("Place:", placeholder="Input a place to view data")
forecast_days = st.slider("Forecast Days", 1, 5, 1)
data_choice = ["Temperature", "Weather"]
select_data = st.selectbox("Select data to view", data_choice, index=None, placeholder="What data you want to see?")
st.title("Temperature for the next 2 days in ")

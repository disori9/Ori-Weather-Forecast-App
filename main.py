import streamlit as st


st.title("Weather Forecast for the Next Days")
forecast_days = st.slider("Forecast Days", 1, 5, 1)
data_choice = ["Temperature", "Weather"]
select_data = st.selectbox("Select data to view", data_choice, index=None, placeholder="Select data")
st.title("Temperature for the next 2 days in ")

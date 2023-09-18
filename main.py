import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, select box and sub header
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast days:", min_value=1, max_value=5,
                 help="Select the number of days to be forecasted.")
option = st.selectbox("Select the data to view:", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")
if place:
# Gettemp and sky data
    try:
        filtered_data = get_data(place, days)

        if option == "Temperature":
        #Create a temp plot
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "temperature"})
            st.plotly_chart(figure)
        if option == "Sky":
            images = {"Clear": "weather_imgs/clear.png",
                      "Clouds": "weather_imgs/clouds.png",
                      "Rain": "weather_imgs/rain.png",
                      "Snow": "weather_imgs/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=115)
    except KeyError:
        st.write("That place does not exist.")
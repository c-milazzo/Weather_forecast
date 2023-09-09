import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forecast days:", min_value=1, max_value=5,
                 help="Select the number of days to be forecasted.")
option = st.selectbox("Select the data to view:", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

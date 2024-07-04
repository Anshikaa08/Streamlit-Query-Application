import streamlit as st
import requests

# Title of the app
st.title("API Query Application")

# Input fields for query parameters
param1 = st.text_input("Parameter 1")
param2 = st.text_input("Parameter 2")
param3 = st.text_input("Parameter 3")

# Button to submit the query
if st.button("Submit"):
    # Replace with your API endpoint
    api_url = f"https://api.example.com/data?param1={param1}&param2={param2}&param3={param3}"

    # Make a request to the API
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        st.write("Data Retrieved Successfully")
        st.json(data)
    else:
        st.write("Failed to retrieve data")

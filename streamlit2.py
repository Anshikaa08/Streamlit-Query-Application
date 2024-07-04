import streamlit as st
import requests

# Title of the app
st.title("User Data Query Application")

# Input fields for query parameters
user_id = st.text_input("User ID")

# Button to submit the query
if st.button("Submit"):
    # Replace with the sample API endpoint
    api_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    # Make a request to the API
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        st.write("Data Retrieved Successfully")
        st.json(data)
    else:
        st.write("Failed to retrieve data")
        st.write(f"Error Code: {response.status_code}")
        st.write(response.text)

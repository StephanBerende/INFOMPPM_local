import streamlit as st
import pandas as pd

# Configure the layout of the Streamlit page to use a wide format for more space
st.set_page_config(page_title = "User Profile", 
                   layout="wide",
                   page_icon= "👤"
)
st.sidebar.header("Select the page above.")


preference_options = {
    'Not interested': 1,
    'Mildly interested': 2,
    'Moderately interested': 3,
    'Highly Interested': 4,
    'Extremely Interested': 5
}

st.title("User Profile")

st.write("Are your reccomendations not what you expected? Change your preferences below by indicating how interested you are in each category.")

sport_preference = st.select_slider(
    'Sports',
    options=list(preference_options.keys()))

arts_preference = st.select_slider(
    'Arts',
    options=list(preference_options.keys()))

comedy_preference = st.select_slider(
    'Comedy',
    options=list(preference_options.keys()))

def get_preferences():
    preference_options = {
        'Not interested': 1,
        'Mildly interested': 2,
        'Moderately interested': 3,
        'Highly Interested': 4,
        'Extremely Interested': 5
    }

    sport_preference = st.select_slider(
        'Sports',
        options=list(preference_options.keys()))

    arts_preference = st.select_slider(
        'Arts',
        options=list(preference_options.keys()))

    comedy_preference = st.select_slider(
        'Comedy',
        options=list(preference_options.keys()))
    
    return {
        'sport_preference': sport_preference,
        'arts_preference': arts_preference,
        'comedy_preference': comedy_preference
    }

get_preferences()

    

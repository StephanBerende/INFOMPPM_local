import streamlit as st

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

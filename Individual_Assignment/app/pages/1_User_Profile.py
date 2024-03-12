import streamlit as st
import pandas as pd

# Configure the layout of the Streamlit page to use a wide format for more space
st.set_page_config(page_title = "Home Page", 
                   layout="wide",
                   page_icon= "👤"
)

df = pd.read_csv(r'C:\Users\Gebruiker\Documents\CODE\Master\Personalisation\INFOMPPM_local\Individual_Assignment\data\combined_dataframe.csv', sep=';', encoding='latin-1', low_memory=False)

st.title("User Profile", anchor= False)
st.write("Are your reccomendations not what you expected? Change your preferences below by indicating how interested you are in each category.")

preference_options = {
    'Not interested': 0,
    'Mildly interested': 1,
    'Moderately interested': 2,
    'Highly Interested': 3,
    'Extremely Interested': 4
}

sport_preference = st.select_slider(
    'Sports',
    options=list(preference_options.keys()),
    key = "sport_preference")

arts_preference = st.select_slider(
    'Arts',
    options=list(preference_options.keys()),
    key = 'arts_preference')

comedy_preference = st.select_slider(
    'Comedy',
    options=list(preference_options.keys()),
    key = "comedy_preference")

# Convert preferences to integers
sport_preference = preference_options[sport_preference]
arts_preference = preference_options[arts_preference]
comedy_preference = preference_options[comedy_preference]

# Calculate total score
total_score = sport_preference + arts_preference + comedy_preference

# Check if total score is 0 to avoid division by zero
if total_score == 0:
    # If all preferences are 0, assign equal weights to each category
    sport_score = 1/3
    arts_score = 1/3
    comedy_score = 1/3
else:
    # Calculate category scores
    sport_score = sport_preference / total_score
    arts_score = arts_preference / total_score
    comedy_score = comedy_preference / total_score

st.text('')
st.text('')
st.write("From now on, your recommendations will be made up as follows: Sports (", sport_score * 100, "%) , Arts (", arts_score * 100, "%) , Comedy(", comedy_score * 100, "%)" )
st.text('')

st.header("Subcategories")
st.write("If you want to further define your reccomendations, this can be done by selecting subcategories of the categories you enjoy.")

st.multiselect(
    'Sports Subcategories:',
    ['Football', 'Racing', 'Tennis', 'Cycling', 'Cricket', 'Baseball', 'Swimming'],
    ['Football', 'Racing', 'Cycling']
    )

st.multiselect(
    'Arts Subcategories:',
    ['Modern Art', 'Architecture', 'Music', 'Theatre', 'Painting'],
    ['Music', 'Theatre'])

st.multiselect(
    'Comedy Subcategories:',
    ['Stand-Up', 'Drama', 'Dark', 'Slapstick'],
    ['Stand-Up', 'Slapstick'])

st.text('')
if st.button("Back Home"):
    st.switch_page(r"Home.py")
















    

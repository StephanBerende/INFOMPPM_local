import streamlit as st
import pandas as pd
from preferences import get_preferences


# Configure the layout of the Streamlit page to use a wide format for more space
st.set_page_config(page_title = "Home Page", 
                   layout="wide",
                   page_icon= "🏠"
)
st.sidebar.header("Select the page above.")

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
    options=list(preference_options.keys()))

arts_preference = st.select_slider(
    'Arts',
    options=list(preference_options.keys()))

comedy_preference = st.select_slider(
    'Comedy',
    options=list(preference_options.keys()))

# Convert preferences to integers
sport_preference = preference_options[sport_preference]
arts_preference = preference_options[arts_preference]
comedy_preference = preference_options[comedy_preference]\


def calculate_preferences(sport_preference, arts_preference, comedy_preference):
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
    
    # Calculate the number of movies to display for each category based on the scores
    num_sport_movies = int(round((sport_score) * 10))
    num_arts_movies = int(round((arts_score) * 10))
    num_comedy_movies = int(round((comedy_score) * 10))

    st.write("From now on, your recommendations are made up as follows: Sports (", sport_score * 100, "%) , Arts (", arts_score * 100, "%) , Comedy(", comedy_score * 100, "%)" )
    
    # Filter the dataframe to get movies for each category
    sport_movies = df[df['category'] == 'Sports'].sample(n=num_sport_movies)
    arts_movies = df[df['category'] == 'Arts'].sample(n=num_arts_movies)
    comedy_movies = df[df['category'] == 'Comedy'].sample(n=num_comedy_movies)
    
    # Concatenate the dataframes and shuffle the result
    selected_movies = pd.concat([sport_movies, arts_movies, comedy_movies])
    selected_movies = selected_movies.sample(frac=1).reset_index(drop=True)
    
    return selected_movies
    
df_start = calculate_preferences(sport_preference, arts_preference, comedy_preference)


st.title("Recommended Just For You:", anchor= False)

col1, col2 = st.columns(2)
with col1:
    st.write("These videos were selected based on what you have watched and enjoyed earlier. If this does not allign with your expectations, you can change your preferences in the 'User Profile' tab, found in the sidebar. If you want to see something different, click the 'Try Something Else' button. ")
with col2:
    option = st.selectbox( "Try Something Else:" ,
                          ('Your Recommendations'+ '👤',
                           'What Are My Friends Watching?'+ '👥', 
                           'What\'s Popular?' + '🔥', 
                           'More...')
                           )
df_rec = df_start

# Load the dataset based on the selected option
if option == 'Your Recommendations':
    df_rec = df_start.sample(n=9, random_state=2)
elif option == 'What Are My Friends Watching?':
    df_rec = df.sample(n=9, random_state=3)
elif option == 'What\'s Popular?':
    df_rec = df.sample(n=9, random_state=4)
elif option == 'More...': 
    df_rec = df.sample(n=9, random_state=5)

# Calculate the number of rows needed based on the number of items in df_rec
num_rows = (len(df_rec) + 4) // 5

for row in range(num_rows):
    row_data = df_rec.iloc[row * 5: (row + 1) * 5]
    columns = st.columns(len(row_data))
    for i, col in enumerate(columns):
        if i < len(row_data):
            item = row_data.iloc[i]
            with col:
                st.image(item["image"])
                st.text(item["category"] + ": " + item["title"])
                



    



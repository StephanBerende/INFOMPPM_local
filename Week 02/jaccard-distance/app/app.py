import streamlit as st
import pandas as pd
import template as t
import itertools

st.set_page_config(layout="wide")

# load the dataset with the ratings
df_ratings = pd.read_csv(r'C:\Users\Gebruiker\Documents\CODE\Master\Personalisation\INFOMPPM_local\Week 02\jaccard-distance\data\BX-Book-Ratings-Subset.csv', sep=';', encoding='latin-1', low_memory=False)
df_books = pd.read_csv(r'C:\Users\Gebruiker\Documents\CODE\Master\Personalisation\INFOMPPM_local\Week 02\jaccard-distance\data\BX-Books.csv', sep=';', encoding='latin-1', low_memory=False)

# initialize a session state with a user
if 'User-ID' not in st.session_state:
  st.session_state['User-ID'] = 98783

# which user do you want to see?
st.session_state['User-ID'] = 98783


def get_jaccard_recommendations(id):
    
  # create lists per user
  users = df_ratings.groupby('User-ID')['ISBN'].apply(list)
    
  comparison_user = users[id]
  
  dist_list = []
  new_content = []
  similar_users = []
  
  for user, value in users.items():
      
      # calculate Jaccard distance
      union = set(comparison_user + users[user])
      intersect = list(set(comparison_user) & set(users[user]))
      jac_sim = len(intersect) / float(len(union))
      distance = 1 - jac_sim
      dist_list.append(distance)   
    
      # tweak this parameter. Closer to 0.0 is more the same. 0.0 is the user.
      if distance < 0.78 and distance != 0.0:
      
            
          # get the differences in sets (ISBN) from the the selected user and user in the for-loop
          # add these differences to new_content 
          new_items = set(users[user]).difference(comparison_user)
          new_content.extend(new_items)
          # add the user to similiar_users
          similar_users.append(user)
      else:
          pass
     
  # flatten the list with the sets
  new_content = set(new_content)
  # select the books
  selected_books = df_ratings["ISBN"].isin(new_content)
  df_recommendations = df_ratings[selected_books]
  df_recommendations = df_recommendations["ISBN"]
  df_recommendations = df_recommendations.to_frame().reset_index()
  return df_recommendations

# create a dataframe where you get all the ratings from the selected user
df_user_ratings = df_ratings[df_ratings['User-ID'] == st.session_state['User-ID']]

# display the reviews of the user
st.subheader('User '+str(st.session_state['User-ID'])+' reviewed')
df = df_user_ratings.merge(df_books, on='ISBN')
t.recommendations(df)

# display the recommendations for the user
st.subheader('Reviews based on Jaccard distance to other users')
df_recommendations = get_jaccard_recommendations(st.session_state['User-ID'])
df = df_recommendations.merge(df_books, on='ISBN')
df = df.drop_duplicates(subset=['ISBN']).head(10)
t.recommendations(df)

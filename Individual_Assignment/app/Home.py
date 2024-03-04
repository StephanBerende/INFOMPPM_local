import streamlit as st
import pandas as pd
from preferences import get_preferences


# Configure the layout of the Streamlit page to use a wide format for more space
st.set_page_config(page_title = "Home Page", 
                   layout="wide",
                   page_icon= "🏠"
)
st.sidebar.header("Select the page above.")

st.title("Recommended Just For You:", anchor= False)

col1, col2 = st.columns(2)
with col1:
    st.write("These videos were selected based on what you have watched and enjoyed earlier. If this does not allign with your expectations, you can change your preferences in the 'User Profile' tab, found in the sidebar. If you want to see something different, click the 'Try Something Else' button. ")
with col2:
    option = st.selectbox( "Try Something Else:",
                          ('Your Recommendations',
                           'What Are My Friends Watching?', 
                           'What\'s Popular?', 
                           'I\'m Feeling Lucky!')
                           )

# Load the dataset containing book information
df = pd.read_csv(r'C:\Users\Gebruiker\Documents\CODE\Master\Personalisation\INFOMPPM_local\Individual_Assignment\data\combined_dataframe.csv', sep=';', encoding='latin-1', low_memory=False)
df_rec = df[df["category"] == 'Sports']

# Load the dataset based on the selected option
if option == 'Your Recommendations':
    df_rec = df_rec.sample(n=6, random_state=2).head(6)
elif option == 'What Are My Friends Watching?':
    df_rec = df_rec.sample(n=6, random_state=3).head(6)
elif option == 'What\'s Popular?':
    df_rec = df_rec.sample(n=6, random_state=4).head(6)
else:  # 'I\'m Feeling Lucky!'
    df_rec = df_rec.sample(n=6, random_state=5).head(6)

# Calculate the number of rows needed based on the number of items in df_rec
num_rows = (len(df_rec) + 2) // 3

for row in range(num_rows):
    row_data = df_rec.iloc[row * 3: (row + 1) * 3]
    columns = st.columns(len(row_data))
    for i, col in enumerate(columns):
        if i < len(row_data):
            item = row_data.iloc[i]
            with col:
                st.image(item["image"])
                st.text(item["title"])



preferences = get_preferences()



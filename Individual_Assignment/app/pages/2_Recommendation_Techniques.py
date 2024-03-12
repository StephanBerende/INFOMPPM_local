import streamlit as st

# Configure the layout of the Streamlit page to use a wide format for more space
st.set_page_config(page_title = "Home Page", 
                   layout="wide",
                   page_icon= "🧭"
)
# Title
st.title("Select Recommendation Technique")

# Placeholder text
st.write("We use complex algorithms to suggest the best content for you, but nobody knows you better than yourself. We have already selected three recommendation algorithms for you, but you can change the used techniques at any time.")

# Create a two-column layout using st.beta_columns
emoji_col, checkbox_col, text_col = st.columns([0.2,2,4])

# Checkbox items
with checkbox_col:
    option1 = st.checkbox("The Copycat" + '🐈', value = True)
    option2 = st.checkbox("The Traditionalist" + '⛰️', value = True)
    option3 = st.checkbox("The Trendy" + '🔥', value = True)
    option4 = st.checkbox("The Adventurer" + '🧭')
    option5 = st.checkbox("The Renegade" + '😎')
    option6 = st.checkbox("The Oracle" + '🔮')
    option6 = st.checkbox("The Chaotic" + '⚡')
    

# Descriptive text for each checkbox item
with text_col:
    st.write("Reccomendations are based on users similar to you")
    st.write("Reccomendations based on what you have watched before")
    st.write("Videos that are popular right now")    
    st.write("Content categories which you have rarely watched before")
    st.write("Series you would normally never watch to broaden your horizon")
    st.write("Be the first to watch the newest content which suits your profile")
    st.write("Completely random content")

if st.button("Back Home"):
    st.switch_page(r"Home.py")


















    

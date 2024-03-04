import streamlit as st

preference_options = {
    'Not interested': 1,
    'Mildly interested': 2,
    'Moderately interested': 3,
    'Highly Interested': 4,
    'Extremely Interested': 5
}

# Define main category sliders and buttons
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        sports_preference = st.select_slider('Sports', options=list(preference_options.keys()))

    with col2:
        st.button("Show More")



selected_subcategories = st.multiselect("Choose Subcategories:", ["Football", "Tennis", "Basketball", "Cricket"])















    

import pandas as pd
import streamlit as st
import plotly.express as px
import re

st.set_page_config(layout='wide', page_title='Restaurant Dashboard')

@st.cache_data
def load_data():
    url = 'https://raw.githubusercontent.com/skathirmani/datasets/refs/heads/main/restaurant_reviews.csv'
    data = pd.read_csv(url)
    return data

reviews = load_data()

# Clean the `rating` column to extract only the rating as number
reviews['rating_cleaned'] = reviews['rating'].str.replace('Rated ', '').astype(float)

# Extract `Monthname` from `date` column
reviews['date'] = pd.to_datetime(reviews['date'], format='%d/%m/%y %H:%M')
reviews['Monthname'] = reviews['date'].dt.strftime('%B')

# Using `rev_count` create two new columns for `reviews_count` and `followers_count`
reviews['reviews_count'] = reviews['rev_count'].apply(lambda v: int(re.findall('[0-9]+', v)[0]))
reviews['followers_count'] = reviews['rev_count'].apply(lambda v: int(re.findall('[0-9]+', v)[1]))

# Sidebar header and name
st.sidebar.header('Restaurant Review Analysis')
st.sidebar.write('Hamreeth.L.S')  # Replace with your name

# Text input for filtering based on words in the `text` column
filter_text = st.sidebar.text_input("Filter by text:")

# Filtering the DataFrame based on the text input
if filter_text:
    filtered_reviews = reviews[reviews['text'].str.contains(filter_text, case=False)]
else:
    filtered_reviews = reviews

# Monthname filter
selected_month = st.sidebar.selectbox("Select Month", options=reviews['Monthname'].unique())
filtered_reviews = filtered_reviews[filtered_reviews['Monthname'] == selected_month]

# Bar chart for Top 5 Restaurants based on average rating
top_restaurants = filtered_reviews.groupby('res_name')['rating_cleaned'].mean().nlargest(5).reset_index()
fig_restaurants = px.bar(top_restaurants, x='res_name', y='rating_cleaned', title='Top 5 Restaurants by Average Rating')
st.plotly_chart(fig_restaurants)

# Bar chart for Top 5 Users based on total followers count
top_followers = filtered_reviews.groupby('res_name')['followers_count'].sum().nlargest(5).reset_index()
fig_followers = px.bar(top_followers, x='res_name', y='followers_count', title='Top 5 Restaurants by Total Followers Count')
st.plotly_chart(fig_followers)

# Display the filtered DataFrame below the charts
st.write(filtered_reviews)

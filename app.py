import streamlit as st
import pickle
import pandas as pd
import requests
import os

API_KEY = "46f74c05"

def fetch_poster(movie_id, movie_title):
    """
    Fetches the poster URL from OMDb using IMDb ID first,
    then falls back to movie title, and finally to default.jpeg.
    """
    # Try with IMDb IDgit add README.md
    if movie_id:
        url = f"http://www.omdbapi.com/?i=tt{movie_id}&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        if data.get("Poster") and data["Poster"] != "N/A":
            return data["Poster"]

    # Fallback: Try with movie title
    if movie_title:
        url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
        response = requests.get(url)
        data = response.json()
        if data.get("Poster") and data["Poster"] != "N/A":
            return data["Poster"]

    # Final fallback: Use default.jpeg from project folder
    default_path = os.path.join(os.getcwd(), "default.jpeg")
    return default_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key=lambda x:x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        movie_title = movies.iloc[i[0]].title
        #fetch poster from API
        recommended_movie_posters.append(fetch_poster(movie_id,movie_title))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    
    return recommended_movie_names,recommended_movie_posters

st.header('Movie Recommendation System')
movies=pickle.load(open('movie_list.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))


movie_list=movies['title'].values
selected_movie=st.selectbox(
    "Type or Select a movie, and we will suggest 5 similar ones:",
    movie_list
)

if st.button('Recommendation'):
        recommended_movie_names,recommended_movie_posters =recommend(selected_movie)

        # To show Posters
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1: 
            st.text(recommended_movie_names[0])
            st.image(recommended_movie_posters[0])  
        with col2:
            st.text(recommended_movie_names[1])
            st.image(recommended_movie_posters[1])
        with col3:
            st.text(recommended_movie_names[2])
            st.image(recommended_movie_posters[2])
        with col4:
            st.text(recommended_movie_names[3])
            st.image(recommended_movie_posters[3])
        with col5:
            st.text(recommended_movie_names[4])
            st.image(recommended_movie_posters[4])


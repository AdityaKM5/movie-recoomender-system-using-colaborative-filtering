import pickle
import streamlit as st
import requests
import numpy as np

def fetch_movie_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
def recommend(movie):
    index= np.where(pt.index==movie)[0][0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommend_movie_names = []
    recommend_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies[movies['original_title']== pt.index[i[0]]]['tmdbId'].values[0]
        recommend_movie_posters.append(fetch_movie_poster(movie_id))
        recommend_movie_names.append(pt.index[i[0]])

    return recommend_movie_names,recommend_movie_posters


st.header('Movie Recommender System')
movies = pickle.load(open('filtered.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
similarity = pickle.load(open('colaborative_similarity.pkl','rb'))

#popular= pickle.load(open('popular.pkl','rb'))

movie_list = movies['original_title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown",movie_list)

if st.button('Show Recommendation'):
    recommend_movie_names,recommend_movie_posters = recommend(selected_movie)
    column1, column2, column3, column4, column5 = st.columns(5)
    with column1:
        st.text(recommend_movie_names[0])
        st.image(recommend_movie_posters[0])
    with column2:
        st.text(recommend_movie_names[1])
        st.image(recommend_movie_posters[1])

    with column3:
        st.text(recommend_movie_names[2])
        st.image(recommend_movie_posters[2])
    with column4:
        st.text(recommend_movie_names[3])
        st.image(recommend_movie_posters[3])
    with column5:
        st.text(recommend_movie_names[4])
        st.image(recommend_movie_posters[4])

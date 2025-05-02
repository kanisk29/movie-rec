import streamlit as st
import pickle
import requests

st.set_page_config(
    page_title="Movie Recommender",
    layout="wide"
)

movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

st.title("🎬 Movie Recommender System")
st.subheader("Discover your next favorite movie with posters!")

def fetch_itunes_poster(movie_title):
    params = {"term": movie_title, "media": "movie", "limit": 1}
    results = requests.get("https://itunes.apple.com/search", params=params).json().get("results", [])
    if results:
        url = results[0].get("artworkUrl100", "")
        return url.replace("100x100bb", "600x600bb")
    return None

def recommend(movie_title):
    idx = movies[movies['title'] == movie_title].index[0]
    distances = similarity[idx]
    top_indices = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in top_indices]

col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    selected_movie = st.selectbox(
        "Select a movie:",
        movies['title'].values
    )
    if st.button("Get Recommendations"):
        recs = recommend(selected_movie)
        cols = st.columns(len(recs))
        for idx, title in enumerate(recs):
            with cols[idx]:
                poster_url = fetch_itunes_poster(title)
                if poster_url:
                    st.image(poster_url, use_container_width=True)
                st.write(title)

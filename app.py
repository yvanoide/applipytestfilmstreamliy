import streamlit as st
from models.movies_data import MoviesData

def main():
    st.title("Projet de Dashboard pour les Tests")

    # Charger les données depuis le fichier CSV
    movies_data = MoviesData("/home/yves/iadev-python/stepro/py-testing-main/py-streamlit/sl-test/data/netflix_titles.csv")

    # Afficher une liste courte de films
    st.subheader("Liste courte de films :")
    short_list_size = st.slider("Nombre de films à afficher :", min_value=1, max_value=100, value=10)
    short_list = movies_data.get_short_list(short_list_size)
    st.dataframe(short_list)

    # Afficher un graphique des années de sortie des films
    st.subheader("Graphique des années de sortie :")
    release_years = movies_data.get_realyse_years_array()
    st.bar_chart(release_years)

if __name__ == "__main__":
    main()

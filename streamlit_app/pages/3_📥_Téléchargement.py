import streamlit as st
from config import set_sidebar_styles
import pandas as pd
st.set_page_config(
    page_title="Application de Scraping et d'Analyse",
    page_icon="📥",
    layout="wide"
)
set_sidebar_styles()

st.title('📥 Téléchargement des données déjà scrapées')
select_options = [
    "Dataset des Chiens",
    "Dataset des Moutons",
    "Dataset des Poules Lapins & Pigeons",
    "Autres animaux"
]


# Label and select input
selected_option = st.selectbox("Choisissez la dataset que vous souhaitez afficher et télécharger", select_options)
st.write(f"### {selected_option}")

match selected_option:
    case "Dataset des Chiens":
        df = pd.read_csv('cleaned_data/chiens.csv')
    case "Dataset des Moutons":
        df = pd.read_csv('cleaned_data/moutons.csv')
    case "Dataset des Poules Lapins & Pigeons":
        df = pd.read_csv('cleaned_data/poules_lapins_et_pigeons.csv')
    case "Autres animaux":
        df = pd.read_csv('cleaned_data/autres_animaux.csv')
        
st.dataframe(df)
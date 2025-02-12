import streamlit as st
from config import set_sidebar_styles
# Configuration de la page
st.set_page_config(
    page_title="Application de Scraping et d'Analyse",
    page_icon="📝",
    layout="wide"
)
set_sidebar_styles()



st.title("📝 Formulaire d'évaluation de l'app")

# Embed the KoboToolbox form using an iframe
st.markdown(
    """
    <iframe src="https://ee.kobotoolbox.org/i/dBbzjx7D" width="800" height="1000"></iframe>
    """,
    unsafe_allow_html=True
)
import streamlit as st
from config import set_sidebar_styles
# Configuration de la page
st.set_page_config(
    page_title="Application de Scraping et d'Analyse",
    page_icon="📊",
    layout="wide"
)
set_sidebar_styles()
# Titre principal
st.title("Bienvenue sur mon App de Scraping & Analyse 👋🏽")

# Sous-titre
st.subheader("Une solution complète pour scraper, analyser et évaluer vos données.")

# Section descriptive
st.markdown("""
Cette application vous permet de réaliser plusieurs tâches liées au scraping de données et à leur analyse. Voici ce que vous pouvez faire :

### 1. **Scraper des Données**
### 2. **Télécharger des Données Non Nettoyées**
### 3. **Voir un Dashboard des Données Nettoyées**
### 4. **Remplir un Formulaire d'Évaluation**
---


""")


# Bouton pour naviguer vers une autre section
if st.button("Commencer à Explorer"):
    st.switch_page("pages/2_📊_Tableau_de_bord.py")

    # st.sidebar.success("Utilisez le menu latéral pour naviguer.")
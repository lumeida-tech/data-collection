import streamlit as st
from config import set_sidebar_styles
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

st.set_page_config(
    page_title="Application de Scraping et d'Analyse",
    page_icon="📊",
    layout="wide"
)
set_sidebar_styles()

st.title('📊 Tableau de bord')

# Charger les trois datasets
@st.cache_data  # Pour éviter de recharger les données à chaque exécution
def load_data():
    chiens_df = pd.read_csv("cleaned_data/chiens.csv")
    moutons_df = pd.read_csv("cleaned_data/moutons.csv")
    poules_lapins_et_pigeons_df = pd.read_csv("cleaned_data/poules_lapins_et_pigeons.csv")
    return chiens_df, moutons_df, poules_lapins_et_pigeons_df

chiens_df, moutons_df, poules_lapins_et_pigeons_df = load_data()

# Nettoyage des données
def clean_price(price):
    if isinstance(price, str) and price != "Prix sur demande":
        return int(price.replace("CFA", "").replace(" ", ""))
    return None  # Ignorer "Prix sur demande"

# Ajouter une colonne "Catégorie" et nettoyer les prix pour chaque DataFrame
chiens_df['Catégorie'] = 'Chiens'
chiens_df['Prix_net'] = chiens_df['Prix'].apply(clean_price)

moutons_df['Catégorie'] = 'Moutons'
moutons_df['Prix_net'] = moutons_df['Prix'].apply(clean_price)

poules_lapins_et_pigeons_df['Catégorie'] = 'Poules, Lapins & Pigeons'
poules_lapins_et_pigeons_df['Prix_net'] = poules_lapins_et_pigeons_df['Prix'].apply(clean_price)

# Combiner les trois DataFrames en un seul
combined_df = pd.concat([chiens_df, moutons_df, poules_lapins_et_pigeons_df])

# Filtrer les lignes avec des prix valides
cleaned_df = combined_df.dropna(subset=['Prix_net'])


# Graphique 1 : Comparaison des prix moyens par catégorie
st.subheader("Comparaison des prix moyens par catégorie d'animaux")
average_prices = cleaned_df.groupby('Catégorie')['Prix_net'].mean().sort_values(ascending=False)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=average_prices.index, y=average_prices.values, palette="coolwarm", ax=ax2)
ax2.set_title("Comparaison des prix moyens par catégorie d'animaux", fontsize=16)
ax2.set_xlabel("Catégorie d'animaux", fontsize=12)
ax2.set_ylabel("Prix moyen (CFA)", fontsize=12)
plt.xticks(rotation=45)
st.pyplot(fig2)


# Graphique 2 : Nombre d'annonces par ville/région
st.subheader("Nombre d'annonces par ville/région")
# Extraire les villes/régions à partir de la colonne Adresse
combined_df['Ville'] = combined_df['Adresse'].str.split(',').str[0]

# Compter le nombre d'annonces par ville/région
city_counts = combined_df['Ville'].value_counts()

# Créer le graphique
plt.figure(figsize=(12, 6))
sns.barplot(x=city_counts.index, y=city_counts.values, palette="viridis")
plt.title("Nombre d'annonces par ville/région", fontsize=16)
plt.xlabel("Ville/Région", fontsize=12)
plt.ylabel("Nombre d'annonces", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Afficher le graphique dans Streamlit
st.pyplot(plt)

# Graphique 3 : Nombre d'annonces par ville/région
st.subheader("Comparaison des Prix Moyens par Région")

# Extraire les régions/villes à partir de la colonne Adresse
combined_df['Région'] = combined_df['Adresse'].str.split(',').str[0]

# Filtrer les lignes avec des prix valides
cleaned_df = combined_df.dropna(subset=['Prix_net'])

# Calculer les prix moyens par région
average_prices_by_region = cleaned_df.groupby('Région')['Prix_net'].mean().sort_values(ascending=False)

# Créer le graphique
plt.figure(figsize=(12, 6))
sns.barplot(x=average_prices_by_region.index, y=average_prices_by_region.values, palette="coolwarm")
plt.title("Comparaison des Prix Moyens par Région", fontsize=16)
plt.xlabel("Région", fontsize=12)
plt.ylabel("Prix Moyen (CFA)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Afficher le graphique dans Streamlit
st.pyplot(plt)


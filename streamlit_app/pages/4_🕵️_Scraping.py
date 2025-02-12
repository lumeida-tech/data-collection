import streamlit as st
from config import set_sidebar_styles
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

st.set_page_config(
    page_title="Application de Scraping et d'Analyse",
    page_icon="🕵️",
    layout="wide"
)

set_sidebar_styles()

st.title('🕵️ Scraping de données sur plusieurs page')

select_options = [
    "URL page des Chiens",
    "URL page des Moutons",
    "URL page des Poules Lapins & Pigeons",
    "URL page Autres animaux"
]

selected_option = st.selectbox("Choisissez l'url de la page à scrapper", select_options)


match selected_option:
    case "URL page des Chiens":
        url = 'https://sn.coinafrique.com/categorie/chiens'
    case "URL page des Moutons":
        url = 'https://sn.coinafrique.com/categorie/moutons'
    case "URL page des Poules Lapins & Pigeons":
        url = 'https://sn.coinafrique.com/categorie/poules-lapins-et-pigeons'
    case "URL page Autres animaux":
        url = 'https://sn.coinafrique.com/categorie/autres-animaux'

data = []

if st.button("Lancez le scraping"):

    progress_bar = st.progress(0)
    success_message_placeholder = st.empty()
    status_text = st.empty()

    response = requests.get(url)
    bsp = bs(response.text, 'html.parser')
    containers = bsp.find_all('div', class_='col s6 m4 l3')


    total_items = len(containers)
    for i, item in enumerate(containers):
        try:

            progress = (i + 1) / total_items
            progress_bar.progress(progress)

            image_url = item.find('img', class_='ad__card-img').attrs['src']
            price = item.find('p', class_='ad__card-price').text.strip()
            adresse = item.find('p', class_='ad__card-location').find('span').text
            info = {
                "Image_lien": image_url,
                "Prix": price,
                "Adresse": adresse,
            }

            if selected_option == 'URL page des Poules Lapins & Pigeons':
                details_page_url = item.find('a', class_='card-image ad__card-image waves-block waves-light')['href']
                details_page_response = requests.get(f'https://sn.coinafrique.com{details_page_url}')
                details_page_bsp = bs(details_page_response.text, 'html.parser')
                
                element_detail = details_page_bsp.find('div', class_='ad__info__box ad__info__box-descriptions')
                if element_detail:
                    paragraphs = element_detail.find_all('p')
                    if len(paragraphs) >= 2:
                        info['Détail'] = paragraphs[1].text.strip().replace('\r\n', ' ').replace('\r\r', ' ')
                else:
                    info['Détail'] = ""
            else:
                name = item.find('p', class_='ad__card-description').text.strip()
                info['Nom'] = name

            data.append(info)
            
            if progress < 1: 
                status_text.text(f"Scraping en cours... {int(progress * 100)}%")
            else:   
                status_text.empty()
                success_message_placeholder.success("Scraping terminé avec succès'.")
               
                
        except Exception as e:
            st.error(f"Erreur lors du scraping : {e}")


    df = pd.DataFrame(data)

    st.write(f"### Données scraper")

    st.dataframe(df)
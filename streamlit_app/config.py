import streamlit as st

def set_sidebar_styles():
    st.markdown("""
    <style>
        /* Modifier la taille des éléments du menu */
        [data-testid="stSidebarNav"] ul {
            font-size: 20px;
        }
        
        /* Change button hover color */
        div.stButton > button:hover {
            border-color: #2E86C1 !important;  /* Blue color for hover */
            color: #2E86C1 !important;
        }
        
        div.stButton > button:focus {
            background-color: #2E86C1 !important;  /* Blue color for hover */
            color: white !important;
            border-color: #2E86C1
        }

        /* Ajouter des icônes aux entrées du menu en fonction de leur ordre */
        [data-testid="stSidebarNav"] ul li:nth-of-type(1) span:before {
            content: "🏠 "; /* Icône Accueil */
        }
    </style>
    """, unsafe_allow_html=True)

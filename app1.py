import streamlit as st
import pandas as pd

# Chargement des utilisateurs
@st.cache_data
def load_users():
    return pd.read_csv("users.csv")

users_df = load_users()

# --- Authentification simple ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = ""

st.title("Mon Application Chien 🐶")

if not st.session_state.logged_in:
    st.subheader("Connexion")
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    if st.button("Se connecter"):
        user = users_df[(users_df["name"] == username) & (users_df["password"] == password)]
        if not user.empty:
            st.success("Connexion réussie !")
            st.session_state.logged_in = True
            st.session_state.username = username
        else:
            st.error("Nom d'utilisateur ou mot de passe incorrect")
else:
    # Menu sidebar
    st.sidebar.title("Menu")
    st.sidebar.write(f"Bienvenue {st.session_state.username} 👋")
    page = st.sidebar.radio("Navigation", ["Accueil", "Album", "Déconnexion"])

    if page == "Déconnexion":
        st.session_state.logged_in = False
        st.rerun()

    elif page == "Accueil":
        st.write("🎉 Bienvenue sur la page d'accueil de l'application !")

    elif page == "Album":
        st.subheader("📸 Album de Chien")
        
        # Liste des images locales
        images = ["Akita Inu 1.png", "Akita Inu 2.png", "Akita Inu 3.png"]
        
        cols = st.columns(3)
        for i, img in enumerate(images):
            with cols[i % 3]:
                st.image(img, caption=f"Chien {i+1}")
        st.write("Voici quelques photos de chiens Akita Inu. Profitez-en !")
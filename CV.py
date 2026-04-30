import streamlit as st

#Configuration de la Page
st.title("Portfolio Professionel") 

st.header("Profil")
st.write("Je suis Technichien Supérieur en Géomatique")

st.subheader("COMPETENCES")
col1 ,col2 = st.columns(2)
with col1:
    st.subheader("SIG et Cartographie")
    st.write("-Confection de cartes thématique")
    st.write("-Hiérarchisation des réseaux routiers")
    st.write("-Manipulation de données administratives")
    st.write("-Numérisation d'image")
with col2:
    st.subheader("Programmation")
    st.write("-Developpement d'outils avec Python")
    st.write("-Automatisation de calculs")
    st.write("-Création d'interfaces(streamlit)")
    st.write("-Github")


col1 ,col2, = st.columns(2)
with col1:
    st.subheader("Topographie")
    st.write("-Calculs de gisements")
    st.write("-Dessin technique sur Autocad")
with col2:
    st.header("Bureautique")
    st.write("Word")
    st.write("Excel")
    st.write("Powerpoint")



#Le Baccalauréat
st.subheader("Baccalauréat")

st.markdown("""
* Série : L2
* Mention : Passable""")


with st.sidebar:
    st.header("Abdourahmane Ba")
    st.subheader("Brevet Technique Supérieur en Géomatique")
    st.write("Dakar, Sénégal|+221 77 163 64 42|")
    st.write("avdourahmaneba19@gmail.com")
   















    
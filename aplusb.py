import streamlit as st

# Titre de l'application
st.title("Additionneur de deux nombres")

# Entrée des nombres
num1 = st.number_input("Entrez le premier nombre :", value=0.0)
num2 = st.number_input("Entrez le deuxième nombre :", value=0.0)

# Bouton pour effectuer l'addition
if st.button("Additionner"):
    resultat = num1 + num2
    st.success(f"Résultat : {resultat}")

# Entrada principal

''' Importamos la biblioteca Streamlit con el alias st '''
import streamlit as st

# Configuramos el titulo, icono y diseño de la app
st.set_page_config(
    page_title="TechoVivo",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="auto"
)

# Principal
st.title("🌿 TechoVivo")
st.subheader("Una solucion sostenible para gestionar el agua de la lluvia")
st.write("""
    Bienvenido a **TechoVivo**, una aplicacion interactiva creada como parte de un estudio de tesis que analiza como los jardines verdes en azoteas pueden **Reducir el impacto del agua de lluvia** en las calles urbanas.

         Usa el menu lateral para navegar entre:
         - 📘 Introduccion del proyecto
         - 🌧️ Simulacion de captacion de agua
         - ⚖️ Comparacion con/sin jardin
         - ℹ️ Acerca del proyecto     
""")

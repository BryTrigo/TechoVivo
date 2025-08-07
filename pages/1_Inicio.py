import streamlit as st

st.set_page_config(
    page_title="TechoVivo",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="auto"
)

st.title("📘 Introducción")

st.markdown("""
El raudal urbano causado por lluvias intensas es un problema creciente en muchas ciudades.  
La falta de áreas verdes y la impermeabilización del suelo hacen que grandes volúmenes de agua escurran rápidamente hacia las calles, generando inundaciones, daños a la infraestructura y problemas de movilidad.

---

## 🌿 ¿Qué propone *TechoVivo*?

El uso de **jardines verdes en azoteas** permite:

- Retener y absorber parte del agua de lluvia  
- Retrasar el tiempo en que el agua llega a la calle  
- Reducir el caudal del escurrimiento superficial  
- Contribuir a mejorar el microclima urbano

---

Este proyecto busca **simular, analizar y visualizar** el impacto que tendría esta solución en la regulación del agua pluvial, comparando resultados **con** y **sin** jardín en la azotea.
""")

# Mostrar imagen (asegurate de tener esta imagen en /pages/images/ o ajusta la ruta)
st.image("pages/images/techo_verde.png",
         caption="Ejemplo de jardín verde en azotea reteniendo agua")

# Preguntas frecuentes
st.header("❓ Preguntas frecuentes")

with st.expander("¿Qué es un jardín verde en azotea?"):
    st.write("Es un sistema que utiliza plantas y sustrato para retener y absorber agua de lluvia, disminuyendo el escurrimiento hacia las calles.")

with st.expander("¿Cómo ayuda esto a reducir inundaciones?"):
    st.write("Al retener el agua en la azotea, se reduce la velocidad y volumen de agua que llega a las calles, ayudando a mitigar inundaciones urbanas.")

with st.expander("¿Qué beneficios adicionales tiene un jardín verde?"):
    st.write("""
    - Mejora la eficiencia energética del edificio  
    - Aumenta la biodiversidad urbana  
    - Contribuye a la calidad del aire y el microclima  
    - Embellece el entorno
    """)

# Enlaces útiles
st.markdown("""
---
### 📚 Más información

- [Artículo científico sobre azoteas verdes](https://www.sciencedirect.com/science/article/pii/S2210670717300335)  
- [Normativa local sobre gestión de aguas pluviales](https://www.epa.gov/green-infrastructure/green-roofs)  
- [Organización mundial de la salud: Gestión de aguas urbanas](https://www.who.int/water_sanitation_health/publications/urban-water-management/en/)
""")

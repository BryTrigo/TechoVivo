# 4_Acerca.py

import streamlit as st

st.set_page_config(page_title="Acerca de", layout="centered",
                   initial_sidebar_state="auto")

st.title("ℹ️ Acerca de TechoVivo")

st.markdown("""
---

### 🎯 Objetivo del proyecto

**TechoVivo** es una aplicación desarrollada como parte de un trabajo de tesis que busca analizar el impacto de los **jardines verdes en azoteas** como sistema de retención y regulación del caudal de agua de lluvia en zonas urbanas.  
Su objetivo es **demostrar cómo la implementación de estos sistemas puede disminuir el impacto del raudal en las calles** mediante simulaciones técnicas y visuales.

---

### 🧠 Autor

- **Nombre:** Bryan Trigo  
- **Rol:** Desarrollador, investigador y autor de la tesis  
- **Institución:** [Universidad Americana]  
- **Carrera:** [Facultad de Comunicación, Artes y Ciencias de la Tecnología]

---

### 🛠️ Tecnologías utilizadas

- **Python 3**  
- **Streamlit** para el desarrollo de la app  
- **Matplotlib** para visualizaciones  
- **VS Code** como entorno de desarrollo


---

### 📩 Contacto

Si querés saber más o colaborar con el proyecto:

- Email: `bryan95trigo@gmail.com`

- LinkedIn: [https://www.linkedin.com/in/braiantrigo/]

---
""")

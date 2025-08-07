# 3_comparacion.py

import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Comparación de Retención",
                   layout="centered", initial_sidebar_state="auto")

# Título de la página
st.title("🌧️ Comparativa de Retención de Agua de Lluvia")
st.markdown("""
Este módulo compara dos escenarios:
- Azotea convencional.
- Azotea verde con jardín.

La comparación estima el **volumen de agua** que llega a las calles en cada caso.
""")

# Entradas del usuario
st.header("Parámetros de Simulación")

area_azotea = st.number_input("Área de la azotea (m²)", min_value=1, value=100)
intensidad_lluvia = st.number_input(
    "Intensidad de lluvia (mm/h)", min_value=1, value=50)
duracion_lluvia = st.number_input(
    "Duración de la lluvia (horas)", min_value=1, value=1)

# Porcentaje de retención del jardín verde (supuesto)
retencion_jardin = st.slider(
    "Capacidad estimada de retención del jardín verde (%)", min_value=0, max_value=100, value=60)

# Cálculos
# Conversión: 1 mm lluvia en 1 m² = 1 litro de agua = 0.001 m³
volumen_total = area_azotea * intensidad_lluvia * duracion_lluvia * 0.001  # m³

# Sin jardín
volumen_convencional = volumen_total

# Con jardín verde
volumen_jardin = volumen_total * (1 - retencion_jardin / 100)

# Mostrar resultados
st.subheader("💧 Resultados del Análisis:")
st.write(f"**Volumen total generado por la lluvia:** {volumen_total:.2f} m³")
st.write(
    f"**Volumen que llega a la calle sin jardín:** {volumen_convencional:.2f} m³")
st.write(
    f"**Volumen que llega a la calle con jardín verde:** {volumen_jardin:.2f} m³")

# Comparación gráfica
st.subheader("📊 Comparación Gráfica")

etiquetas = ['Sin jardín', 'Con jardín verde']
valores = [volumen_convencional, volumen_jardin]

fig, ax = plt.subplots()
ax.bar(etiquetas, valores)
ax.set_ylabel('Volumen que llega a la calle (m³)')
ax.set_title('Comparación de Escorrentía')
st.pyplot(fig)

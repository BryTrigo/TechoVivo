import streamlit as st
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
import datetime
import io  # Para buffer en memoria

st.set_page_config(page_title="Exportar resultados",
                   layout="centered", initial_sidebar_state="auto")
st.title("📄 Exportar resultados a PDF")

st.markdown(
    "Generá un informe PDF con los resultados de simulación de TechoVivo.")

# --- Entradas del usuario ---
st.header("📌 Parámetros del informe")

area = st.number_input("Área de la azotea (m²)", min_value=1, value=100)
intensidad = st.number_input(
    "Intensidad de lluvia (mm/h)", min_value=1, value=50)
duracion = st.number_input(
    "Duración de la lluvia (horas)", min_value=1, value=1)
retencion = st.slider("Retención estimada del jardín verde (%)",
                      min_value=0, max_value=100, value=60)

# --- Cálculos ---
volumen_total = area * intensidad * duracion * 0.001  # m³
volumen_convencional = volumen_total
volumen_jardin = volumen_total * (1 - retencion / 100)

# --- Botón para generar PDF ---
if st.button("📥 Generar PDF"):

    buffer = io.BytesIO()  # Buffer en memoria

    # Crear el documento PDF usando el buffer en memoria
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elementos = []

    # Encabezado
    elementos.append(
        Paragraph("Informe de Simulación - TechoVivo", styles["Title"]))
    elementos.append(Spacer(1, 20))

    # Fecha y hora
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    elementos.append(
        Paragraph(f"Fecha de generación: {now}", styles["Normal"]))
    elementos.append(Spacer(1, 10))

    # Parámetros
    elementos.append(Paragraph(f"Área de azotea: {area} m²", styles["Normal"]))
    elementos.append(
        Paragraph(f"Intensidad de lluvia: {intensidad} mm/h", styles["Normal"]))
    elementos.append(
        Paragraph(f"Duración de la lluvia: {duracion} h", styles["Normal"]))
    elementos.append(
        Paragraph(f"Retención estimada del jardín: {retencion}%", styles["Normal"]))
    elementos.append(Spacer(1, 20))

    # Resultados
    elementos.append(Paragraph("Resultados:", styles["Heading2"]))
    elementos.append(Paragraph(
        f"Volumen total de agua generado: {volumen_total:.2f} m³", styles["Normal"]))
    elementos.append(Paragraph(
        f"Volumen sin jardín (escurrimiento): {volumen_convencional:.2f} m³", styles["Normal"]))
    elementos.append(Paragraph(
        f"Volumen con jardín verde (escurrimiento): {volumen_jardin:.2f} m³", styles["Normal"]))
    elementos.append(Spacer(1, 30))

    elementos.append(Paragraph(
        "Este informe fue generado automáticamente por la aplicación TechoVivo.", styles["Italic"]))

    # Generar PDF en el buffer
    doc.build(elementos)

    # Volver al inicio del buffer para lectura
    buffer.seek(0)

    # Botón para descargar el PDF directamente desde memoria
    st.download_button(
        label="📄 Descargar informe PDF",
        data=buffer,
        file_name="informe_techo_vivo.pdf",
        mime="application/pdf"
    )

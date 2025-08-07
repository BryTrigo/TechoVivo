import streamlit as st
import plotly.graph_objects as go
from fpdf import FPDF
import base64

st.set_page_config(
    page_title="TechoVivo",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="auto"
)

# --- TÍTULO Y DESCRIPCIÓN ---
st.title("🌧️ Simulación de Retención del Jardín Verde")
st.markdown("""
Esta simulación te permite calcular cuánta agua puede retener una azotea verde
durante una lluvia, en comparación con una azotea convencional.
""")

# --- ENTRADA DE PARÁMETROS ---
st.header("📥 Parámetros de entrada")

col1, col2 = st.columns(2)

with col1:
    area = st.number_input("Área de la azotea (m²)",
                           min_value=1.0, value=100.0)
    intensidad_lluvia = st.number_input(
        "Intensidad de lluvia (mm/h)", min_value=0.0, value=30.0)
    duracion_lluvia = st.number_input(
        "Duración de la lluvia (horas)", min_value=0.1, value=1.0)

with col2:
    espesor_sustrato = st.number_input(
        "Espesor del sustrato (cm)", min_value=1.0, value=10.0)
    porosidad_sustrato = st.slider(
        "Porosidad del sustrato (%)", min_value=10, max_value=100, value=45)

# --- CÁLCULOS ---
volumen_lluvia = (intensidad_lluvia * duracion_lluvia * area) / 1000
volumen_sustrato = (espesor_sustrato / 100) * area
capacidad_retencion = volumen_sustrato * (porosidad_sustrato / 100)
volumen_retenido = min(volumen_lluvia, capacidad_retencion)
volumen_excedente = max(0, volumen_lluvia - volumen_retenido)

porcentaje_retenido = (volumen_retenido / volumen_lluvia *
                       100) if volumen_lluvia > 0 else 0
porcentaje_excedente = 100 - porcentaje_retenido

# --- RESULTADOS TEXTUALES ---
st.header("📊 Resultados de la simulación")

st.markdown(f"""
- **Volumen total de lluvia caído**: `{volumen_lluvia:.2f} m³`
- **Capacidad de retención del jardín verde**: `{capacidad_retencion:.2f} m³`
- **Volumen de agua retenido**: `{volumen_retenido:.2f} m³` ({porcentaje_retenido:.1f}%)
- **Volumen que escapa a la calle**: `{volumen_excedente:.2f} m³` ({porcentaje_excedente:.1f}%)
""")

if volumen_excedente <= 0:
    st.success("✅ El jardín verde retiene toda el agua de esta lluvia.")
else:
    st.warning("⚠️ El jardín verde no retiene toda el agua: hay excedente.")

# --- GRÁFICAS ---
st.subheader("📉 Comparación de volúmenes (m³)")

fig = go.Figure(data=[
    go.Bar(name='Volumen total de lluvia', x=['Lluvia'], y=[
           volumen_lluvia], marker_color='blue'),
    go.Bar(name='Volumen retenido', x=['Lluvia'], y=[
           volumen_retenido], marker_color='green'),
    go.Bar(name='Volumen que escapa', x=['Lluvia'], y=[
           volumen_excedente], marker_color='red')
])
fig.update_layout(barmode='group', yaxis_title='Volumen (m³)',
                  xaxis_title='Evento de lluvia')
st.plotly_chart(fig)

st.subheader("📎 Porcentaje de distribución del agua")
fig_pie = go.Figure(data=[
    go.Pie(
        labels=['Retenido', 'Escapa'],
        values=[volumen_retenido, volumen_excedente],
        hole=0.4,
        marker=dict(colors=['green', 'red']),
    )
])
fig_pie.update_layout(showlegend=True)
st.plotly_chart(fig_pie)

# --- GENERAR PDF ---


def generar_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, "Reporte de Simulación TechoVivo", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("Arial", '', 12)
    pdf.cell(0, 10, f"Área de la azotea: {area} m²", ln=True)
    pdf.cell(0, 10, f"Intensidad de lluvia: {intensidad_lluvia} mm/h", ln=True)
    pdf.cell(0, 10, f"Duración de la lluvia: {duracion_lluvia} horas", ln=True)
    pdf.cell(0, 10, f"Espesor del sustrato: {espesor_sustrato} cm", ln=True)
    pdf.cell(0, 10, f"Porosidad del sustrato: {porosidad_sustrato} %", ln=True)
    pdf.ln(10)

    pdf.cell(0, 10, "Resultados:", ln=True)
    pdf.cell(
        0, 10, f"Volumen total de lluvia: {volumen_lluvia:.2f} m³", ln=True)
    pdf.cell(
        0, 10, f"Capacidad de retención del jardín verde: {capacidad_retencion:.2f} m³", ln=True)
    pdf.cell(
        0, 10, f"Volumen de agua retenido: {volumen_retenido:.2f} m³ ({porcentaje_retenido:.1f}%)", ln=True)
    pdf.cell(
        0, 10, f"Volumen que escapa a la calle: {volumen_excedente:.2f} m³ ({porcentaje_excedente:.1f}%)", ln=True)

    # Guardar el PDF en un buffer
    return pdf.output(dest='S').encode('latin1')


# Botón para descargar PDF
pdf_data = generar_pdf()
b64 = base64.b64encode(pdf_data).decode()

href = f'<a href="data:application/octet-stream;base64,{b64}" download="Reporte_TechoVivo.pdf">📥 Descargar reporte PDF</a>'
st.markdown(href, unsafe_allow_html=True)

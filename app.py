import streamlit as st
import pandas as pd
import plotly_express as px

wine_data = pd.read_csv('wine_qt.csv')

st.title("Análisis: Calidad del vino")
st.write("Visualizaciones básicas del dataset de vinos.")
st.image("ChatGPT_wineqt.png", caption="image1.wine", use_container_width=True)

# Histogram of quality
st.header("Distribución de la calidad del vino")
hist_button = st.button('Construir histograma')
if hist_button:
    st.write("Histograma creado")
    fig1 = px.histogram(wine_data, x="quality", nbins=10,
                        color_discrete_sequence=["#EC90EC"], title="Fig1: Calidad del vino")
    st.plotly_chart(fig1, use_container_width=True)

# Crear casillas de verificación para los gráficos de dispersión
build_scatter1 = st.checkbox(
    'Construir gráfico de dispersión: Alcohol vs Calidad')
build_scatter2 = st.checkbox(
    'Construir gráfico de dispersión: Acidez Volátil vs Calidad')
# Scatter: alcohol vs quality
if build_scatter1:
    st.write("Relación entre Alcohol y Calidad")
    fig2 = px.scatter(wine_data, x="alcohol", y="quality", trendline="ols",
                      title="Fig2: Los vinos con mayor graduación alcohólica tienden a ser evaluados con mayor calidad.")
    st.plotly_chart(fig2, use_container_width=True)

# Scatter: volatile acidity vs quality
if build_scatter2:
    st.write("Relación entre Acidez Volátil y Calidad")
    fig3 = px.scatter(wine_data, x="volatile acidity", y="quality", trendline="ols",
                      title="Fig3: A mayor acidez volátil, menor calidad")
    st.plotly_chart(fig3, use_container_width=True)

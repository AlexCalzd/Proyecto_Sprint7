import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
df = pd.read_csv("vehicles_us.csv")

st.header("Dashboard: Análisis de anuncios de coches")

if st.button("Mostrar histograma de odómetro"):
    st.write("Histograma de la columna 'odometer'")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if st.button("Mostrar gráfico de dispersión año vs precio"):
    st.write("Gráfico de dispersión entre 'model_year' y 'price'")
    
    # Eliminar filas con datos faltantes para evitar errores en el gráfico
    df_filtered = df.dropna(subset=["model_year", "price"])
    
    fig = px.scatter(df_filtered, x="model_year", y="price",
                     labels={"model_year": "Año del modelo", "price": "Precio"},
                     title="Precio vs Año del modelo")
    st.plotly_chart(fig, use_container_width=True)
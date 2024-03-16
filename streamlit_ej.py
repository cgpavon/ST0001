import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Función para generar datos aleatorios
def generar_datos(num_filas):
    datos = np.random.normal(loc=50, scale=10, size=num_filas)
    return datos

# Título de la aplicación
st.title("Análisis de Datos")

# Sección para generar datos
st.header("Generar Datos")
num_filas = st.slider("Selecciona el número de filas", 10, 1000, 100)
datos = generar_datos(num_filas)

# Mostrar los datos generados
st.subheader("Datos Generados")
df = pd.DataFrame(datos, columns=['Valor'])
st.write(df)

# Cálculos estadísticos
st.header("Cálculos Estadísticos")
media = np.mean(datos)
st.write(f"Media: {media:.2f}")

mediana = np.median(datos)
st.write(f"Mediana: {mediana:.2f}")

desviacion_std = np.std(datos)
st.write(f"Desviación Estándar: {desviacion_std:.2f}")

# Visualización de tendencia
st.header("Tendencia")
fig, ax = plt.subplots()
ax.plot(datos)
ax.set_title("Tendencia de los Datos")
ax.set_xlabel("Índice")
ax.set_ylabel("Valor")
st.pyplot(fig)
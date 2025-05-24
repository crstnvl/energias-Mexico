import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos ya unidos
df = pd.read_csv('C:/Users/HyA/Desktop/Projects/Energias Renovables/energia_total_y_renovables_mexico.csv')

# Asegúrate de que estos nombres coincidan con tu CSV:
columnas_renovables = ['Hidroelectrica', 'Eolica', 'Solar', 'Geotermica', 'Biomasa', 'Maremotriz']

# Calcula la suma total de renovables si no existe
if 'Total_Renovables' not in df.columns:
    df['Total_Renovables'] = df[columnas_renovables].sum(axis=1)

st.title("Dashboard: Energía Renovable en México")
st.subheader("Datos históricos y comparación (2000-2023)")

# Selección de variables
opciones = [col for col in df.columns if col not in ['Año']]  # evita duplicar año
seleccion = st.multiselect(
    'Selecciona las energías a mostrar (puedes elegir varias):',
    opciones,
    default=['Total_Energia_Electrica_GWh', 'Total_Renovables']
)

# Filtrar por año
año_min, año_max = int(df["Año"].min()), int(df["Año"].max())
rango = st.slider('Rango de años:', año_min, año_max, (año_min, año_max), 1)
df_filtro = df[(df['Año'] >= rango[0]) & (df['Año'] <= rango[1])]

# Gráfica
fig, ax = plt.subplots(figsize=(12,7))
for col in seleccion:
    ax.plot(df_filtro['Año'], df_filtro[col], marker='o', label=col)
ax.set_xlabel("Año")
ax.set_ylabel("GWh")
ax.set_title("Evolución histórica de energías (selección)")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Mostrar tabla
if st.checkbox("Mostrar tabla de datos"):
    st.dataframe(df_filtro)

st.info("Puedes seleccionar y comparar energías renovables individuales, el total nacional o la suma de renovables. Ideal para visualizar tendencias y crecimiento.")

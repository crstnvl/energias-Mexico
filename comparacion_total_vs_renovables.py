import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. Leer los datos de energía total
df_total = pd.read_csv('C:/Users/HyA/Desktop/Projects/Energias Renovables/energia_total_mexico.csv', encoding='latin-1')

# 2. Leer los datos de energías renovables
df_ren = pd.read_csv('C:/Users/HyA/Desktop/Projects/Energias Renovables/energias_renovables_mexico.csv', encoding='latin-1')

# 3. Limpiar nombres de columnas y tipos
df_total.columns = df_total.columns.str.strip()
df_ren.columns = df_ren.columns.str.strip()

# Forzar tipo de dato correcto para merge
df_total['Año'] = df_total['Año'].astype(int)
df_ren['Año'] = df_ren['Año'].astype(int)

print("df_total columnas:", df_total.columns.tolist())
print("df_ren columnas:", df_ren.columns.tolist())

# 4. Graficar cada energía renovable individualmente
plt.figure(figsize=(12,7))
for col in df_ren.columns[1:]:
    plt.plot(df_ren['Año'], df_ren[col], marker='o', label=col)
plt.title('Generación de Energía Renovable por Fuente en México (GWh)')
plt.xlabel('Año')
plt.ylabel('GWh')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('renovables_mexico.png')
plt.show()

# 5. Unir ambos dataframes por Año
df_merged = pd.merge(df_total, df_ren, on='Año')

# 6. Verifica los nombres de columnas renovables para el cálculo
# Puedes imprimirlos así para ver:
print("df_merged columnas:", df_merged.columns.tolist())

# En tu archivo, asegúrate de que los nombres de las columnas sean exactamente:
# ['Hidroeléctrica', 'Eólica', 'Solar', 'Geotérmica', 'Biomasa', 'Maremotriz']
# Si tienes versiones sin acento, ajusta aquí:
columnas_renovables = ['Hidroelectrica', 'Eolica', 'Solar', 'Geotermica', 'Biomasa', 'Maremotriz']

# 7. Porcentaje de renovables vs total
df_merged['Renovable_vs_Total_%'] = (
    df_merged[columnas_renovables].sum(axis=1)
    / df_merged['Total_Energia_Electrica_GWh'] * 100
)

# 8. Graficar el porcentaje
plt.figure(figsize=(10,6))
plt.plot(df_merged['Año'], df_merged['Renovable_vs_Total_%'], marker='o', color='green')
plt.title('Participación de Energías Renovables en el Total de Generación Eléctrica (%)')
plt.xlabel('Año')
plt.ylabel('Porcentaje (%)')
plt.grid(True)
plt.tight_layout()
plt.savefig('porcentaje_renovables.png')
plt.show()

# 9. Opcional: Guardar el dataframe combinado
df_merged.to_csv('C:/Users/HyA/Desktop/Projects/Energias Renovables/energia_total_y_renovables_mexico.csv', index=False, encoding='utf-8')

print("¡Listo! Se han generado las gráficas y el archivo combinado.")

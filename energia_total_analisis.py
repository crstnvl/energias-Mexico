import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# Leer los datos
df = pd.read_csv('C:/Users/HyA/Desktop/Projects/Energias Renovables/energia_total_mexico.csv')

# Variables
X = df[['Año']].values
y = df['Total_Energia_Electrica_GWh'].values

# Modelo de regresión lineal
model = LinearRegression()
model.fit(X, y)

# Predicción para los próximos 5 años
future_years = np.arange(df['Año'].max() + 1, df['Año'].max() + 6).reshape(-1, 1)
future_preds = model.predict(future_years)

# Visualización
plt.figure(figsize=(10, 6))
plt.plot(df['Año'], y, marker='o', label='Histórico')
plt.plot(future_years, future_preds, marker='*', linestyle='--', color='red', label='Predicción')
plt.title('Generación Total de Energía Eléctrica en México (GWh)')
plt.xlabel('Año')
plt.ylabel('GWh')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('energia_total_prediccion.png')
plt.show()

# Imprimir predicciones numéricas
print("Predicción de generación total de energía eléctrica para los próximos 5 años (GWh):")
for year, pred in zip(future_years.flatten(), future_preds):
    print(f"{year}: {int(pred):,} GWh")

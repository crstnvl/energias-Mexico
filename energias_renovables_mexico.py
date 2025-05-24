import pandas as pd
import matplotlib.pyplot as plt

# Leer el archivo renovables
df_ren = pd.read_csv('C:/Users/HyA/Desktop/Projects/Energias Renovables/energias_renovables_mexico.csv', encoding='latin-1')

print(df_ren.columns.tolist())

# Graficar cada energía renovable
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

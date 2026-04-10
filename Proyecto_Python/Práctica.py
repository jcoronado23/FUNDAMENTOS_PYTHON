#pip install pandas

import pandas as pd

# Crear datos de ejemplo
data = {
    "Nombre": ["Carlos", "Ana", "Luis"],
    "Edad": [25, 30, 22],
    "Ciudad": ["San José", "Alajuela", "Cartago"]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Mostrar los datos
print("Datos del DataFrame:")
print(df)

# Mostrar promedio de edad
print("\nPromedio de edad:")
print(df["Edad"].mean())
sintomas = df.explode("sintomas")
print(sintomas["sintomas"].value_counts())
# Esto nos dará una idea de cuáles son los síntomas más comunes entre los pacientes.
# Y tabién reemplazara mi counters por un dataframe que es más fácil de manejar.
# Fase 5 — Ejercicio 5.1
# Define clasificar_nota(nota) y reporte_salon(lista_notas).

notas_ejemplo = ["Ana Pérez",
"Carlos Mora",
"María González",
"Luis Jiménez",
"Sofía Rojas",
"Diego Castro",
"Valentina Herrera",
"Andrés Vargas",
"Camila Núñez",
"Roberto Alvarado",
"Patricia Solís",
"Fernando Quesada",
"Laura Méndez",
"Esteban Brenes",
"Daniela Ureña"]
notas = [92, 78, 65, 88, 55, 73, 96, 82, 47, 61, 85, 70, 93, 58, 79]
suma = 0
aprobados = 0
reprobados = 0
lista = 0
def clasificar_nota(nota):
    """Retorna la categoría de la nota."""
    if nota >= 90:
        return "Excelente"
    elif nota >= 75:
        return "Bueno"
    elif nota >= 60:
        return "Suficiente"
    else:
        return "Reprobado"
    
# Usar la 8}función con varias notas

for  nota in notas:
    categoria = clasificar_nota(nota)
    print(f":{nota} → {categoria}")
    

# Úsalas con el archivo notas_ejemplo.csv.

#Respuesta
print("=================================")
print("       REPORTE DEL SALÓN 📔      ")
print("=================================")

for nota in notas:
    suma += nota
    if nota >= 70:
        aprobados += 1
    else:
        reprobados += 1
promedio = suma / len(notas)
notas.sort(reverse=True)

print(f"\nPromedio del salón: {promedio}")
print(f"Estudiantes aprobados: {aprobados}")
print(f"Estudiantes reprobados: {reprobados}")

#Notas mas altas y mas bajas
print("\nNotas mas altas ➕ y mas bajas ➖")
nota_alta = (max(notas))
nota_baja = (min(notas))
print(f"\nNota mas alta: {nota_alta}")
print(f"nota mas baja: {nota_baja}")
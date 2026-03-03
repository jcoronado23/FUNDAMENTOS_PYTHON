# Fase 5 — Ejercicio 5.1

notas_ejemplo = [
"Ana Pérez",
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
"Daniela Ureña"
]

notas = [92, 78, 65, 88, 55, 73, 96, 82, 47, 61, 85, 70, 93, 58, 79]


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


def reporte_salon(lista_notas):
    """Genera el reporte del salón."""
    suma = 0
    aprobados = 0
    reprobados = 0

    for nota in lista_notas:
        suma += nota
        if nota >= 70:
            aprobados += 1
        else:
            reprobados += 1

    promedio = suma / len(lista_notas)

    print("=================================")
    print("       REPORTE DEL SALÓN 📔      ")
    print("=================================")

    print(f"\nPromedio del salón: {promedio:.2f}")
    print(f"Estudiantes aprobados: {aprobados}")
    print(f"Estudiantes reprobados: {reprobados}")

    print("\nNotas más altas ➕ y más bajas ➖")
    print(f"Nota más alta: {max(lista_notas)}")
    print(f"Nota más baja: {min(lista_notas)}")


# Mostrar clasificación individual
print("CLASIFICACIÓN INDIVIDUAL")
for nota in notas:
    categoria = clasificar_nota(nota)
    print(f"{nota} → {categoria}")

print("\n")

# Llamar función reporte
reporte_salon(notas)
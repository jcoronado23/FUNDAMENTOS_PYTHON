import matplotlib.pyplot as plt
import pandas as pd

# Cargar datos de archivo clinica_s08_avanzado.json
data = pd.read_json('clinica_s08_avanzado.json')
# Limpiar pantalla de la consola
import os
os.system('cls' if os.name == 'nt' else 'clear')

# 1 Función para mostrar información de paciente por carnet
def mostrar_paciente():
    carnet = int(input("Ingrese el número de carnet del paciente: "))
    paciente = data[data['carnet'] == carnet]
    if not paciente.empty:
        print(paciente.to_string(index=False))
    else:
        print("Paciente no encontrado.")
    input("Presione Enter para continuar...")
    
# 2 Función para gráfica de barras de pacientes por género
# Agregar cantidad de pacientes por género en barras y mostrar el número encima de cada barra
def grafica_barras_genero():
    genero_counts = data['genero'].value_counts()
    genero_counts.plot(kind='bar')
    plt.title('Número de pacientes por género')
    plt.xlabel('Género')
    plt.ylabel('Número de pacientes')
    plt.xticks(rotation=0)
    for i, v in enumerate(genero_counts):
        plt.text(i, v + 0.5, str(v), ha='center', va='bottom')
    plt.show()
    input("Presione Enter para continuar...")
    
# 3 Función para gráfica de pastel de pacientes por edad
def grafica_pastel_edad():
    # Rangos de edad
    edad_bins = [0, 18, 30, 50, 100]
    edad_labels = ['0-17', '18-29', '30-49', '50+']
    
    # Crear grupos
    data['edad_grupo'] = pd.cut(data['edad'], bins=edad_bins, labels=edad_labels, right=False)
    # Contar pacientes por grupo 
    edad_counts = data['edad_grupo'].value_counts().sort_index()
    # Eliminar espacios vacíos
    edad_counts = edad_counts[edad_counts > 0]
    # Tamaño de la figura
    plt.figure(figsize=(8, 6))
    # Grafica de pastel
    plt.pie(edad_counts, labels=edad_counts.index, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'white'}, pctdistance=0.7)
    # Título
    
    plt.title('Distribución de pacientes por grupo de edad')
    # Ajustar diseño
    plt.tight_layout()
    # Mostrar gráfica
    plt.show()
    input("Presione Enter para continuar...")
    
# 4 Función para gráfica de barras horizontales de enfermedades más comunes por edad
def grafica_barras_horizontales_enfermedades_edad():
    # Top 5 enfermedades más comunes
    top_enfermedades = data['enfermedad'].value_counts().head(5).index

    # Filtrar datos para las enfermedades seleccionadas
    datos_filtrados = data[data['enfermedad'].isin(top_enfermedades)]

    # Crear tabla de contingencia
    tabla = pd.crosstab(datos_filtrados['edad'], datos_filtrados['enfermedad'])

    # Crear gráfico de barras horizontales
    tabla.plot(kind='barh', stacked=True, figsize=(10, 6))
    plt.title('Distribución de enfermedades por edad')
    plt.xlabel('Número de pacientes')
    plt.ylabel('Edad')
    plt.legend(title='Enfermedades', bbox_to_anchor=(1.02, 1), loc='upper left')
    plt.tight_layout()
    plt.show()
    input("Presione Enter para continuar...")

# 5 Función para gráfica de barras de enfermedades más comunes top 10
def grafica_barras_enfermedades_top10():
    enfermedades_counts = data['enfermedad'].explode().value_counts().head(10)
    enfermedades_counts.plot(kind='bar')
    plt.title('Top 10 enfermedades más comunes')
    plt.xlabel('Enfermedades')
    plt.ylabel('Número de pacientes')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    input("Presione Enter para continuar...")

# Crear menú de opciones
def menu():
    # Limpiar pantalla de la consola
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Seleccione una opción:")
    
    print("1. Mostrar información de paciente por carnet")
    print("2. Gráfica de barras de pacientes por género")
    print("3. Gráfica de pastel de pacientes por edad 1 a 100 años")
    print("4. Gráfica de Barras horizontales de enfermedades más comunes por edad")
    print("5. Gráfica de barras de enfermedades más comunes top 10")
    print("6. Salir")
    opcion = input("Ingrese el número de la opción: ")
    return opcion

# Bucle principal del programa
while True:
    opcion = menu()
    if opcion == '1':
        mostrar_paciente()
    elif opcion == '2':
        grafica_barras_genero()
    elif opcion == '3':
        grafica_pastel_edad()
    elif opcion == '4':
        grafica_barras_horizontales_enfermedades_edad()
    elif opcion == '5':
        grafica_barras_enfermedades_top10()
    elif opcion == '6':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, intente de nuevo.")
        

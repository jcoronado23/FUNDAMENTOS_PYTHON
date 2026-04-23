import os
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')
from contexto import resumen


# Cargar datos desde el archivo CSV
df = pd.read_csv('Vehículos_Eléctricos.csv')

# Normalizar nombres de columnas por si vienen con espacios
df.columns = df.columns.str.strip()

data = df

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu():
    global data
    
    while True:
        limpiar_pantalla()
        print("=====================================================")
        print("Sistema de Análisis de Problemas en Vehículos Eléctricos ⚡")
        print("=====================================================")
        print('♾️')
        print('-' * 130)
        print("Información💭")
        print(resumen)
        print('-' * 130)
        
        print("\nSeleccione una opción del menú para continuar🔜\n")
        print("1. Buscar problema por número de serie.")
        print("2. Ver modelos y años de una marca a escoger.")
        print("3. Gráfica de barras de reportes por marca top(10) y otros📊.")
        print("4. Registrar vehículo nuevo👤.")
        print("5. Salir del programa.")

        opcion = input("\nIngrese el número de la opción que desea ejecutar: ")
            
        if opcion == '1':
            numero_id = input("Ingrese el número de identificación del vehículo: ").strip()

            resultado = data[data['id_documento'].astype(str) == numero_id]

            if not resultado.empty:
                print("\nInformación del vehículo encontrado:\n")
                print(resultado[['id_documento', 'marca', 'modelo', 'año_modelo', 'problemas']].to_string(index=False))
            else:
                print("\nNo se encontró ningún vehículo con ese número de identificación.")

        elif opcion == '2':
            marca = input("Ingrese la marca del vehículo: ").strip()

            resultado = data[data['marca'].str.lower() == marca.lower()]
            if not resultado.empty:
                print(f"\nModelos y años de la marca {marca}:\n")
                print(resultado[['modelo', 'año_modelo']].to_string(index=False))
            else:
                print("\nNo se encontraron vehículos de esa marca.")

        elif opcion == '3':
            conteo_marcas = data['marca'].value_counts()
            top_marcas = conteo_marcas.head(10)
            otras_marcas = conteo_marcas[10:].sum()

            plt.figure(figsize=(12, 6))
            top_marcas.plot(kind='bar', color='skyblue')
            if otras_marcas > 0:
                plt.bar('Otras', otras_marcas, color='lightcoral')
            plt.title('Cantidad de reportes por marca (Top 10 y otras)')
            plt.xlabel('Marca\nAutos Eléctricos y otras')
            plt.ylabel('Cantidad de reportes')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            plt.show()
            
        elif opcion == '4':
    
            while True:
                print("\n=== Registro de nuevo vehículo ===")

                # Validar ID
                while True:
                    id_documento = input("Ingrese el número de identificación: ").strip()
                    if id_documento == "":
                        print("⚠️ Este campo no puede estar vacío.")
                    else:
                        existe = data[data['id_documento'].astype(str) == id_documento]
                        if not existe.empty:
                            print("⚠️ Ya existe un vehículo con ese ID.")
                        else:
                            break

                # Validar marca
                while True:
                    marca = input("Ingrese la marca: ").strip()
                    if marca == "":
                        print("⚠️ Este campo no puede estar vacío.")
                    else:
                        break

                # Validar modelo
                while True:
                    modelo = input("Ingrese el modelo: ").strip()
                    if modelo == "":
                        print("⚠️ Este campo no puede estar vacío.")
                    else:
                        break

                # Validar año (numérico y rango)
                while True:
                    año_modelo = input("Ingrese el año del vehículo: ").strip()
            
                    if not año_modelo.isdigit():
                        print("⚠️ El año debe ser un número.")
                    else:
                        año_modelo = int(año_modelo)
                
                        if 1886 <= año_modelo <= 2026:
                            break
                        else:
                            print("⚠️ Año fuera de rango válido (1886 - 2026).")

                # Validar problemas
                while True:
                    problemas = input("Ingrese el problema reportado: ").strip()
                    if problemas == "":
                        print("⚠️ Este campo no puede estar vacío.")
                    else:
                        break

                # Crear nuevo registro
                nuevo_vehiculo = pd.DataFrame([{
                    'id_documento': id_documento,
                    'marca': marca,
                    'modelo': modelo,
                    'año_modelo': año_modelo,
                    'problemas': problemas
                }])

                # Agregar al dataset
                data = pd.concat([data, nuevo_vehiculo], ignore_index=True)

                # Guardar en CSV
                data.to_csv('Vehículos_Eléctricos.csv', index=False, encoding='utf-8-sig')

                print("\n✅ Vehículo registrado correctamente.")

                # Preguntar si desea continuar
                continuar = input("\n¿Desea registrar otro vehículo? (s/n): ").strip().lower()
                if continuar != 's':
                    break
        elif opcion == '5':
            print("\nGracias por usar el sistema de Reportes de Autos Electricos. ¡Hasta luego!")
            break
        
        else:
            print("\nOpción no válida. Por favor, ingrese un número del 1 al 5.")

        input("\nPresione Enter para devolver al menú principal... 🔚")

if __name__ == "__main__":
    mostrar_menu()
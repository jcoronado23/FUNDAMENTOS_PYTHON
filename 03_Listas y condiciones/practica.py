Biblioteca = {
    "libro1": {
        "titulo": "Cien años de soledad",
        "autor": "Gabriel García Márquez",
        "año": 1967
    },
    "libro2": {
        "titulo": "1984",
        "autor": "George Orwell",
        "año": 1948

    },
    "libro3": {
        "titulo": "El gran Gatsby",
        "autor": "F. Scott Fitzgerald",
        "año": 1925
    }

}
# imprimir solo libro1
for libro in Biblioteca:
    print('Libros para inspirar tú vida.📖👨‍💻\n')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(f'Título: {Biblioteca[libro]['titulo']}')
    print(f'Autor: {Biblioteca[libro]['autor']}')
    print(f'Año: {Biblioteca[libro]['año']}')
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')
print('Fin mi amigo, que tengas una buena noche.⭐')
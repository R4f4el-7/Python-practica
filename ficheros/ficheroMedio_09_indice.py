'''Enunciado
Escribe un programa que lea un fichero datos.txt y cree un índice de todas las palabras del fichero, indicando en qué líneas aparece cada una.

Instrucciones:

Lee todas las líneas del fichero.
Usa un diccionario donde las claves sean las palabras y los valores sean listas con los números de línea.
Muestra el índice en pantalla.'''

diccPalabras = {}

with open("data.txt", "r") as f:
    lineas = f.readlines()

for cont_linea, linea in enumerate(lineas, start=1):
    palabras = linea.split()
    for p in palabras:
        # Convertir a minúsculas para uniformidad
        palabra = p.lower()
        # Si la palabra no existe, inicializamos la lista
        if palabra not in diccPalabras:
            diccPalabras[palabra] = []
        # Añadimos el número de línea
        diccPalabras[palabra].append(cont_linea)

# Mostrar el índice ordenado alfabéticamente
for palabra, lineas in sorted(diccPalabras.items()):
    print(f"{palabra}: {lineas}")
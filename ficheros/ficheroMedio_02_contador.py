'''Crea un programa que lea un fichero datos.txt y muestre la frecuencia de cada palabra en el archivo.

Instrucciones:

Abre el fichero y lee su contenido.
Usa split() para dividir el texto en palabras.
Usa un diccionario para almacenar las palabras como claves y la frecuencia como valores.
Muestra cada palabra junto con su número de apariciones.'''
dicc = {}

with open("data.txt", "r") as f:
    palabras = f.read().split()

for p in palabras:
    if p in dicc:
        dicc[p] += 1
    else:
        dicc[p] = 1

for palabra, frecuencia in dicc.items():
    print(palabra, ":", frecuencia)

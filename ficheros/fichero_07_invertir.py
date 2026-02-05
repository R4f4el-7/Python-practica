'''Crea un programa que lea un fichero datos.txt e invierta el orden de sus líneas, guardando el resultado en un nuevo fichero invertido.txt.

Instrucciones:

Usa readlines() para leer todas las líneas.
Invierte el orden de la lista de líneas.
Escribe las líneas invertidas en el nuevo fichero.'''
with open("data.txt", "r") as fichero:
    lineas = fichero.readlines()

with open("invertido.txt", "w") as invertido:
    for linea in reversed(lineas):
        invertido.write(linea)
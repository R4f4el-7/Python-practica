'''Escribe un programa que abra un fichero datos.txt y cuente cuántas líneas tiene el archivo.

Instrucciones:

Usa readlines() para obtener una lista de líneas.
Usa la función len() para contar las líneas.
Muestra el número de líneas en pantalla.'''
try:
    with open("data.txt") as f:
        print(len(f.readlines()))
    f = open("data.txt")
    print(len(f.readlines()))
except:
    print("No fichero")
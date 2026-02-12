'''Enunciado
Crea un programa que lea las líneas de un fichero datos.txt, las ordene alfabéticamente y guarde el resultado en un nuevo fichero ordenado.txt.

Instrucciones:

Lee todas las líneas del fichero.
Usa la función sorted() para ordenar las líneas alfabéticamente.
Guarda las líneas ordenadas en un nuevo fichero.'''
with open("data.txt","r") as f:
    lineas = f.readlines()

lineas_ordenadas = sorted(lineas)

with open("ordenado.txt","w") as f:
    f.writelines(lineas_ordenadas)
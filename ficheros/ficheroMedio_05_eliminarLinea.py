'''Enunciado
Escribe un programa que lea un fichero datos.txt, elimine las líneas vacías y guarde el resultado en un nuevo fichero sin_lineas_vacias.txt.

Instrucciones:

Abre el fichero y lee todas las líneas.
Filtra las líneas vacías o que contengan solo espacios en blanco.
Escribe las líneas no vacías en un nuevo fichero.'''

with open("data.txt","r") as f:
    lineas = f.readlines()

with open("sin_lineas_vacias.txt", "w") as fichero_sin_vacias:
    for linea in lineas:
        if linea.strip():  # Si la línea no está vacía
            fichero_sin_vacias.write(linea)
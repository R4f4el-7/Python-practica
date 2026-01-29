'''Escribe un programa que abra un fichero datos.txt y 
permita al usuario añadir nuevas líneas de texto al final.

Instrucciones:

Usa open() en modo agregar (‘a’).
Solicita al usuario las líneas a añadir.
Escribe cada línea en el fichero.
Cierra el fichero.'''
try:
    cantidadInput = input("Cantidad de lineas: ")
    for num in range(int(cantidadInput)):
        lineaInput = input(f'linea {num}: ')
        with open("data.txt", "a") as f:
            f.write(lineaInput+"\n")

    #open and read the file after the appending:
    with open("data.txt") as f:
        print(f.read())
except:
    print("Fichero no existe")
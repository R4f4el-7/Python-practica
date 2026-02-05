'''Escribe un programa que abra un fichero datos.txt y 
permita al usuario añadir nuevas líneas de texto al final.

Instrucciones:

Usa open() en modo agregar (‘a’).
Solicita al usuario las líneas a añadir.
Escribe cada línea en el fichero.
Cierra el fichero.'''
try:
    with open("data.txt", "a") as fichero:
        while True:
            linea = input("Añade una nueva línea (o 'fin' para terminar): ")
            if linea.lower() == "fin":
                break
            fichero.write(linea + "\n")
except:
    print("Fichero no existe")
'''Escribe un programa que lea un fichero datos.txt y 
muestre solo las líneas que contienen una palabra clave proporcionada por el usuario.

Instrucciones:

Solicita al usuario una palabra clave.
Lee el fichero línea por línea.
Muestra solo las líneas que contienen la palabra clave.'''

palabraInput = input("Palabra: ")

with open("data.txt","r") as f:
    lineas = f.readlines()

for l in lineas:
    if(palabraInput in l):
        print(l)
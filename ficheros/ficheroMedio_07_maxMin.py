'''Enunciado
Escribe un programa que lea un fichero datos.txt y muestre las líneas más largas y más cortas en términos de caracteres.

Instrucciones:

Lee todas las líneas del fichero.
Usa max() y min() con la función key=len para encontrar las líneas más largas y más cortas.
Muestra ambas líneas en la consola.'''

with open("data.txt","r") as f:
    lineas = f.readlines()

maximo = max(lineas, key=len)
minimo = min(lineas, key=len)

print(maximo)
print(minimo)
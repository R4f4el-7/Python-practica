'''Enunciado
Crea un programa que lea dos ficheros datos1.txt y datos2.txt 
 compare sus líneas. Si encuentra líneas diferentes, muestra cuáles son y en qué posición se encuentran.

Instrucciones:

Abre y lee ambos ficheros.
Compara las líneas una por una.
Muestra las diferencias encontradas'''

with open("data.txt","r") as f:
    lineas1 = f.readlines()
with open("dataNueva.txt","r") as f:
    lineas2 = f.readlines()

# Determinar el número máximo de líneas entre ambos archivos
num_lineas = max(len(lineas1), len(lineas2))

for i in range(num_lineas):
    # Obtener la línea de cada archivo o cadena vacía si no existe
    l1 = lineas1[i].rstrip("\n") if i < len(lineas1) else ""
    l2 = lineas2[i].rstrip("\n") if i < len(lineas2) else ""

    if l1 != l2:
        print(f"Línea {i+1} diferente:")
        print(f"  archivo 1: {l1}")
        print(f"  archivo 2: {l2}")
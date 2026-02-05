'''Crea un programa que lea un archivo CSV llamado notas.csv y 
calcule el promedio de las notas que se encuentran en la columna “Nota”.'''
import csv
total_notas = 0
cantidad = 0
with open("notas.csv","r") as f:
    lector = csv.DictReader(f)
    for linea in lector:
        print(linea)
        total_notas += int(linea["Nota"])
        cantidad += 1
print(f'Promedio: {total_notas/cantidad}')
'''Escribe un programa que lea un archivo CSV llamado datos.csv 
y muestre todo su contenido en la consola, fila por fila.'''
import csv

with open("datos.csv","r") as f:
    for linea in f:
        print(linea.strip())
        
with open("datos.csv","r") as f:
    lector = csv.DictReader(f)
    for linea in lector:
        print(linea)
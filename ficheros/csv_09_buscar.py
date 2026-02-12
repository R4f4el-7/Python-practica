'''Enunciado
Escribe un programa que lea un archivo CSV llamado clientes.csv y
 busque un cliente específico por su nombre, mostrando todos los detalles de dicho cliente.'''
import csv
with open("estudiantes.csv","r") as f:
    for linea in f:
        
        print(linea.strip())
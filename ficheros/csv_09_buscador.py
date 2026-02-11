'''Enunciado
Escribe un programa que lea un archivo CSV llamado clientes.csv 
y busque un cliente específico por su nombre, mostrando todos los detalles de dicho cliente.'''
import csv
nombreCliente = input("Nombre cliente: ")
with open("clientes.csv","r") as f:
    lector = csv.DictReader(f)
    for l in lector:
        if(l['Nombre'] == nombreCliente):
            print(l)
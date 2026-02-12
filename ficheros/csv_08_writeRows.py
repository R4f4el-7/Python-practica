'''Enunciado
Crea un programa que escriba varios registros de estudiantes en un archivo CSV llamado estudiantes.csv utilizando csv.DictWriter().

estudiantes.csv

Nombre,Edad,Grado
Juan,20,A
Ana,22,B
Luis,21,A''' 
import csv
estudiantes = [
    {"Nombre": "Juan", "Edad": 20, "Grado": "A"},
    {"Nombre": "Ana", "Edad": 22, "Grado": "B"},
    {"Nombre": "Luis", "Edad": 21, "Grado": "A"}
]
with open("estudiantes.csv","w",newline="") as f:  
    escritor = csv.DictWriter(f,fieldnames=["Nombre","Edad","Grado"])
    
    escritor.writeheader()
    escritor.writerows(estudiantes)  
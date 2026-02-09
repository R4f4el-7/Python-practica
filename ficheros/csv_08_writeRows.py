'''Enunciado
Crea un programa que escriba varios registros de estudiantes en un archivo CSV llamado estudiantes.csv utilizando csv.DictWriter().

estudiantes.csv

Nombre,Edad,Grado
Juan,20,A
Ana,22,B
Luis,21,A'''
import csv
estudiantes = [
    {"Nombre":"nombre1","Edad":"1","Grado":"a"},
    {"Nombre":"nombre2","Edad":"2","Grado":"b"},
    {"Nombre":"nombre3","Edad":"3","Grado":"c"}
]
with open("estudiantes.csv","a",newline="") as f:
    escritor = csv.DictWriter(f,fieldnames=["Nombre","Edad","Grado"])
    escritor.writerows(estudiantes)
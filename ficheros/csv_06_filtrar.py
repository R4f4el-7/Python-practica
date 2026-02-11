'''Escribe un programa que lea un archivo CSV llamado empleados.csv 
y muestre solo a los empleados que tengan un salario superior a 3000.

empleados.csv:

Nombre,Salario,Departamento
Juan Pérez,500,Recursos Humanos
Ana Gómez,4200,Marketing
Luis Rodríguez,2800,Desarrollo
María Fernández,1900,Finanzas
Carlos Sánchez,4700,Ventas
Sofía Torres,3200,Desarrollo
Pedro Díaz,4500,Marketing'''
import csv

empleados_3000 = []

with open("empleados.csv", "r") as f:
    lector = csv.DictReader(f)
    for linea in lector:
        salario = int(linea["Salario"])
        if salario > 3000:
            empleados_3000.append(linea)

for emp in empleados_3000:
    print(emp)

with open("Empleados3000.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["Nombre", "Salario", "Departamento"]
    escritor = csv.DictWriter(f, fieldnames=fieldnames)
    escritor.writeheader()           # Opcional, pero recomendable
    escritor.writerows(empleados_3000) 
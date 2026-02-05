'''with open("datos.csv","r") as f:
    for linea in f:
        print(linea.strip())
import csv
#lee como lista
with open("datos.csv","r") as f:
    lector = csv.reader(f)
    next(lector) #salta primera linea(encabezado)
    for linea in lector:
        print(linea)
#leer como diccionario
with open("datos.csv","r") as f:
    lector = csv.DictReader(f)
    #next(lector) #salta primera linea(encabezado)
    for linea in lector:
        print(linea)'''
import csv
lista_datos = [
    ["persona1","1","ciudad1"],
    ["persona2","2","ciudad2"]
]
listadatos_dicc = [
    {"Nombre": "persona1", "dni": "1"},
    {"Nombre": "Persona2", "dni": "2"}
]
#escritura csv
with open("datos.csv", "a", newline="") as f:
    escritor = csv.writer(f)
    # Escribimos Mary y Lopez como fila independiente
    escritor.writerow(['Mary', 'Lopez'])
    # Escribimos las filas de la lista
    escritor.writerows(lista_datos)
#escritura en csv
# Escritura con diccionarios
with open("datos2.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["Nombre", "dni"]
    escritor = csv.DictWriter(f, fieldnames=fieldnames)
    escritor.writeheader()           # Opcional, pero recomendable
    escritor.writerows(listadatos_dicc)    


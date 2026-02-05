'''Escribe un programa que cree un archivo CSV llamado productos.csv 
y escriba en él los nombres de productos, sus precios y cantidades en stock.

Ejemplo:

Producto,Precio,Cantidad
Manzana,1.50,100
Banana,0.80,150
Naranja,0.90,120'''
import csv
listaDatos_dicc =[
    {"Producto":"Manzana","Precio":"1.50","Cantidad":"100"},
    {"Producto":"Banana","Precio":"0.80","Cantidad":"150"},
    {"Producto":"Naranja","Precio":"0.90","Cantidad":"120"}
]
with open("productos.csv","w", newline="") as f:
    fieldnames = ["Producto","Precio","Cantidad"]
    escritor = csv.DictWriter(f,fieldnames=fieldnames)
    escritor.writeheader() 
    escritor.writerows(listaDatos_dicc)
'''Crea un programa que añada nuevas filas de datos a un archivo CSV
 llamado inventario.csv. Las nuevas filas deben incluir los datos de productos adicionales.

inventario.csv

Grapadora,12.99,50
Bolígrafo,0.99,500'''
import csv
campos =["producto","precio","cantidad"]
with open("inventario.csv","a",newline="") as f:
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()           
    while True:
        producto={
            "producto": input("Introduce producto: "),
            "precio": input("Introduce precio: "),
            "cantidad": input("Introduce cantidad: ")
        }
        if(int(producto["cantidad"]) > 10):
            escritor.writerow(producto)
            print("Producto insertado")
        else:
            print("La cantidad del producto es menor a 10")
        opcion = input("¿Continuar?s/n: ")
        if(opcion == "n"):
            break; 
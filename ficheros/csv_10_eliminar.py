'''Enunciado
Crea un programa que elimine una fila de un archivo CSV llamado
 inventario.csv basándose en el nombre de un producto que proporcione el usuario.'''
import csv
nombreProducto = input("Producto: ")
filasFiltradas = []

with open("inventario.csv","r") as f:
    lector = csv.DictReader(f)
    for l in lector:
        if(l['Producto'] != nombreProducto):
            filasFiltradas.append(l)

with open("inventario.csv","w") as f:
    campos = ['Producto', 'Precio', 'Cantidad']
    escritor = csv.DictWriter(f, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(filasFiltradas)

print(f"El producto '{nombreProducto}' ha sido eliminado del inventario.")
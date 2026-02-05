'''Ejercicio 7
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa
debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario 
decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total,
con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste'''

cesta={}

while(True):
    articuloInput = input('Articulo: ')
    precioInput = input('Precio: ')
    cesta[articuloInput] = precioInput
    salir = input('¿salir?s/n: ')
    if(salir == 's'):
        break

print("\nLista de la compra")
print("Artículo\tPrecio")

total = 0
for articulo, precio in cesta.items():
    print(f"{articulo}\t\t{precio}")
    total += float(precio)

print(f"Total\t\t{total}")
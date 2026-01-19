'''Ejercicio 3
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio 
de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar
 un mensaje informando de ello.'''
frutas = {
    "platano":1.35,
    "manzana":0.8,
    "pera":0.85,
    "naranja":0.7
}
frutaInput = input("Fruta: ")
kiloInput = input("Kilos: ")

for clave in frutas:
    if(clave == frutaInput):
        precioTotal = frutas[clave] *  int(kiloInput)
        print(f"Precio total: {precioTotal} ")

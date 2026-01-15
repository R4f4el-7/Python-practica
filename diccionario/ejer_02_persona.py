'''Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y 
lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> 
tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.'''
persona = {
    "nombre":"",
    "edad":"",
    "direccion":"",
    "telefono":""
}
for clave, valor in persona.items():
    valor = input(f'{clave}: ')
    print(valor)

print(persona)
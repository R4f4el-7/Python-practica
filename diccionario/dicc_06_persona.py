'''Ejercicio 6
Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario.
 Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.'''
diccionario = {
    "nombre":"",
    "edad":"",
    "sexo":""
}
for clave in diccionario:
    diccionario[clave] = input(f'Introduce {clave}: ')
    print(diccionario)



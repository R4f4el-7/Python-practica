'''Ejercicio 8
Escribir un programa que cree un diccionario de traducción español-inglés. 
El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
y cada par <palabra>:<traducción> separados por comas. El programa debe crear un 
diccionario con las palabras y sus traducciones. Después pedirá una frase en español 
y utilizará el diccionario para traducirla palabra a palabra. 
Si una palabra no está en el diccionario debe dejarla sin traducir.'''
traductor = {}

entrada = input(
    "Introduce las palabras en formato palabra:traducción separadas por comas: "
)

pares = entrada.split(",")

for par in pares:
    palabra, traduccion = par.split(":")
    traductor[palabra] = traduccion

frase = input("Introduce una frase en español: ")

palabras = frase.split()
frase_traducida = []

for palabra in palabras:
    if palabra in traductor:
        frase_traducida.append(traductor[palabra])
    else:
        frase_traducida.append(palabra)

print("Traducción:")
print(" ".join(frase_traducida))
'''Ejercicio 3: Crea una función analizar_texto(texto) que devuelva una tupla con:
● Número total de caracteres.
● Número de palabras.
● Primera palabra del texto.'''
def analizar_texto(texto):
    num_caracteres = len(texto)
    num_palabras = len(texto.split())
    primera_palabra = texto.split()[0]

    return num_caracteres,num_palabras,primera_palabra

num_caracteres,num_palabras,primera_palabra = analizar_texto("Hola mundo")
print(f'Numeto total de caracteres: {num_caracteres}')
print(f'Numero de palabras: {num_palabras}')
print(f'Primera palabra: {primera_palabra}')
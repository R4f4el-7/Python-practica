'''Modifica la cadena “ este ejercicio es muy complicado ” para que el ejercicio
sea facilísimo y cada una de las palabras comience en mayúsculas y sin espacios y luego
imprimelo invertido, ademas busca el indice de la palabra complicado.'''

cadena = " este ejercicio es muy complicado " 
cadena_sin_espacio = cadena.strip()
palabras = cadena_sin_espacio.split()
lista_palapras_mayuscula = []
for palabra in palabras:
    lista_palapras_mayuscula.append(palabra.capitalize())
cadena_palabras = " ".join(lista_palapras_mayuscula)
cadena_invertida = cadena_palabras[::-1]
indice_complicado = cadena_sin_espacio.find("complicado")

print(cadena)
print(palabras)
print(cadena_palabras)
print(cadena_invertida)
print("Índice de 'complicado':", indice_complicado)
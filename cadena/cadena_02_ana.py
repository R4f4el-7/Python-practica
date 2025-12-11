'''Ejercicio 2 (Ana López)
Vamos a definir una cadena y la vamos a pasar a minúsculas, eliminar los espacios
y las letras pares las vamos a cambiar por asteriscos'''
cadena = "Esto es  una cadena"
cadena_sin_espacios = cadena.replace(" ","")
cadena_par = ""
contador = 0
for letra in cadena_sin_espacios:
    if contador % 2 == 0:
        cadena_par += "*"
    else:
        cadena_par += letra
    contador += 1

print(cadena)
print(cadena_sin_espacios)
print(cadena_par)
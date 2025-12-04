'''Pida al usuario una frase.

Elimine los espacios al inicio y al final (strip()).

Muestre:

La frase en minúsculas (lower()).

La frase en mayúsculas (upper()).

La frase con la primera letra en mayúscula (capitalize()).

Reemplace todas las comas por puntos (replace()).

Cuente cuántas veces aparece una palabra que el usuario ingresa (count()).

Verifique si la frase empieza con una vocal (startswith()).

Muestre cuántas palabras tiene la frase (split()).'''

cadenaInput = input("Cadena: ")
cadena = cadenaInput.strip()
print("Cadena sin espacios inicial y final: "+cadena)
print("Cadena en minúscula: "+cadena.lower())
print("Cadena en mayuscula: "+cadena.upper())
print("Cadena comienza con mayuscula: "+cadena.capitalize())
print("Cadena reemplazando comas por puntos: "+cadena.replace(",", "."))
print("Cantidad de palabras: "+str(cadena.count(" ")+1))
arr_vocal = ["a","e","i","o","u"]
valido = False
for vocal in arr_vocal:
    if (cadena.lower().startswith(vocal)):
        valido = True
        break
if(valido):
    print("La cadena comienza con vocal")
else:
    print("No comienza con vocal")
    
print("Cadena separada por palabras: "+str(cadena.split()))
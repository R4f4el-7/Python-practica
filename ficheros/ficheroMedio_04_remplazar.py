'''Enunciado
Crea un programa que lea un fichero datos.txt, reemplace todas las apariciones de una palabra 
con otra palabra proporcionada por el usuario, y guarde los cambios en un nuevo fichero modificado.txt.

Instrucciones:

Solicita al usuario la palabra a reemplazar y la nueva palabra.
Lee todo el contenido del fichero.
Usa el método replace() para reemplazar las palabras.
Guarda el resultado en un nuevo fichero.'''

palabraInicial = input("Palabra a remplazar: ")
palabraFinal = input("Nueva palabra: ")

with open("data.txt","r") as f:
    contenido = f.read()

contenido = contenido.replace(palabraInicial, palabraFinal)
    
with open("dataNueva.txt","w") as f:
    f.write(contenido)
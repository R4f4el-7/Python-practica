'''Enunciado
Escribe un programa que lea un fichero datos.txt y cuente cuántas palabras contiene en total.

Instrucciones:

Abre el fichero en modo lectura.
Lee todas las líneas y luego utiliza la función split() para separar las palabras.
Cuenta todas las palabras y muestra el total.
datos.txt:

Python es un lenguaje de programación.
Se utiliza para el desarrollo web, ciencia de datos, automatización y mucho más.
El aprendizaje automático y la inteligencia artificial son áreas populares de Python.
Los pandas son una biblioteca de Python para análisis de datos.
Este archivo de texto es un ejemplo para practicar con ficheros en Python.
Python es fácil de aprender y tiene una gran comunidad.'''

with open("data.txt","r") as f:
    linea = f.read()
    palabras = linea.split()
    print(len(palabras))
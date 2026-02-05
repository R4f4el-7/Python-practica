'''Escribe un programa que copie el contenido de un fichero datos.txt 
a un nuevo fichero llamado copia.txt.

Instrucciones:

Abre el fichero original en modo lectura.
Abre el nuevo fichero en modo escritura.
Copia el contenido de un fichero al otro.
Cierra ambos ficheros.'''

with open("data.txt","r") as f:
    lineas = f.read()

with open("copia.txt","a") as f:
    f.write(lineas)

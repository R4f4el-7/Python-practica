'''Escribe un programa que copie el contenido de un fichero datos.txt 
a un nuevo fichero llamado copia.txt.

Instrucciones:

Abre el fichero original en modo lectura.
Abre el nuevo fichero en modo escritura.
Copia el contenido de un fichero al otro.
Cierra ambos ficheros.'''
try:
    f = open("copia.txt", "x") 

    with open("data.txt") as f:
        with open("copia.txt", "a") as f:
            f.write(f.read())

    #open and read the file after the appending:
    with open("copia.txt") as f:
        print(f.read())
except:
    print("dio un error")
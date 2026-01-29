'''Escribe un programa que abra un fichero de texto llamado datos.txt, lea todo su contenido y lo muestre por pantalla.

Instrucciones:

Usa la función open() para abrir el fichero en modo lectura.
Usa read() para leer el contenido.
Imprime el contenido en la consola.
Cierra el fichero.
datos.txt:'''
try:
    with open("data.txt") as f:
        print(f.read())
    f.close()
except:
    print("Fichero no existe")
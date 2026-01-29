'''Escribe un programa que cree un fichero nuevo.txt 
y escriba en él varias líneas de texto introducidas por el usuario.

Instrucciones:

Usa open() en modo escritura (‘w’).
Solicita al usuario varias líneas de texto.
Escribe cada línea en el fichero.
Cierra el fichero al finalizar.'''
try:
    f = open("nuevo.txt", "x") 

    cantidadInput = input("Cantidad de lineas: ")
    for num in range(int(cantidadInput)):
        lineaInput = input(f'linea {num}: ')
        with open("nuevo.txt", "a") as f:
            f.write(lineaInput+"\n")

    #open and read the file after the appending:
    with open("nuevo.txt") as f:
        print(f.read())
except:
    print("dio un error")
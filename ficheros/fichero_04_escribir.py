'''Escribe un programa que cree un fichero nuevo.txt 
y escriba en él varias líneas de texto introducidas por el usuario.

Instrucciones:

Usa open() en modo escritura (‘w’).
Solicita al usuario varias líneas de texto.
Escribe cada línea en el fichero.
Cierra el fichero al finalizar.'''
try:
    with open("nuevo.txt", "w") as fichero:
        while True:
            linea = input("Escribe una línea (o 'fin' para terminar): ")
            if linea.lower() == "fin":
                break
            fichero.write(linea + "\n")
except:
    print("dio un error")
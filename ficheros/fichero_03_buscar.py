'''Crea un programa que lea el fichero datos.txt y cuente cuántas veces aparece una palabra específica que el usuario introduce.

Instrucciones:

Solicita al usuario la palabra a buscar.
Usa read() para leer todo el contenido del fichero.
Usa el método count() para contar las ocurrencias de la palabra.'''

palabraInput = input("Palabra a buscar: ")
try:
    with open("data.txt") as f:
        linea = f.read()
        print(linea.count(palabraInput))
    f.close()
except:
    print("Fichero no existe")
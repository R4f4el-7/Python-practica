'''Ejercicio 2: Tabla de multiplicar
Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10. Usa un bucle for
para generar la tabla. Si el usuario introduce un valor no numérico, muestra un mensaje de
error usando try-except'''
def tabla(num):
    resultado = []
    i=1
    while(i < 11):
        resultado.append(i*num)
        i += 1
    return resultado

try:
    num = int(input("Introduce num: "))
    
    list_tabla = tabla(num)
    
    for n in list_tabla:
        print(n, end=",")
except ValueError:
    print("Valor no valido")
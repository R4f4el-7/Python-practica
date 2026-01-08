'''Ejercicio 2: Tabla de multiplicar
Pide al usuario un número y muestra su tabla de multiplicar del 1 al 10. Usa un bucle for
para generar la tabla. Si el usuario introduce un valor no numérico, muestra un mensaje de
error usando try-except'''

try:
    num = int(input("Introduce num: "))

    for i in range(1,11):
        print(f"{i} X {num} = {(i*num)}")
except ValueError:
    print("Valor no valido")

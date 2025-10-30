'''Ejercicio 1: Calculadora de operaciones básicas
Crea un programa que simule una calculadora. El usuario debe introducir dos números y
seleccionar una operación: suma, resta, multiplicación o división. El programa debe
repetirse hasta que el usuario decida salir. Debe manejar errores como división por cero y
entrada de datos no numéricos.'''
def suma(a, b):
    return a + b
def resta(a, b):
    return a - b
def multiplicacion(a, b):
    return a * b
def division(a, b):
    return a / b

opcion = ""

while(opcion != "5"):
    print("Operaciones: ")
    print("1-Suma")
    print("2-Resta")
    print("3-Multiplicacion")
    print("4-Division")
    print("5-Salir")

    opcion = input("Opcion: ")

    if opcion == "5":
        print("Fin")
        break 
     
    try:
        num1 = int(input("num1: "))
        num2 = int(input("num2: "))
    except ValueError:
        print("Valor no valido")
        continue

    if opcion == "1":
        print(f"Resultado: {suma(num1, num2)}")
    elif opcion == "2":
        print(f"Resultado: {resta(num1, num2)}")
    elif opcion == "3":
        print(f"Resultado: {multiplicacion(num1, num2)}")
    elif opcion == "4":
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            print(f"Resultado: {division(num1, num2)}")
    else:
        print("Opción no válida. Intenta de nuevo.")
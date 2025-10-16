'''Ejercicio 1: Calculadora de operaciones básicas
Crea un programa que simule una calculadora. El usuario debe introducir dos números y
seleccionar una operación: suma, resta, multiplicación o división. El programa debe
repetirse hasta que el usuario decida salir. Debe manejar errores como división por cero y
entrada de datos no numéricos.'''
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
        resultado = num1 + num2
        print(f"Resultado: {resultado}")
    elif opcion == "2":
        resultado = num1 - num2
        print(f"Resultado: {resultado}")
    elif opcion == "3":
        resultado = num1 * num2
        print(f"Resultado: {resultado}")
    elif opcion == "4":
        if num2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = num1 / num2
            print(f"Resultado: {resultado}")
    else:
        print("Opción no válida. Intenta de nuevo.")

        
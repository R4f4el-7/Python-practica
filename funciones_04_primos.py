'''Ejercicio 4: Comprobar si un número es primo
Solicita al usuario un número entero positivo y comprueba si es primo. Usa un bucle while
para verificar si tiene divisores y muestra el resultado. Valida la entrada con try-except.'''

def esPrimo(num):
    contador = 0
    i = 1

    while i <= num:
        if num % i == 0:
            contador += 1
        i += 1
    """for i in range(1,num+1):
        if num % i == 0:
            contador += 1"""
    
    if contador == 2:
        print('Es primo')
    else:
        print('No es primo')

try:
    num = int(input('Introduce num: '))
    esPrimo(num)
except ValueError:
    print("Valor no valido")
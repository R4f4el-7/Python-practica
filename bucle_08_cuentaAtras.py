'''Ejercicio 2: Cuenta atrás
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
la cuenta atrás desde ese número hasta cero separados por comas'''
try:
    num = int(input('Numero: '))

    while(num >= 0):
        print(f'{num}')
        num -= 1
except ValueError:
    print('valor invalido')
'''Ejercicio 1: Calcula inversión
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el
número de años, y muestre por pantalla el capital obtenido en la inversión cada año que
dura la inversión.'''
cantidad_inversion = int(input('Cantidad de inversion: '))
interes_anual = int(input('Interes anual: '))
num_anno = int(input('Numero de años: '))

capital = cantidad_inversion * (interes_anual/100) * num_anno

print(f'Capital: {capital}')
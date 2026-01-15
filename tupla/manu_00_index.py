'''Adivina en qué posición está el nº n (aleatorio 1-10) en una tupla'''
import random
tupla = (1,2,3,4,5,6,7,8,9,10)
numero_aleatorio = random.randint(1,10)
print(f'Numero aleatorio: {numero_aleatorio}')
numero = input('Introduce numero: ')
print(f'numero en el indice {int(numero)}: {tupla.index(int(numero))}')
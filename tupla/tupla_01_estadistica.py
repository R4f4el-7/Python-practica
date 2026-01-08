'''Ejercicio 1: Crea una función calcular_estadisticas(numeros) que reciba una lista de
números y devuelva una tupla con:
● El valor mínimo.
● El valor máximo.
● La media aritmética.'''
def calcular_estadisticas(numeros):
    return min(numeros), max(numeros), sum(numeros)/2
numeros = [1, 10]
print(f'Minimo: {calcular_estadisticas(numeros)[0]}')
print(f'Maximo: {calcular_estadisticas(numeros)[1]}')
print(f'Media: {calcular_estadisticas(numeros)[2]}')
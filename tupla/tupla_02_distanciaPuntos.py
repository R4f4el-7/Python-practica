'''Ejercicio 2: Crea una función distancia(p1, p2) que reciba dos tuplas representando
puntos en el plano (x, y) y devuelva la distancia entre ellos usando la fórmula:'''
import math
def distancia(p1,p2):
    return math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
print(f'Distancia entre puntos: {distancia((1,1),(2,2))}')
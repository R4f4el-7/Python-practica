'''Módulo de cálculo de áreas
Crear un módulo (calculos.py) que contenga funciones para calcular el área de un círculo
areaCirculo(radio), cuadrado areaCuadrado(lado) y triángulo areaTriangulo(base,
altura). Hay que tener en cuenta que si no se ha introducido alguno de los valores
necesarios, tomará por defecto el 8
Desde otro fichero. usa las funciones del módulo para calcular el área de un círculo con
radio 5, un cuadrado de lado 10 y un triángulo de base 4 y altura 6.'''
import calculos

print(f"Area del circulo: {calculos.areaCirculo(5)}")
print(f"Area del lado: {calculos.areaCuadrado(10)}")
print(f"Area del triangulo: {calculos.areaTriangulo(4,6)}")

print("---Valores por defecto---")
print(f"Area del circulo: {calculos.areaCirculo()}")
print(f"Area del lado: {calculos.areaCuadrado()}")
print(f"Area del triangulo: {calculos.areaTriangulo()}")

import calculos as cal

print(f"Area del circulo: {cal.areaCirculo(5)}")
print(f"Area del lado: {cal.areaCuadrado(10)}")
print(f"Area del triangulo: {cal.areaTriangulo(4,6)}")

from calculos import areaCirculo, areaCuadrado, areaTriangulo

print(f"Area del circulo: {areaCirculo(5)}")
print(f"Area del lado: {areaCuadrado(10)}")
print(f"Area del triangulo: {areaTriangulo(4,6)}")
'''Añade una nueva función al módulo multiplicandoUnaSuma que reciba
cualquier cantidad de números y un parámetro multiplicador La función debe devolver la
suma de los números multiplicada por el valor del multiplicador.
'''
def multiplicandoSuma(multi, *num):
    total = multi * sum(num)
    return total

print(multiplicandoSuma(10, 1, 2, 3))
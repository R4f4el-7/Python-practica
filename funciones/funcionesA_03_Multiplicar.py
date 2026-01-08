'''Añade otra función multiplicar que reciba cualquier cantidad de números y
devuelva su producto.'''
def multiplicarNum(*num):
    total = 1
    for n in num:
        total *= n
    return total

print(multiplicarNum(1, 2, 3))
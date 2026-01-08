tupla = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
total = 0
for n in range(10):
    if(n%2 != 0):
        x = tupla.count(n)
        print(f'Contador de {n}: {x}')
        total += x
print(f'Total de impares es: {total}')
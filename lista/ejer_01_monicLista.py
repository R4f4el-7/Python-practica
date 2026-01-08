lista = [1,2,3,2,5,6,7,8,9]
cont = 0
numB = 2
for num in lista:
    if(numB == num):
        cont += 1
if(cont > 1):
    print("Aparecio más una vez")
if(cont == 1):
    print("Aparecio una vez")
else:
    print(f'Aparecio ${cont} veces')
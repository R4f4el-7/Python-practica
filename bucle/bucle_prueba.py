"""for i in [5, 4, 3, 2, 1] :
    print(i)
print('Blastoff!')"""

n = 5
while(n > 0):
    print(n)
    n = n -1
print('blastoff!')
print(n)

while True:
    line = input('> ')
    if line[0] == '#' :
        continue
    if line == 'done' :
        break
    print(line)
print('Done!')

#lectura de array con for
friends = ["amigo1", "amigo2", "amigo3"]

for friend in friends:
    print('Bienvenido ', friend)
print('done')

#media de un numero
contador = 0
total = 0

notas = [1, 2, 5, 6, 1]

for nota in notas:
    total += nota
    contador += 1
print('Media: ', total/contador)
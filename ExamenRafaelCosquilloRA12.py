'''lista_nombre_1 = ["Alberto", "Antonio", "Infanta"]
lista_nombre_2 = ["Elena", "Alberto", "Benedicto"]

contador_validos = 0

for i in lista_nombre_1:
    for j in lista_nombre_2:
        try:
            if(i != j): #ALBERTO ALBERTO
                print(f"Nombre compuesto: {i}{j}")
                contador_validos += 1
            nombre_compuesto = i + j
            if(nombre_compuesto == "InfantaElena"):
                raise ValueError
        except ValueError:
            print("IES en Galapagar con estudios de formación profesional")

print(f"Se han generado {contador_validos} nombres validos")
precio = -1
contador_10 = 0
total = 0
mayor = 0

while(precio != 9999.99):
    try:
        precio = float(input("Introduzca precio: "))
        if(precio < 0 ):
            raise ValueError
        if(precio == 9999.99):
            continue
        if(precio >= 10):
            print(f"El precio {precio} es mayor o igual a 10")
            contador_10 += 1
            total = total + precio
        if(precio > mayor):
            mayor = precio
    except ValueError:
        print("Valor no valido")
print(f"Hay {contador_10} productos mayor o igual a 10")
print(f"El precio medio: {total / contador_10}")
print(f"El precio mas alto: {mayor}")'''

total_fibo = 0
variable_1= 1

for i in range(0,5):
    variable_1 = variable_1 + total_fibo
    print(f"{total_fibo},{variable_1}", end=",")
    total_fibo = total_fibo + variable_1


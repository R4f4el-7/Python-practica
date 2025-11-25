from operaciones import *

#Ejercicio 1
print(f"Cantidad de argumentos: {info_argumentos(1,2,3)}")
divisibles3(3,7,9,11,12)
histograma(4,9,7)

#Ejercicio 2
print(f"Total: {coste_envio(4,False,2)}")
print(f"Total: {coste_envio(4,True,2)}")

print(f"Total: {coste_envio(4,False)}")
print(f"Total: {coste_envio(4,True)}")

print(f"Total: {coste_envio(4)}")

#Ejercicio 3
import operaciones as op

while(True):
    try:
        horas = int(input("Introduce las horas: "))
        minutos = int(input("Introduce las minutos: "))
        segundos = int(input("Introduce las segundos: "))

        if(horas >= 0 and horas < 24 and minutos >= 0 and minutos < 60
            and segundos >= 0 and segundos < 60):
            print(f"Total de segundos: {op.convertir_segundos(horas,minutos,segundos)}")
            break
        else:
            print("Debe seguir el formato 24 horas")
            continue
    except ValueError:
        print("Valor no valido")
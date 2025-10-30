'''Ejercicio 5: Números primos hasta N
Solicita al usuario un número entero positivo N y muestra todos los números primos desde 2
hasta N. Usa un bucle for para recorrer los números y otro bucle while para verificar si son
primos. Maneja errores si el usuario introduce un valor no válido.'''

def primosN(num):
    contador = 0
    i = 1
    j = 1

    while(i <= num):
        while(j <= i):
            if(i % j == 0):
                contador += 1
            j += 1
        
        if(contador == 2):
            print(f"{i} es primo")
        
        contador = 0
        j = 1
        i += 1

try:
    num = int(input("Introduce num: "))
    primosN(num)
except ValueError:
    print("Valor no valido")
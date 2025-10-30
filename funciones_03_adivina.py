'''Ejercicio 3: Adivina el número
El programa genera un número aleatorio entre 1 y 100. El usuario debe adivinarlo. Después
de cada intento, el programa indica si el número es mayor o menor. Usa try-except para
validar que la entrada sea numérica. El juego termina cuando el usuario acierta.'''
import random

def adivinarNum(num_aleatorio):
    num_intento = 0
    while True:
        try:
            num_intento += 1
            num = int(input("Introduce valor num: "))

            if(num > num_aleatorio):
                print("El numero que buscas es menor")
            elif(num < num_aleatorio):
                print("El numero que buscas es mayor")
            else:
                print(f"Iguales. Intentos: {num_intento}")
                break
        except ValueError:
            print("Valor no valido")

    print(f"Numero aleatorio: {num_aleatorio}")

num_aleatorio = random.randint(1, 100)
print(num_aleatorio)
adivinarNum(num_aleatorio)
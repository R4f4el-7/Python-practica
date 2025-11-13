print("-----Nombre-----")
def my_function(greeting, *names):
    for name in names:
        print(greeting, name)
    print(names[0])

my_function("Hello", "Emil", "Tobias", "Linus")

print("-----Suma-----")
def my_function_suma(multi, *numbers):
  total = 0
  for num in numbers:
    total += (num * multi)
  return total

print(my_function_suma(10, 2, 3))
print(my_function_suma(10, 20, 30, 40))
print(my_function_suma(10, 5))
print(my_function_suma(0))

print("-----Maximo-----")
def my_function_maximo(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

print(my_function_maximo(3, 7, 2, 9, 1))

print("-----Pizza-----")
def my_function_pizza(porciones, *ingredientes):
    cadena = ", ".join(ingredientes)
    return "Tu pizza tiene "+str(porciones)+" porciones y "+cadena

print(my_function_pizza(8, "peperoni", "ajo", "piña", "barbacoa", "abeto"))

import random

print("-----Ganador-----")
def my_function_ganador(*nombres):
    ran = random.randint(0 ,len(nombres)-1)
    return nombres[ran]

print(my_function_ganador("nombre1","nombre2","nombre3","nombre4"))

import mymodule as mol
#from mymodule import calculaSuma,greeting

print("-----mymodule-----")
mol.greeting("Jonathan")
mol.calculaSuma(1,2)
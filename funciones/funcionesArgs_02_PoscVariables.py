#*args permite recibir cualquier cantidad de argumentos posicionales(sin nombre).
def suma(*args):
    return sum(args)

print(suma(1,2,3))

#**kwargs permite recibir cualquier cantidad de argumentos con nombre.
def mostrar_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=25)

#parámetros normales → predeterminados → *args → **kwargs

#def ejemplo(a, b=10, *args, **kwargs):
#   pass
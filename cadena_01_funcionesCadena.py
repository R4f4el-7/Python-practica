'''lower y upper'''
print("---lower y upper---")
print("Hola Mundo".lower())
print("Hola Mundo".upper())

'''capitalize'''
print("---capitalize---")
print("federico".capitalize())

'''title – Primera letra de cada palabra en mayúscula'''
print("---title---")
print("hola mundo desde python".title())

'''swapcase – Invierte mayúsculas/minúsculas'''
print("---swapcase---")
print("HoLa".swapcase())

'''strip – Quita espacios a ambos lados'''
print("---strip---")
print("   hola   ".strip())

'''lstrip – Quita espacios a la izquierda'''
print("---lstrip---")
print("   hola".lstrip())

'''rstrip – Quita espacios a la derecha'''
print("---rstrip---")
print("hola   ".rstrip())

'''replace – Reemplaza texto'''
print("---replace---")
print("Hola mundo".replace("o", "0"))

'''find – Devuelve índice o -1 si no existe'''
print("---find---")
print("programacion".find("grama"))
print("programacion".find("xyz"))

'''rfind – Búsqueda desde la derecha'''
print("---rfind---")
print("bananana".rfind("na"))

'''index – Igual que find, pero lanza error si no existe'''
print("---index---")
print("python".index("th"))

'''count – Cuenta ocurrencias'''
print("---count---")
print("banana".count("na"))

'''startswith – Comienza con...'''
print("---startswith---")
print("archivo.txt".startswith("arch"))

'''endswith – Termina con...'''
print("---endswith---")
print("foto.png".endswith(".png"))

'''isalpha – Solo letras'''
print("---isalpha---")
print("Hola".isalpha())
print("Hola123".isalpha())

'''isdigit – Solo números'''
print("---isdigit---")
print("12345".isdigit())
print("12a45".isdigit())

'''isalnum – Letras y números'''
print("---isalnum---")
print("Hola123".isalnum())
print("Hola 123".isalnum())

'''isspace – Solo espacios'''
print("---isspace---")
print("   ".isspace())

'''split – Divide en lista'''
print("---split---")
print("uno dos tres".split())
print("a,b,c".split(","))

'''join – Une elementos'''
print("---join---")
print("-".join(["a", "b", "c"]))

'''ljust – Alinea a la izquierda con relleno'''
print("---ljust---")
print("hola".ljust(10, "*"))

'''rjust – Alinea a la derecha con relleno'''
print("---rjust---")
print("hola".rjust(10, "."))

'''center – Centra con relleno'''
print("---center---")
print("hola".center(10, "-"))

'''zfill – Rellenar con ceros a la izquierda'''
print("---zfill---")
print("42".zfill(5))

'''upper, lower, isupper, islower'''
print("---isupper / islower---")
print("HOLA".isupper())
print("hola".islower())

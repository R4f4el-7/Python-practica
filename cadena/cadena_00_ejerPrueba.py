'''
Dos cadenas que formaran una cadena que será intercalar dos cadenas carácter por carácter
Ej: cadena1: Hola mundo cadena2: Adios Juan cadenaDefinitiva: HAodliao s mJuunadno'''
def intercalar(c1, c2):
    salida = ""
    m = max(len(c1), len(c2))

    for i in range(m):
        if i < len(c1):
            salida += c1[i]
        else:
            salida += " "

        if i < len(c2):
            salida += c2[i]
        else:
            salida += " " 

    return salida

print(intercalar("aaaa", "bbbb"))


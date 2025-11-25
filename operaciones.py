#Ejercicio 1
def info_argumentos(*args):
    cont = 0
    for a in args:
        cont += 1
        print(a)
    return cont
def divisibles3(*args):
    for a in args:
        if(a % 3 == 0):
            print(a)
def histograma(*args):
    for a in args:
        i = 0
        cadena = ""
        while(i < a):
             cadena = cadena + "*"
             i += 1
        print(cadena)
#Ejercicio 2
def coste_envio(peso, urgente = False, tarifa_base = 5):
    total = 0
    tarifa_total = tarifa_base + (peso * 2)
    if(urgente):
        total = tarifa_total + (tarifa_total * (30/100))
        return total
    
    return tarifa_total
#Ejercicio 3
def convertir_segundos(horas, minutos, segundos):
    horas_segundos = horas * 60 * 60
    minutos_segundos = minutos * 60

    return horas_segundos + minutos_segundos + segundos
    
        
        
    

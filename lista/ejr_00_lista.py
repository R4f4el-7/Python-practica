'''crea un lista de comandos que te permita ejecutar la lista de comandos'''
def saludo():
    print('hola')
def despedida():
    print('adios')
tupla = ('hola','despedida')
comandoInput = input('Di el comando: ')
if(comandoInput == tupla[0]):
    saludo()
if(comandoInput == tupla[1]):
    despedida()
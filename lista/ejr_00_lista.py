'''crea un lista de comandos que te permita ejecutar la lista de comandos'''
def saludo():
    print('hola')
def despedida():
    print('adios')
lista = ['hola','despedida']
comandoInput = input('Di el comando: ')
if(comandoInput == lista[0]):
    saludo()
if(comandoInput == lista[1]):
    despedida()
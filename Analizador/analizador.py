

from AnalizadorLexico import *

def hola():
    print('hola mundo')


def Anlexico():
    print('---')
    analizadorLexico.hola()

    texto = 'hola'
    Listatokens = analizadorLexico.GetTokens(texto)
    print(Listatokens)



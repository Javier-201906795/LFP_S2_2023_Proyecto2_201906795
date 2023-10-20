

from AnalizadorLexico import *
from AnalizadorSintactico import *



erroresAnalizador = []


################################################################
def analizadorBizData(texto):
    global erroresAnalizador
    print('Analizando informacion...')
    print(texto)
    #Pasar al analizador Lexico y Obtenga Tokens
    tokens = analizadorLexico.GetTokens(texto)
    analizadorLexico.imprimirlistatokens()
    analizadorLexico.imprimirerroreslexicos()
    if len(tokens) > 0:
        #Pasar al analizador Sintactico y obtener Estructuras
        estructuras = analizadorSintactico.GetInstrucciones(tokens)
        analizadorSintactico.imprimirErrores()
        analizadorSintactico.imprimirlistaSintactico()
        #[A]Obtener Errores
        #[A1]Obtener Errores Lexicos
        erroresLexicos = analizadorLexico.GetErrores()
        #[A2]Obtener Errores Sintacticos
        erroresSintactico = analizadorSintactico.GetErrores()
        #[A3]Unir Errores
        nuevalista = unirdoslistas(erroresLexicos, erroresSintactico) 
        erroresAnalizador = nuevalista
        # imprimirErrores()


################################################################
def imprimirErrores():
    global erroresAnalizador
    print('\n------------[ ERRORES ]----------------\n')
    for i in erroresAnalizador:
        print(i)
    print('\n---------------------------------------')

################################################################
def unirdoslistas(lista1, lista2):
    newlist = []
    for i in lista1:
        newlist.append(i)
    for j in lista2:
        newlist.append(j)

    return newlist


from AnalizadorLexico import *
from AnalizadorSintactico import *



erroresAnalizador = []



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
        analizadorSintactico.imprimirlistaSintactico()
        analizadorSintactico.imprimirErrores()
        #[A]Obtener Errores
        #[A1]Obtener Errores Lexicos
        erroresLexicos = analizadorLexico.GetErrores()
        #[A2]Obtener Errores Sintacticos
        erroresSintactico = analizadorSintactico.GetErrores()
        #[A3]Unir Errores
        erroresAnalizador = []
        erroresAnalizador.append(erroresLexicos)
        erroresAnalizador.append(erroresSintactico)
        imprimirErrores()



def imprimirErrores():
    global erroresAnalizador
    print('\n---------------------------------------')
    for i in erroresAnalizador:
        print(i,'\n')
    print('\n---------------------------------------')



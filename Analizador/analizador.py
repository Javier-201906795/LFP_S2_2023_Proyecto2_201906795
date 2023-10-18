

from AnalizadorLexico import *




def analizadorBizData(texto):
    print('Analizando informacion...')
    print(texto)
    #Pasar al analizador Lexico y Obtenga Tokens
    tokens = analizadorLexico.GetTokens(texto)
    #Pasar al analizador Sintactico y obtener Estructuras
    estructuras = []
    #[A]Obtener Errores
    #[A1]Obtener Errores Lexicos
    erroresLexicos = analizadorLexico.GetErrores()
    print(erroresLexicos)
    #[A2]Obtener Errores Sintacticos
    erroresSintactico = []
    #[A3]Unir Errores
    erroresAnalizador = []
    erroresAnalizador.append(erroresLexicos)
    erroresAnalizador.append(erroresSintactico)




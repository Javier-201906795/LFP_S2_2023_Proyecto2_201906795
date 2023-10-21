




listainstrucciones = []
txtresultado = ''
################################################################




################################################################
def imprimir(texto):
    print(texto)

################################################################
def imprimirInstrucciones():
    print('\n##################### [ Instrucciones ] #############################')
    for i in listainstrucciones: 
        print(i)

################################################################
def evaluarinstrucciones():
    global listainstrucciones, txtresultado
    c = 0
    maxiteraciones = len(listainstrucciones)
    print('\n##################### [ EVALUANDO... ] #############################')
    while c < maxiteraciones:
        instruccion = listainstrucciones[c] 
        print('Instruccion: ',instruccion[0], 'Contenido: ', instruccion[1])
        if instruccion[0] == 'imprimir':
            print('♦ Imprimir: ', instruccion[1])
            txtresultado += '>>> '+ instruccion[1]
        elif instruccion[0] == 'imprimirln':
            print('♦ Imprimirln: ', instruccion[1])
            txtresultado += '>>> '+ instruccion[1]+'\n'
        c += 1


################################################################
def ejecutar(oldlistainstrucciones):
    global listainstrucciones, txtresultado
    txtresultado = ''
    listainstrucciones = oldlistainstrucciones
    evaluarinstrucciones()


    return txtresultado

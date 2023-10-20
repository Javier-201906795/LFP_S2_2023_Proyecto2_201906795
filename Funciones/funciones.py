




listainstrucciones = []






def imprimir(texto):
    print(texto)



def ejecutar(oldlistainstrucciones):
    global listainstrucciones
    listainstrucciones = oldlistainstrucciones

def imprimirInstrucciones():
    print('##################### [ Instrucciones ] #############################')
    for i in listainstrucciones: 
        print(i)
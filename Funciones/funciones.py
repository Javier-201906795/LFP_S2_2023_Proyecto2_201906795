




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
            txtresultado +=  instruccion[1] + ' '
        elif instruccion[0] == 'imprimirln':
            print('♦ Imprimirln: ', instruccion[1])
            txtresultado +=  instruccion[1]+' \n'
        elif instruccion[0] == 'datos':
            print('♦ Mostrar Datos:')
            txtresultado += '\n' + '-- [ datos(); ] --\n'
            txtresultado += '''
codigo  producto precio_compra precio_venta stock\n
1       Salsa    10.5          20.0         7
'''
            txtresultado += '\n------------------------\n'
        elif instruccion[0] == 'promedio':
            print('♦ Promedio("'+instruccion[1]+'")')
            txtresultado += 'promedio("'+instruccion[1]+'");\n'
            txtresultado += '5.5\n'
        elif instruccion[0] == 'sumar':
            print('♦ Sumar("'+instruccion[1]+'")')
            txtresultado += 'sumar("'+instruccion[1]+'");\n'
            txtresultado += '12\n'


        c += 1


################################################################
def ejecutar(oldlistainstrucciones):
    global listainstrucciones, txtresultado
    txtresultado = ''
    listainstrucciones = oldlistainstrucciones
    evaluarinstrucciones()


    return txtresultado

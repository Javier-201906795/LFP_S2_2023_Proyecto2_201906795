

################################################################
listaSintactico = []


################################################################
def imprimirlistaSintactico():
    print('\n############[ Lista Sintactico | Instrucciones]#################\n')
    for i in listaSintactico:
        print(i)
    print('\n################################################################\n')

################################################################
def evaluartokens(tokens):
    global listaSintactico
    print('\n ####### [ EVALUAR TOKENS ] #######')
    #Iterador
    c = 0
    maxiteraciones = len(tokens)
    while c < maxiteraciones:
        #//////////////////////////////////////////////////////////////////////////////////
        #Ignorar Comentarios
        if tokens[c][3] == 'Comentario_multilinea' or tokens[c][3] == 'Comentario_simple':
            c += 1    
        #//////////////////////////////////////////////////////////////////////////////////
        elif tokens[c][0] == 'i' or tokens[c][0] == 'I':
            if tokens[c+1][0] == 'm' or tokens[c+1][0] == 'M':
                if tokens[c+2][0] == 'p' or tokens[c+2][0] == 'P':
                    if tokens[c+3][0] == 'r' or tokens[c+3][0] == 'R':
                        if tokens[c+4][0] == 'i' or tokens[c+4][0] == 'I':
                            if tokens[c+5][0] == 'm' or tokens[c+5][0] == 'M':
                                if tokens[c+6][0] == 'i' or tokens[c+6][0] == 'I':
                                    if tokens[c+7][0] == 'r' or tokens[c+7][0] == 'R':
                                        if tokens[c+8][0] == '(':
                                            if tokens[c+9][3] == 'Texto':
                                                if tokens[c+10][0] == ')':
                                                    texto = tokens[c+9][0]
                                                    c += 11
                                                    print('\n//////////////////\n')
                                                    print(texto)
                                                    print('\n//////////////////')
                                                    listaSintactico.append(['imprimir',texto])
                                                else:
                                                    c += 10
                                            else:
                                                c += 9
                                        else:
                                            c += 8
                                    else:
                                        c += 7
                                else:
                                    c += 6
                            else:
                                c += 5
                        else:
                            c += 4
                    else:
                        c += 3
                else:
                    c += 2
            else:
                c += 1
        #//////////////////////////////////////////////////////////////////////////////////
        else:
            print(tokens[c])
            c += 1
    
        

################################################################
def GetInstrucciones(tokens):
    global listaSintactico

    #Evaluar tokens
    evaluartokens(tokens)

    return listaSintactico


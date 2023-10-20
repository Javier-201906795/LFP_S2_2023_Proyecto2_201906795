

################################################################
listaSintactico = []
listaErroresSintactico = []


################################################################
def imprimirErrores():
    print('\n############[ Errores | Sintactico]#################\n')
    for i in listaErroresSintactico: 
        print(i)
    print('\n################################################################\n')

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
                                                    listaSintactico.append(['imprimir',texto])
                                                else:
                                                    listaErroresSintactico.append([tokens[c+10][0],')',tokens[c+10][1],tokens[c+10][2],'error Sintactico'])
                                                    c += 10
                                            else:
                                                listaErroresSintactico.append([tokens[c+9][0],'Texto',tokens[c+9][1],tokens[c+9][2],'error Sintactico'])
                                                c += 9
                                        else:
                                            listaErroresSintactico.append([tokens[c+8][0],'(',tokens[c+8][1],tokens[c+8][2],'error Sintactico'])
                                            c += 8
                                    else:
                                        listaErroresSintactico.append([tokens[c+7][0],'r',tokens[c+7][1],tokens[c+7][2],'error Sintactico'])
                                        c += 7
                                else:
                                    listaErroresSintactico.append([tokens[c+6][0],'i',tokens[c+6][1],tokens[c+6][2],'error Sintactico'])
                                    c += 6
                            else:
                                listaErroresSintactico.append([tokens[c+5][0],'m',tokens[c+5][1],tokens[c+5][2],'error Sintactico'])
                                c += 5
                        else:
                            listaErroresSintactico.append([tokens[c+4][0],'i', tokens[c+4][1],tokens[c+4][2],'error Sintactico'])
                            c += 4
                    else:
                        listaErroresSintactico.append([tokens[c+3][0],'r',tokens[c+3][1],tokens[c+3][2],'error Sintactico'])
                        c += 3
                else:
                    listaErroresSintactico.append([tokens[c+2][0],'p',tokens[c+2][1],tokens[c+2][2],'error Sintactico'])
                    c += 2
            else:
                listaErroresSintactico.append([tokens[c+1][0],'m',tokens[c+1][1],tokens[c+1][2],'error Sintactico'])
                c += 1
        #//////////////////////////////////////////////////////////////////////////////////
        else:
            print(tokens[c])
            c += 1
    
################################################################
def GetErrores():
    return listaErroresSintactico


################################################################
def GetInstrucciones(tokens):
    global listaSintactico, listaErroresSintactico
    listaSintactico = []
    listaErroresSintactico = []

    #Evaluar tokens
    evaluartokens(tokens)

    return listaSintactico


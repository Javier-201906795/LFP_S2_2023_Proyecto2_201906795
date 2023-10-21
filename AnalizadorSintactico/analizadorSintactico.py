

################################################################
listaSintactico = []
listaErroresSintactico = []
listatokens = []


################################################################
def imprimirErrores():
    print('\n############[ Errores | Sintactico]#################\n')
    for i in listaErroresSintactico: 
        print(i)

################################################################
def imprimirlistaSintactico():
    print('\n############[ Lista Sintactico | Instrucciones]#################\n')
    for i in listaSintactico:
        print(i)

################################################################
def obtenertexto(a):
    global listatokens
    inicio = a
    texto = ''
    #-----
    maxiteraciones = len(listatokens)
    while a < maxiteraciones:
        token = listatokens[a][0]
        if token == '"' or token == "'":
            a += 1
            return [texto,a]
        else:
            texto += token
            a += 1

################################################################
def fininstruccion(a,tokenesperado):
    global listatokens, listaErroresSintactico
    inicio = a
    maxiteraciones = len(listatokens)
    while a < maxiteraciones:
        token = listatokens[a][0]
        if token == ';' or token == '\n':
            a += 1
            #Agregar a errores
            listaErroresSintactico.append([listatokens[inicio][0],str(tokenesperado),listatokens[inicio][1],listatokens[inicio][2],'error Sintactico',listatokens[inicio][1],a])
            return a
        else:
            a += 1
    



################################################################
def evaluartokens(tokens):
    global listaSintactico, listatokens
    listatokens = tokens
    print('\n####### [ EVALUAR TOKENS ] #######')
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
                                            if tokens[c+9][0] == '"':
                                                #ObtenerTexto
                                                texto, a = obtenertexto(c+10)
                                                print('TEXTO: ', texto, ' A:',a)
                                                #cambiar numero iteracion
                                                c = a 
                                                print('new c:', c,'token:',tokens[c][0], 'next:',c+1,'tokennext:',tokens[c+1][0])
                                                if tokens[c][0] == ')':
                                                    sig = tokens[c+1][0]
                                                    if tokens[c+1][0] == ';':
                                                        sig = tokens[c+2][0]
                                                        c += 2
                                                        listaSintactico.append(['imprimir',texto])
                                                    else:
                                                        a = fininstruccion(c+1,';')
                                                        c = a + 1
                                                else:
                                                    a = fininstruccion(c, ')')
                                                    c = a + 1
                                            else:
                                                a = fininstruccion(c+9,'"')
                                                c = a + 1
                                        else:
                                            if tokens[c+8][0] == 'l' or tokens[c+8][0] == 'L':
                                                if tokens[c+9][0] == 'n' or tokens[c+9][0] == 'N':
                                                    if tokens[c+10][0] == '(':
                                                        if tokens[c+11][0] == '"':
                                                            #ObtenerTexto
                                                            texto, a = obtenertexto(c+12)
                                                            print('TEXTO: ', texto, ' A:',a)
                                                            c = a
                                                            if tokens[c][0] == ')':
                                                                if tokens[c+1][0] == ';':
                                                                    print('imprimirln: ', texto)
                                                                    listaSintactico.append(['imprimirln',texto])
                                                else:
                                                    a = fininstruccion(c+9, 'n | N')
                                                    c = a + 1
                                            else:
                                                a = fininstruccion(c+8,'( | l | L')
                                                c = a + 1
                                    else:
                                        a = fininstruccion(c+7, 'r | R')
                                        c = a + 1
                                else:
                                    a = fininstruccion(c+6,'i | I')
                                    c = a + 1
                            else:
                                a = fininstruccion(c+5,'m | M')
                                c = a + 1
                        else:
                            a = fininstruccion(c+4,'i | I')
                            c = a + 1
                    else:
                        a = fininstruccion(c+3, 'r | R')
                        c = a + 1
                else:
                    a = fininstruccion(c+2, 'p | P')
                    c = a + 1
            else:
                a = fininstruccion(c+1,'m | M')
                c = a + 1
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




################################################################
listaSintactico = []
listaErroresSintactico = []
listatokens = []
listasimbolos = ['{','}',':','[',']',',','(',')',';','=','"',"'",'#','_','-','.']
listaletras = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','Ñ','ñ']


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
        token = listatokens[a][1]
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
        token = listatokens[a][1]
        if token == ';' or token == '\n':
            a += 1
            #Agregar a errores
            listaErroresSintactico.append([listatokens[inicio][1],str(tokenesperado),listatokens[inicio][2],listatokens[inicio][3],'error Sintactico',listatokens[inicio][2],listatokens[a-1][3]])
            return a
        else:
            a += 1
################################################################################################################################
################################################################################################################################
################################################################
def ErrorAFDTextoentrecomillas(a,tokenesperado):
    global listatokens, listaErroresSintactico
    inicio = a
    maxiteraciones = len(listatokens)
    while a < maxiteraciones:
        token = listatokens[a][1]
        if token == ')' or token == ';' or token == '\n':
            a += 1
            #Agregar a errores
            listaErroresSintactico.append([listatokens[a-1][1],str(tokenesperado),listatokens[a-1][2],listatokens[a-2][3],'error Sintactico',listatokens[a-1][2],listatokens[a-1][3]])
            return a
        else:
            a += 1


################################################################
def AFDTextoentrecomillas(c):
    global listatokens
    #iterador
    maxiteraciones = len(listatokens)
    #TEXTO
    texto = ''
    #Estados
    #q1,q2,q3,q4,q5
    inicio = 0
    final = 5
    estado = inicio

    if listatokens[c][1] == '"':
        estado = 1
        c+=1
        while c < maxiteraciones:
            #Token
            token = listatokens[c][1]
            if token == ')' or token == ';' or token == '\n':
                return False
            elif token == '"':
                estado = 5
                c+=1
                return True
            elif token in listaletras:
                estado = 2
                c+=1
            elif token in listasimbolos:
                estado = 3
                c+=1
            elif token.isdigit():
                estado = 4
                c+=1
            else:
                c+=1
        
        return False
################################################################
def getTextoentrecomillas(c):
    global listatokens
    #iterador
    maxiteraciones = len(listatokens)
    #TEXTO
    texto = ''
    if listatokens[c][1] == '"':
        c+=1
        while c < maxiteraciones:
            #Token
            token = listatokens[c][1]
            if token == '"':
                c+=1
                return texto, c
            elif token in listaletras or token in listasimbolos:
                #Añadir token
                texto += token
                c+=1
            else:
                c+=1
################################################################################################################################
################################################################################################################################
def Gramaticatokeni(c):
    global listaSintactico, listatokens
    if listatokens[c][1] == 'i':
        if listatokens[c+1][1] == 'm':
            if listatokens[c+2][1] == 'p':
                if listatokens[c+3][1] == 'r':
                    if listatokens[c+4][1] == 'i':
                        if listatokens[c+5][1] == 'm':
                            if listatokens[c+6][1] == 'i':
                                if listatokens[c+7][1] == 'r':
                                    if listatokens[c+8][1] == '(':
                                        c = GramaticaEspecialtextoentreparentesisycomillas(c+8,'imprimir')
                                    else:
                                        if listatokens[c+8][1] == 'l':
                                            if listatokens[c+9][1] == 'n':
                                                if listatokens[c+10][1] == '(':
                                                    c = GramaticaEspecialtextoentreparentesisycomillas(c+10,'imprimirln')
                                                else:
                                                    c = fininstruccion(c+10,'(')
                                            else:
                                                c = fininstruccion(c+9,'n')
                                        else:
                                            c = fininstruccion(c+8,'( | l ')
                                else:
                                    c = fininstruccion(c+7,'r')
                            else:
                                c = fininstruccion(c+6,'i')
                        else:
                            c = fininstruccion(c+5,'m')
                    else:
                        c = fininstruccion(c+4,'i')
                else:
                    c = fininstruccion(c+3,'r')
            else:
                c = fininstruccion(c+2,'p')
        else:
            c = fininstruccion(c+1,'m')
    
    return c

################################################################################################################################
def Gramaticatokend(c):
    global listaSintactico, listatokens
    if listatokens[c][1] == 'd':
        if listatokens[c+1][1] == 'a':
            if listatokens[c+2][1] == 't':
                if listatokens[c+3][1] == 'o':
                    if listatokens[c+4][1] == 's':
                        if listatokens[c+5][1] == '(':
                            if listatokens[c+6][1] == ')':
                                if listatokens[c+7][1] == ';':
                                    c = c+8
                                    listaSintactico.append(['datos',None])
                                else:
                                    c = fininstruccion(c+7,';')
                            else:
                                c = fininstruccion(c+6,')')
                        else:
                            c = fininstruccion(c+5,'(')
                    else:
                        c = fininstruccion(c+4,'s')
                else:
                    c = fininstruccion(c+3,'o')
            else:
                c = fininstruccion(c+2,'t')
        else:
            c = fininstruccion(c+1,'a')
    return c

################################################################################################################################
def Gramaticatokens(c):
    global listaSintactico, listatokens
    if listatokens[c][1] == 's':
        if listatokens[c+1][1] == 'u':
            if listatokens[c+2][1] == 'm':
                if listatokens[c+3][1] == 'a':
                    if listatokens[c+4][1] == 'r':
                        if listatokens[c+5][1] == '(':
                            c = GramaticaEspecialtextoentreparentesisycomillas(c+5,'sumar')
                        else:
                            c = fininstruccion(c+5,'(')
                    else:
                        c = fininstruccion(c+4,'r')
                else:
                    c = fininstruccion(c+3,'a')
            else:
                c = fininstruccion(c+2,'m')
        else:
            c = fininstruccion(c+1,'u')
    return c

################################################################################################################################
def Gramaticatokenm(c):
    global listaSintactico, listatokens
    if listatokens[c][1] == 'm':
        if listatokens[c+1][1] == 'a':
            if listatokens[c+2][1] == 'x':
                if listatokens[c+3][1] == '(':
                    c = GramaticaEspecialtextoentreparentesisycomillas(c+3,'maximo')
                else:
                    c = fininstruccion(c+3,'(')
            else:
                c = fininstruccion(c+2,'x')
        else:
            if listatokens[c+1][1] == 'i':
                if listatokens[c+2][1] == 'n':
                    if listatokens[c+3][1] == '(':
                        c = GramaticaEspecialtextoentreparentesisycomillas(c+3,'minimo')
                    else:
                        c = fininstruccion(c+3,'(')
                else:
                    c = fininstruccion(c+2,'n')
            else:
                c = fininstruccion(c+1,'a|i')
    return c

################################################################################################################################
def Gramaticatokenp(c):
    global listaSintactico, listatokens
    if listatokens[c][1] == 'p':
        if listatokens[c+1][1] == 'r':
            if listatokens[c+2][1] == 'o':
                if listatokens[c+3][1] == 'm':
                    if listatokens[c+4][1] == 'e':
                        if listatokens[c+5][1] == 'd':
                            if listatokens[c+6][1] == 'i':
                                if listatokens[c+7][1] == 'o':
                                    if listatokens[c+8][1] == '(':
                                        c = GramaticaEspecialtextoentreparentesisycomillas(c+8,'promedio')
                                    else:
                                        c = fininstruccion(c+8,'(')
                                else:
                                    c = fininstruccion(c+7,'o')
                            else:
                                c = fininstruccion(c+6,'i')
                        else:
                            c = fininstruccion(c+5,'d')
                    else:
                        c = fininstruccion(c+4,'e')
                else:
                    c = fininstruccion(c+3,'m')
            else:
                c = fininstruccion(c+2,'o')
        else:
            c = fininstruccion(c+1,'r')
    return c

################################################################################################################################
def GramaticaEspecialtextoentreparentesisycomillas(c,funcion):
    global listaSintactico, listatokens
    if listatokens[c][1] == '(':
        if listatokens[c+1][1] == '"':
            AFDTexto = AFDTextoentrecomillas(c+1)
            if AFDTexto == True:
                texto, a = obtenertexto(c+2)
                c = a
                if listatokens[c][1] == ')':
                    if listatokens[c+1][1] == ';':
                        c += 2
                        listaSintactico.append([funcion,texto])
                    else:
                        c = fininstruccion(c+1,';')
                else:
                    c = fininstruccion(c,')')
            else:
                c = ErrorAFDTextoentrecomillas(c+6,'"')
                c = fininstruccion(c,')')  
        else:
            c = fininstruccion(c+1,'"')
    else:
        c = fininstruccion(c,'(')
    
    return c

################################################################################################################################
################################################################################################################################


################################################################

def evaluartokens(tokens):
    global listaSintactico, listatokens
    listatokens = tokens
    print('\n####### [ EVALUAR TOKENS ] #######')
    #Iterador
    c = 0
    maxiteraciones = len(tokens)
    while c < maxiteraciones:
        Token = tokens[c][1]
        #//////////////////////////////////////////////////////////////////////////////////
        #Ignorar Comentarios
        if tokens[c][4] == 'Comentario_multilinea' or tokens[c][3] == 'Comentario_simple':
            c += 1    
        #[ m ] ///////////////////////////////////////////////////////////////////////////////
        elif Token == 'm':
            c = Gramaticatokenm(c)
        #[ d ] ///////////////////////////////////////////////////////////////////////////////
        elif Token == 'd':
            c = Gramaticatokend(c)
        #[ i ] ///////////////////////////////////////////////////////////////////////////////
        elif Token == 'i':
            c = Gramaticatokeni(c)
        #[ p ] ///////////////////////////////////////////////////////////////////////////////
        elif Token == 'p':
            c = Gramaticatokenp(c)
        #[ s ] ///////////////////////////////////////////////////////////////////////////////
        elif Token == 's':
            c = Gramaticatokens(c)
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


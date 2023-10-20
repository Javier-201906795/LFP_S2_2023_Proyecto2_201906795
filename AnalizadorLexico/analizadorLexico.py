

from tkinter import messagebox as MessageBox





tokens = []
linea = 1
columna = 1
listaerrores = []
listadocaracteresbuscados = ['{','}',':','[',']',',','(',')',';','=','"',"'",'#','_','-']
listaabecedario = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','Ñ','ñ']







################################################################
def evaluartexto(texto):
    global tokens, linea, columna, listaerrores, listadocaracteresbuscados
    #Iterador
    c=0
    #Numero maximo de iteraciones
    maxiter = len(texto)
    while c < maxiter:
        #Obtener caracter
        caracter = texto[c]
        #Evaluar
        #//////////////////////////////////////////////////////////////////////////////////
        if caracter.isspace():
            #Si es algun tipo de espacio
            if caracter == '\n':
                #Si es un Salto de linea | Aumenta la linea | Reinicia columnas
                linea += 1
                columna = 1
            elif caracter == '\t':
                #Si es un Tabulador | Aumenta la columna en 4
                columna += 4
            else:
                #Si es un espacio | Aumenta la columna
                columna += 1
            #Contador
            c += 1
        #//////////////////////////////////////////////////////////////////////////////////
        elif caracter in listadocaracteresbuscados:
            #Almacena token
            tokens.append([caracter,linea,columna,'token',linea, columna])
            print('token: ', caracter, ' linea:', linea,' columna: ',columna)
            #Aumenta columna
            columna += 1
            #Contador
            c += 1
        #//////////////////////////////////////////////////////////////////////////////////
        elif caracter in listaabecedario:
            #Almacena token
            tokens.append([caracter,linea,columna,'token',linea, columna])
            print('token: ', caracter, ' linea:', linea,' columna: ',columna)
            #Aumenta columna
            columna += 1
            #Contador
            c += 1
        #//////////////////////////////////////////////////////////////////////////////////
        elif caracter.isdigit():
            #Guardar inicio
            templinea = linea
            tempcolumna = columna
            #Obtener numero
            textoaevaluar = texto[c:]
            numero, pos = obtenernumero(textoaevaluar, c)
            #Aumentar contador y columna
            c = pos
            txtnumero = str(numero) 
            columna += len(txtnumero) + 1
            #Almacenar token
            tokens.append([numero,templinea, tempcolumna,'Numero',linea,columna])
            print('token: ', numero, ' linea:', linea,' columna: ',columna)
        #//////////////////////////////////////////////////////////////////////////////////
        else:
            #Caracter Desconocido
            print("\033[1;31;40m Error: caracter desconocido:", caracter," |Linea:",linea," |Columna:",columna,"\033[0m")
            #Almacenar error
            listaerrores.append([caracter, linea, columna,'error lexico'])
            #Aumentar contador y columna
            c += 1
            columna += 1




################################################################
def obtenernumero(texto, a):
    numero = ""
    isDecimal = False
    for newcaracter in texto:
        if newcaracter.isdigit():
            numero += newcaracter
            a += 1
        elif newcaracter == "." and not isDecimal:
            numero += newcaracter
            a += 1
            isDecimal = True
        else:
            break
    if isDecimal:
        return [float(numero), a]
    return [int(numero), a]



################################################################
def imprimirerroreslexicos():
    print('######### [ ERRORES LEXICOS ] #########\n')
    for i in listaerrores:
        print(i)

################################################################
def imprimirlistatokens():
    print('######### [ TOKENS ] ##########\n')
    for i in tokens:
        print(i)
################################################################
def GetErrores():
    return listaerrores

################################################################
def GetTokens(texto):
    #Validar tamaño del texto
    if len(texto) < 0:
        MessageBox.showerror('Error - lexico()','No hay informacion necesarioa para procesarlo')
        return
    #Reiniciar valores
    global tokens, linea, columna, listaerrores
    tokens = []
    linea = 1
    columna = 1
    listaerrores = []
    #Analizar Texto
    evaluartexto(texto)
    
    
    return tokens

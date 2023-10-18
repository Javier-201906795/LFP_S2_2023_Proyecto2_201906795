

from tkinter import messagebox as MessageBox





tokens = []
linea = 1
columna = 1
listaerrores = []
listadocaracteresbuscados = ['{','}',':','[',']',',']
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
            #Aumenta columna
            columna += 1
            #Contador
            c += 1
            #Almacena token
            tokens.append([caracter,linea,columna,'token',linea, columna])
            print('token: ', caracter, ' linea:', linea,' columna: ',columna)
        #//////////////////////////////////////////////////////////////////////////////////
        elif caracter in listaabecedario:
            #Aumenta columna
            columna += 1
            #Contador
            c += 1
            #Almacena token
            tokens.append([caracter,linea,columna,'token',linea, columna])
            print('token: ', caracter, ' linea:', linea,' columna: ',columna)
        #//////////////////////////////////////////////////////////////////////////////////
        elif caracter == '"' or caracter == "'":
            #Guardar inicio
            templinea = linea
            tempcolumna = columna
            #Evaluar si es un comentario multilinea
            caractersig = texto[c+1:c+2]
            if caractersig == '"' or caractersig == "'":
                caractersig2 = texto[c+2:c+3]
                if caractersig2 == '"' or caractersig2 == "'":
                    print('Comentario multilinea')
                    #obtener texto entre comillas
                    textoaevaluar = texto[c+3:]
                    string, pos, lineasextra, columnastring = obtenercomentariomultilinea(textoaevaluar, c,columna)
                    #Aumentar contador y columna
                    c = pos + 4
                    columna = columnastring
                    linea = linea + lineasextra
                    #Almacenar token
                    tokens.append([string,templinea,tempcolumna,'Comentario_multilinea',linea, columna])
                    print('token: ', string, ' linea:', linea,' columna: ',columna)
            #//////////////////////////////////////////////////////////////////////////////////
            else:
                #obtener texto entre comillas
                textoaevaluar = texto[c+1:]
                string, pos = obtenertexto(textoaevaluar, c)
                #Aumentar contador y columna
                c = pos + 2
                columna = len(string) + 1
                #Almacenar token
                tokens.append([string,templinea,tempcolumna,'Texto',linea, columna])
                print('token: ', string, ' linea:', linea,' columna: ',columna)
        #//////////////////////////////////////////////////////////////////////////////////
        elif caracter == '#':
            #Guardar inicio
            templinea = linea
            tempcolumna = columna
            #Si es un texto un posible token
            textoaevaluar = texto[c+1:]
            string, pos = obtenercomentario(textoaevaluar, c)
            #Aumentar contador y columna
            c = pos + 1
            columna = len(string) + 1
            #Almacenar token
            tokens.append([string,templinea,tempcolumna,'Comentario_simple',linea, columna])
            print('token: ', string, ' linea:', linea,' columna: ',columna)
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
            #Aumentar contador y columna
            c += 1
            columna += 1
            #Caracter Desconocido
            print("\033[1;31;40m Error: caracter desconocido:", caracter," |Linea:",linea," |Columna:",columna,"\033[0m")
            #Almacenar error
            error = [caracter, linea, columna,'error lexico']
            listaerrores.append([error,linea,columna])


################################################################
def obtenertexto(text, a):
    #Texto
    string = ''
    #Evaluar caracter por carcater
    for newcaracter in text:
        if newcaracter == '"':
            #Si encuntra el cierre "
            return [string, a]
        #Forma el texto
        string += newcaracter
        a += 1
    print("Error: No se encontraron comillas doble que cerraran el texto.")

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
def obtenercomentario(text, a):
    #Texto
    string = ''
    #Evaluar caracter por carcater
    for caracter in text:
        if caracter == '\n':
            return [string, a]
        #Forma el texto
        string += caracter
        a += 1
    print("Error: No al obtenrecomentario().")

################################################################
def obtenercomentariomultilinea(text, a, columna):
    #Texto
    string = ''
    lineasextra = 0
    #Evaluar caracter por carcater
    c = 0
    for newcaracter in text:
        columna += 1
        if newcaracter == "\n":
            lineasextra +=1
            columna = 1
        elif newcaracter == '"' or newcaracter == "'":
            caractersig = text[c+1:c+2]
            if caractersig == '"' or caractersig == "'":
                caractersig2 = text[c+2:c+3]
                if caractersig2 == '"' or caractersig2 == "'":
                    columna += 1
                    a += 2            
                    return [string, a, lineasextra, columna]
        #Forma el texto
        string += newcaracter
        a += 1
        c += 1
    print("Error: No se encontraron comillas doble que cerraran el texto.")






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
    #Imprimir tokens
    print('##########################\n')
    for i in tokens:
        print(i)
    
    return tokens

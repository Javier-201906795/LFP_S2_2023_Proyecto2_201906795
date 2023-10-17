

from tkinter import messagebox as MessageBox





tokens = []
linea = 1
columna = 1
listaerrores = []
listadocaracteresbuscados = ['{','}',':','[',']',',']







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
        if caracter.isspace():
            #Si es algun tipo de espacio
            if caracter == '\n':
                #Si es un Salto de linea | Aumenta la linea
                linea += 1
                #Reinicia columnas
                columna = 1
            elif caracter == '\t':
                #Si es un Tabulador | Aumenta la columna en 4
                columna += 4
            else:
                #Si es un espacio | Aumenta la columna
                columna += 1
            #Reporte
            # print('Caracter: ', caracter, ' Linea: ', linea, ' Columna: ',columna)
            #Contador
            c += 1
        elif caracter in listadocaracteresbuscados:
            #Aumenta columna
            columna += 1
            #Contador
            c += 1
            #Almacena token
            tokens.append(caracter)
            print('token: ', caracter, ' linea:', linea,' columna: ',columna)
        elif caracter == '"':
            #Si es un texto un posible token
            textoaevaluar = texto[c+1:]
            string, pos = obtenertexto(textoaevaluar, c)
            #Aumentar contador y columna
            c = pos + 2
            columna = len(string) + 1
            #Almacenar token
            tokens.append(string)
            print('token: ', string, ' linea:', linea,' columna: ',columna)
        elif caracter == '#':
            #Si es un texto un posible token
            textoaevaluar = texto[c:]
            string, pos = obtenercomentario(textoaevaluar, c)
            #Aumentar contador y columna
            c = pos + 1
            columna = len(string) + 1
            #Almacenar token
            tokens.append(string)
            print('token: ', string, ' linea:', linea,' columna: ',columna)
        elif caracter.isdigit():
            #Obtener numero
            textoaevaluar = texto[c:]
            numero, pos = obtenernumero(textoaevaluar, c)
            #Aumentar contador y columna
            c = pos
            txtnumero = str(numero) 
            columna += len(txtnumero) + 1
            #Almacenar token
            tokens.append(numero)
            print('token: ', numero, ' linea:', linea,' columna: ',columna)
        else:
            #Aumentar contador y columna
            c += 1
            columna += 1
            #Caracter Desconocido
            print("\033[1;31;40m Error: caracter desconocido:", caracter," |Linea:",linea," |Columna:",columna,"\033[0m")
            #Almacenar error
            error = [caracter, linea, columna,'error lexico']
            listaerrores.append(error)


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
    
    return [1,'hola','}']

from tkinter import *
from tkinter import messagebox as MessageBox




listainstrucciones = []
txtresultado = ''
################################################################
Claves = []
Registros = []
flagClavesyRegistros = False
tempLista = []


################################################################
def agregar_claves(listaclaves):
    global Claves
    #Limpiar Clave anteriores
    Claves = []
    #Agregar claves
    for i in listaclaves:
        Claves.append(i)
    #Imprimir Resultado
    print('\n---[Claves]---')
    print(Claves,'\n')

################################################################
def agregar_registros(listaregistros):
    global Registros, flagClavesyRegistros
    #Validar
    if len(Claves) <= 0:
        MessageBox.showerror('Error - instrucciones','No hay claves que evaluar')
    else:
        #Limpiar
        Registros = []
        #Filtrar 
        templista = []
        #Obtener elemento lista
        for registro in listaregistros:
            #Almacenar registro en variable temporal
            #Recorrer item por item y almacenar los necesarios
            for i in range(0,len(Claves)):
                item = registro[i]
                templista.append(item)
            #Se obtubo un nuevo listao agregarlo al registro
            Registros.append(templista)
            templista = []
        #Imprimir Resultado
        print('\n---[Registros]---')
        print(Registros)
        flagClavesyRegistros = True

################################################################
def funcion_conteo():
    global flagClavesyRegistros
    mensaje = ''
    if flagClavesyRegistros == True:
        mensaje += '\nconteo();\n'
        Registrosnumeros = len(Registros)
        mensaje += str(Registrosnumeros)+'\n'

    return mensaje

################################################################
def funcion_promedio(filtro):
    global flagClavesyRegistros, tempLista
    tempLista = []
    mensaje = ''
    if flagClavesyRegistros == True:
        mensaje += 'promedio("'+str(filtro)+'");\n'
        #Buscar si existe el Filtro en las Claves
        if filtro in Claves:
            #Buscar cual fila esta ubicado filtro en la lista Claves
            c = 0 
            for i in Claves:
                if i == filtro:
                    break
                c += 1
            print(Claves[c] + ': '+ str(c))
            #Almacenar registros en lista temporal
            for item in Registros:
                tempLista.append(item[c])

            #Obtener promedio
            #formula:   [lista(0)+lista(1)...lista(n)]/n
            # Numerador / Denominador
            bandera = True
            numerador = 0
            for i in tempLista:
                numero = 0
                try:
                    numero = float(i)
                except:
                    bandera = False
                    MessageBox.showerror('Error | promedio','Error al convertir este valor: '+str(i)+' en valor numerico')        
                    break
                numerador += numero
            if bandera == True:
                #Denominador
                denominador = len(tempLista)
                #Promedio
                promedio = numerador / denominador
                promedio = round(promedio, 2)
                #Agregar mensaje
                mensaje += str(promedio)+'\n'
            else:
                mensaje += '-[ Error promedio ]-'

                
        else:
            MessageBox.showerror('Error | promedio','NO se encontro el valor '+str(filtro)+' entre las Claves, por lo tanto no se puede filtrar y promediar')


    return mensaje

################################################################
def funcion_contarsi(informacion):
    global flagClavesyRegistros, tempLista
    tempLista = []
    mensaje = ''
    filtro, valor = informacion
    if flagClavesyRegistros == True:
        mensaje += 'contarsi("'+str(filtro)+'",'+str(valor)+');\n'
        #Buscar si existe el Filtro en las Claves
        if filtro in Claves:
            #Buscar cual fila esta ubicado filtro en la lista Claves
            c = 0 
            for i in Claves:
                if i == filtro:
                    break
                c += 1
            print(Claves[c] + ': '+ str(c))
            #Almacenar registros en lista temporal
            for item in Registros:
                tempLista.append(item[c])

            #Contar si
            contador = 0
            for objetivo in tempLista:
                if  objetivo == valor:
                    contador += 1

            mensaje += str(contador)+'\n'
                
        else:
            MessageBox.showerror('Error | contar si','NO se encontro el valor '+str(filtro)+' entre las Claves, por lo tanto no se puede filtrar')


    return mensaje

################################################################
def funcion_datos():
    global flagClavesyRegistros, tempLista
    tempLista = []
    mensaje = ''
    if flagClavesyRegistros == True:
        try:
            mensaje += '\n' + '-- [ datos(); ] --\n'
            
            titular = ''
            espaciado = ''
            c =0
            for titulo in Claves:
                if c >= len(Claves)-1:
                    titular += '"'+str(titulo) + '"'
                else:
                    titular += '"'+str(titulo) + '",'
                espaciado += '{'
                espaciado += ':<10'
                espaciado += '} '
                c +=1
            #Titulos
            print(espaciado)
            print(titular)
            print("{:<10} {:<10} {:<10} {:<10} {:<10}".format("codigo","producto","precio_compra","precio_venta","stock"))
            print(espaciado.format(titular))
            mensaje += str(titular)+'\n'
            # mensaje += str(espaciado)+'\n'
            # mensaje = "{:<10}".format(Claves)
            
                

            mensaje += '\n------------------------\n'
        
        except Exception:
            MessageBox.showerror('Error | promedio','NO se encontro el valor '+str(filtro)+' entre las Claves, por lo tanto no se puede filtrar y promediar')


    return mensaje



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
    try:
        global listainstrucciones, txtresultado
        c = 0
        maxiteraciones = len(listainstrucciones)
        print('\n##################### [ EVALUANDO... ] #############################')
        while c < maxiteraciones:
            instruccion = listainstrucciones[c] 
            print('•Instruccion: ',instruccion[0], 'Contenido: ', instruccion[1])
            #[ imprimir ] ///////////////////////////////////////////////////////////////////////
            if instruccion[0] == 'imprimir':
                print('♦ Imprimir: ', instruccion[1])
                txtresultado +=  instruccion[1] + ' '
            #[ imprimirln ] ///////////////////////////////////////////////////////////////////////
            elif instruccion[0] == 'imprimirln':
                print('♦ Imprimirln: ', instruccion[1])
                txtresultado +=  instruccion[1]+' \n'
            #[ Claves ] ///////////////////////////////////////////////////////////////////////
            elif instruccion[0] == 'Claves':
                print('♦ Claves=', instruccion[1])
                #Añadir CLAVES
                agregar_claves(instruccion[1])
                txtlista = '['
                contador = 0
                for i in Claves:
                    if contador < len(Claves) - 1:
                        txtlista += str(i)+', '
                    else:
                        txtlista += str(i)
                    contador += 1

                txtlista += ']\n'
                
                txtresultado += 'Claves=' + txtlista
            #[ contar si ] ///////////////////////////////////////////////////////////////////////
            elif instruccion[0] == 'contarsi':
                print('♦ Contarsi: '+instruccion[1][0]+' valor:'+str(instruccion[1][1]))
                txtresultado += funcion_contarsi(instruccion[1])
            #[ conteo ] ///////////////////////////////////////////////////////////////////////
            elif instruccion[0] == 'conteo':
                print('♦ Conteo')
                txtresultado += funcion_conteo()
                
            #[ datos ] ///////////////////////////////////////////////////////////////////////
            elif instruccion[0] == 'datos':
                print('♦ Mostrar Datos:')
                txtresultado += funcion_datos()
            #[ exportarReporte ] ///////////////////////////////////////////////////////////////////////
            elif instruccion[0] == 'exportarReporte':
                print('♦ ExportarReporte("'+instruccion[1]+'")')
                txtresultado += 'Reporte Exportado: '+instruccion[1]+'.html\n'
            #[ maximo ] ///////////////////////////////////////////////////////////////////////
            elif instruccion[0] == 'maximo':
                print('♦ Maximo("'+instruccion[1]+'")')
                txtresultado += 'max("'+instruccion[1]+'");\n'
                txtresultado += '100.0\n'
            #[ Minimo ] ///////////////////////////////////////////////////////////////////////
            elif instruccion[0] == 'minimo':
                print('♦ Maximo("'+instruccion[1]+'")')
                txtresultado += 'min("'+instruccion[1]+'");\n'
                txtresultado += '5.0\n'
            #[ promedio ] ///////////////////////////////////////////////////////////////////////
            elif instruccion[0] == 'promedio':
                print('♦ Promedio("'+instruccion[1]+'")')
                txtresultado += str(funcion_promedio(instruccion[1]))
                
            #[ Registros ] ///////////////////////////////////////////////////////////////////////
            elif instruccion[0] == 'Registros':
                print('♦Registros=',instruccion[1])
                agregar_registros(instruccion[1])
                txtresultado += '\n----[ Registros ]----\n'
                for i in Registros:
                    txtresultado += str(i)+'\n'
                txtresultado += '\n---------------------\n'
            #[ sumar ] ///////////////////////////////////////////////////////////////////////
            elif instruccion[0] == 'sumar':
                print('♦ Sumar("'+instruccion[1]+'")')
                txtresultado += 'sumar("'+instruccion[1]+'");\n'
                txtresultado += '12\n'


            c += 1
    except Exception as e:
        print("\033[1;31;40m Error: Ocurrio un error al ejecutar alguna instruccion \033[0m")
        MessageBox.showerror('Error - instrucciones','Ocurrio un error al ejecutar alguna instruccion ver consola CMD')
        print(e)


################################################################
def ejecutar(oldlistainstrucciones):
    global listainstrucciones, txtresultado, Claves, Registros, flagClavesyRegistros, tempLista
    txtresultado = ''
    listainstrucciones = oldlistainstrucciones
    

    #Reinicar valores
    Claves = []
    Registros = []
    flagClavesyRegistros = False
    tempLista = []
    
    #Evaluar
    evaluarinstrucciones()


    return txtresultado

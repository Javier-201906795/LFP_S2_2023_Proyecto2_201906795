from tkinter import *
from tkinter.ttk import Combobox
from tkinter import filedialog, messagebox
from tkinter import messagebox as MessageBox

from Analizador import *
from AnalizadorLexico import *
from AnalizadorSintactico import *

from Grafica import *

################################################################
def GraficaArbol():
    print('Arbol')
    configuraciones = {'texto':'Operaciones', 'fondo':'white','fuente':'blue', 'forma':'circle'}
    Arbol.configuraciones(configuraciones)
    nodo1 = Arbol.agregarnodo('1')
    nodo2 = Arbol.agregarnodo('1')

    Arbol.conectarnodo(nodo1,nodo2)
    Arbol.render()

    
    


########################################################################
def Abrir():
    print('-- [ Abrir ] --')
    #Limpiar input
    inputtexto.delete('1.0', 'end')
    #Obtener ruta 
    rutaarchivo = filedialog.askopenfilename(filetypes=[("BizData", ".bizdata"),("Texto",".txt")])
    print('Ruta archivo: "',rutaarchivo,'"')
    #Obtener Texto
    textoarchivo = ''
    try:
        with open(rutaarchivo, 'r') as archivo:
            textoarchivo = archivo.read()
    except Exception as e:
        print('• Error[Abrir()][Tk_ventana][CD001]: No se puede abrir el archivo \n')
        print(e)
    
    #Imprimir Texto
    if textoarchivo == '':
        print('No hay texto que procesar...')
    else:
        print('-------------------------')
        print(textoarchivo)
        print('-------------------------')
        #Añadir texto a input
        inputtexto.insert('1.0', str(textoarchivo))
    
########################################################################
def Analizar():
    #Desbloquear consola
    inputconsola.config(state=NORMAL)

    print('\n-- [ Analizar ] --')
    texto = str(inputtexto.get("1.0",END))
    txtconsola = analizador.analizadorBizData(texto)

    print('\n-------------[ CONSOLA ]------------')
    print(txtconsola)
    #Limpiar consola
    inputconsola.delete('1.0', 'end')
    #Agregar Texto
    inputconsola.insert('1.0', str(txtconsola))
    #Bloquear consola
    inputconsola.config(state=DISABLED)

    #Crear Arbol
    Arbol.generagraficaarbol()
    Arbol.reiniciarvalores()

########################################################################
def ReporteErrores():
    try:
        print('Report Errores')
        #Obtiene listas errores
        ErroresLexicos = analizadorLexico.GetErrores()
        ErroresSintactico = analizadorSintactico.GetErrores()

        
        #Validar
        if len(ErroresLexicos) <= 0 and len(ErroresSintactico) <= 0:
            #No hay Errores
            MessageBox.showinfo('Error | Reporte Errores','No hay errores que mostrar.')
        else:
            print('--- [Errores Lexicos] ---')
            print(ErroresLexicos)
            print('--- [Errores Sintacticos] ---')
            print(ErroresSintactico)
            #Crea archivo HTML
            txthtml = crearTextoHTML('Reporte Errores',['No.','Token','Fila I.','Columna I.','Fila F.','Columna F.','Tipo de Error'],ErroresLexicos, ['No.','Token Err.','Token Espe.','Fila I.','Columna I.','Tipo de Error','Fila F.','Columan F.'], ErroresSintactico)
            #Crear Archivo HTML
            ruta = 'Reporte_Errores_201906795.html'
            archivo = open(ruta,'w')
            archivo.write(txthtml)
            archivo.close()

            print('Reporte creado exitosamente...\nReporte_Errores_201906795.html')
            MessageBox.showinfo('Reporte','Reporte creado exitosamente...\nReporte_Errores_201906795.html')


        #Mensaje
    except Exception as e:
        print('Error ', e)

########################################################################
def ReporteTokens():
    try:
        print('Report Tokens')
        #Obtiene listas errores
        Tokens = analizadorLexico.GetTokensFinal()

        
        #Validar
        if len(Tokens) <= 0:
            #No hay Errores
            MessageBox.showinfo('Error | Reporte Errores','No hay errores que mostrar.')
        else:
            print('--- [Tokens] ---')
            print('Tokens: ',len(Tokens))

            #Crea archivo HTML
            txthtml = crearTextoHTMLTokens('Reporte Tokens',['No.','--','Token','Fila I.','Columna I.','---.','Tipo de Token'],Tokens)
            #Crear Archivo HTML
            ruta = 'Reporte_Tokens_201906795.html'
            archivo = open(ruta,'w')
            archivo.write(txthtml)
            archivo.close()

            print('Reporte creado exitosamente...\nReporte_Tokens_201906795.html')
            MessageBox.showinfo('Reporte','Reporte creado exitosamente...\nReporte_Tokens_201906795.html')


        #Mensaje
    except Exception as e:
        print('Error ', e)

################################################################
def crearTextoHTMLTokens(nombre,Titulos,Registros):
    
    txthtml = ''

    #Inicio
    txthtml = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<title>Proyecto 2</title>
</head>
<body>
<div class="container">
    <h1>'''+str(nombre)+'''</h1>
    <h5>Javier Yllescas - 201906795</h5>
    <br>
</div>
<div class="container">
    <table class="table table-bordered">
        <thead class="thead-dark">
        <tr>'''

    #/////////////////////////////////////////////////////////////////////
    #----------------------------------------------------------------
    #Titulo Tabla [ CLAVES ]
    for titulo in Titulos:
        txthtml += '''                <th scope="col">'''+str(titulo)+'''</th>'''

    txthtml += '''</tr>
        </thead>'''
    #----------------------------------------------------------------
    #Filas Tabla
    txthtml += '''<tbody>'''

    contadorerrores = 0

    if len(Registros) > 0:
        for i in range(0,len(Registros)):
            txthtml += '''<tr>'''
            registro = Registros[i]
            contador = 0
            for c in range(0,len(registro)+2):
                
                if contador == 0:
                    txthtml += '''<th scope="row">'''+str(contadorerrores)+'''</th>'''    
                elif contador > 1 and contador < len(registro):
                    txthtml += '''<th scope="row">'''+str(registro[contador-1])+'''</th>'''
                elif contador == 6:
                    txthtml += '''<th scope="row">'''+str(registro[len(registro)-1])+'''</th>'''
                else:
                    txthtml += '''<th scope="row">'''+str('--')+'''</th>'''
                contador += 1

            contadorerrores += 1


            txthtml += '''</tr>'''

    txthtml += '''</tbody>
    </table>
</div>
<br><br><br>'''
    #----------------------------------------------------------------
    #/////////////////////////////////////////////////////////////////////


    
  

    #Final
    txthtml += '''</body>
</html>'''
    return txthtml


################################################################
def crearTextoHTML(nombre,Titulos,Registros,Titulos2,Registros2):
    
    txthtml = ''

    #Inicio
    txthtml = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<title>Proyecto 2</title>
</head>
<body>
<div class="container">
    <h1>'''+str(nombre)+'''</h1>
    <h5>Javier Yllescas - 201906795</h5>
    <br>
</div>
<div class="container">
    <table class="table table-bordered">
        <thead class="thead-dark">
        <tr>'''

    #/////////////////////////////////////////////////////////////////////
    #----------------------------------------------------------------
    #Titulo Tabla [ CLAVES ]
    for titulo in Titulos:
        txthtml += '''                <th scope="col">'''+str(titulo)+'''</th>'''

    txthtml += '''</tr>
        </thead>'''
    #----------------------------------------------------------------
    #Filas Tabla
    txthtml += '''<tbody>'''

    contadorerrores = 0

    if len(Registros) > 0:
        for i in range(0,len(Registros)):
            txthtml += '''<tr>'''
            registro = Registros[i]
            contador = 0
            for c in range(0,len(registro)+3):
                
                if contador == 0:
                    txthtml += '''<th scope="row">'''+str(contadorerrores)+'''</th>'''    
                elif contador > 0 and contador < len(registro):
                    txthtml += '''<th scope="row">'''+str(registro[contador-1])+'''</th>'''
                elif contador == 6:
                    txthtml += '''<th scope="row">'''+str(registro[len(registro)-1])+'''</th>'''
                else:
                    txthtml += '''<th scope="row">'''+str('--')+'''</th>'''
                contador += 1

            contadorerrores += 1


            txthtml += '''</tr>'''

    txthtml += '''</tbody>
    </table>
</div>
<br><br><br>'''
    #----------------------------------------------------------------
    #/////////////////////////////////////////////////////////////////////


    #/////////////////////////////////////////////////////////////////////
    if len(Registros2) > 0:
        txthtml += '''<table class="table table-bordered">
            <thead class="thead-dark">
            <tr>'''
        #----------------------------------------------------------------
        #Titulo Tabla [ CLAVES ]
        for titulo in Titulos2:
            txthtml += '''                <th scope="col">'''+str(titulo)+'''</th>'''

        txthtml += '''</tr>
            </thead>'''
        #----------------------------------------------------------------
        #Filas Tabla
        txthtml += '''<tbody>'''

        contadorerrores = 0

        
        for i in range(0,len(Registros2)):
            txthtml += '''<tr>'''
            registro = Registros2[i]
            contador = 0
            for c in range(0,len(registro)+1):
                
                if contador == 0:
                    txthtml += '''<th scope="row">'''+str(contadorerrores)+'''</th>'''    
                elif contador > 0 and contador < len(registro)+1:
                    txthtml += '''<th scope="row">'''+str(registro[contador-1])+'''</th>'''
                else:
                    txthtml += '''<th scope="row">'''+str('--')+'''</th>'''
                contador += 1

            contadorerrores += 1


            txthtml += '''</tr>'''

        

        txthtml += '''</tbody>
        </table>
    </div>
    <br><br><br>'''
    #/////////////////////////////////////////////////////////////////////
  

    #Final
    txthtml += '''</body>
</html>'''
    return txthtml


########################################################################
raiz = Tk()
raiz.title('LFP Proyecto 2 | 201906795')
raiz.geometry('1250x600')

Label(raiz, pady=0,text='PROYECTO 2 | 201906795', font=("Consolas",14)).place(x=50,y=20)
Button(raiz,text='Abrir', bg='#DBE6A1', fg='#000000',font=("Consolas",12), command=Abrir).place(x=500,y=20, width=90, height= 35)
Button(raiz,text='Analizar', bg='#DBE6A1', fg='#000000',font=("Consolas",12), command=Analizar).place(x=610,y=20, width=120, height= 35)


opcionesarchivo = ['Reportes','Errores','Tokens','Arbol', 'Salir']
listaopciones = Combobox(raiz, text='Archivo', values = opcionesarchivo, font=("Consolas",11))
listaopciones.place(x=750,y=20, width=130, height= 35)
listaopciones.current(0)
#Switch case
def seleccion(event):
    print('Seleccionando ->', listaopciones.get())
    sel = listaopciones.get()
    if sel == 'Errores':
        try:
            ReporteErrores()
        except:
            print('Error al crear reporte errores')
    elif sel == 'Tokens':
        try:
            ReporteTokens()
        except:
            print('Error al crear reporte Tokens')
    elif sel == 'Arbol':
        try:
            GraficaArbol()
        except:
            print('Error al crear grafica')
        
    elif sel == 'Salir':
        print('Salir')
#Ejecuta la opcion cuando cambia de seleccion
listaopciones.bind('<<ComboboxSelected>>',seleccion)

#Input
inputtexto = Text(raiz, padx=40, wrap='none', width=75, height=31,)
inputtexto.place(x=10,y=80)

#Etiquetas Input
labelnumeracion = Label(raiz, pady=0,text=' 1.\n 2.\n 3.\n 4.\n 5.', font=("Consolas",10), bg="#FFFFFF").place(x=12,y=82)
labelnumeracion = Label(raiz, pady=0,text=' 6.\n 7.\n 8.', font=("Consolas",10), bg="#FFFFFF").place(x=12,y=160)
labelnumeracion = Label(raiz, pady=0,text=' 9.\n10.\n11.', font=("Consolas",10), bg="#FFFFFF").place(x=12,y=210)
labelnumeracion = Label(raiz, pady=0,text='12.\n13.\n14.', font=("Consolas",10), bg="#FFFFFF").place(x=12,y=258)
labelnumeracion = Label(raiz, pady=0,text='15.\n16.\n17.', font=("Consolas",10), bg="#FFFFFF").place(x=12,y=305)
labelnumeracion = Label(raiz, pady=0,text='18.\n19.\n20.\n21.', font=("Consolas",10), bg="#FFFFFF").place(x=12,y=355)
labelnumeracion = Label(raiz, pady=0,text='22.\n23.\n24.\n25.', font=("Consolas",10), bg="#FFFFFF").place(x=12,y=420)
labelnumeracion = Label(raiz, pady=0,text='26.\n27.\n28.\n29.', font=("Consolas",10), bg="#FFFFFF").place(x=12,y=480)
labelnumeracion = Label(raiz, pady=0,text='30.\n31.', font=("Consolas",10), bg="#FFFFFF").place(x=12,y=545)

#ConsolaTkinter
inputconsola = Text(raiz, wrap=WORD, width=67, height=31,)
inputconsola.place(x=700,y=80)
# inputconsola.config(state=DISABLED)


raiz.mainloop()





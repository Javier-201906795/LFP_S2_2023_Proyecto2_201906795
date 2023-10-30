# Manual Tenico

### Expresion Regular
Una experesion regular, representa unos patrones que son utilizados para encontrar un determinada combinacion de caracteres dentro de una cadena de texto.

### Metodo del arbol
Es una forma de represtar una gramatica. Sirven para genera automatas para resolver la gramatica de una manera efectiva.

## Gramatica
Es una estrucutra logica-matematica con un cojunto de reglas de formacion que definan las cadenas de caracteres admisibles en un determinado lenguaje formal.
---
## Gramatica central
Apartir de la siguiente imagen dependiendo del primer caracter apunta a un gramatica diferente.


![ventana](/1_Arbol_JFLAP/Arbol_1_Central.PNG)

# Token C (mayuscula)
### Gramatica:
![ventana](/1_Arbol_JFLAP/Arbol_Letra_C.png)

# Token c (minuscula)
### Gramatica:
![ventana](/1_Arbol_JFLAP/Arbol_Letra_c2.png)

# Token d 
### Gramatica:
![ventana](/1_Arbol_JFLAP/Arbol_Letra_d.PNG)

# Token e
### Gramatica:
![ventana](/1_Arbol_JFLAP/Arbol_Letra_e.png)

# Token i
### Gramatica:
i•m•p•r•i•m•i•r•('('•"•Letra+|Numero*|simbolo*)|l•n•'('•")•')'•;
![ventana](/1_Arbol_JFLAP/Arbol_Letra_i.PNG)

# Token m
### Gramatica:
![ventana](/1_Arbol_JFLAP/Arbol_Letra_m.PNG)

# Token p
### Gramatica:
![ventana](/1_Arbol_JFLAP/Arbol_Letra_p.PNG)

# Token R (mayuscula)
### Gramatica:
![ventana](/1_Arbol_JFLAP/Arbol_Letra_R.png)

# Token s
### Gramatica:
![ventana](/1_Arbol_JFLAP/Arbol_Letra_s.png)

---
# Gramatica Especiales
### Gramatica Texto entre parentesis y comillas dobles:
![ventana](/1_Arbol_JFLAP/Gramatica_Especial_Textoentreparentesisycomillas.PNG)

### Gramatica Listas(Texto|Numeros) entre Corchetes y Llaves:
![ventana](/1_Arbol_JFLAP/Gramatica_R.png)

# Automata Finito Determinsta (AFD)
# AFD Texto entre comillas

Gramatica Identificadora de TEXTO entre comillas dobles<br>
SIMBOLOS = {{,},:,[,],",",(,),;,=,",',#,_,-}<br>
NUMEROS ={0,1,2,3...9}<br>
LETRAS = {A,a,B,b,C,c...Z,z}<br>
TEXTO = {LETRAS, NUMEROS, SIMBOLOS}<br>
<br>
### Gramatica:<br>
###  “•LETRAS+•NUMEROS*•SIMBOLOS*•”
<br>
Terminales: {",LETRAS,NUMEROS,SIMBOLOS}<br>
NO Terminales: {q0,q1,q2,q3,q4,q5}<br>
Inicio: {q0}<br>
Fin: {q5}<br>

![ventana](/1_Arbol_JFLAP/Automata_Finito_Determinista_TEXTO_ARBOL.PNG)
![ventana](/1_Arbol_JFLAP/Automata_Finito_Determinista_TEXTO_TABLA.PNG)
![ventana](/1_Arbol_JFLAP/Automata_Finito_Determinista_TEXTO_GRAFICA.PNG)

# AFD AUTOMATA [“TEXTO”,”TEXTO2”] 

<br>

![ventana](/1_Arbol_JFLAP/AFD_2.PNG)
![ventana](/1_Arbol_JFLAP/AFD_2_grafica.PNG)
![ventana](/1_Arbol_JFLAP/AFD_2_tablas.PNG)
![ventana](/1_Arbol_JFLAP/AFD_2_AFD.PNG)

---

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

# Estructura Proyecto 2 carpetas  y archivos

~~~
LFP_S2_2023_Proyecto1_201906795
├── 1_Arbol_JFLAP
│   └── Imagenes, AFD, Gramaticas para los manuales
├── Analizador
│   └── analizador.py
├── AnalizadorLexico
│   └── analizadorLexico.py
├── AnalizadorSintactico
│   └── analizadorSintactico.py
├── Funciones
│   └── funciones.py
├── z_Archivos_de_Prueba
│   └── Archivos para probar el programa .txt y .bizdata
├── Archivo de Prueba 2.bizdata
├── Manual_tecnico.md
├── Manual_usuario.md
├── Reporte_201906795.html
├── Reporte_Errores_201906795.html
├── Reporte_Tokens_201906795.html
└── Tk_ventana.py
~~~

---
## Estructura Programa

~~~
LFP_S2_2023_Proyecto1_201906795
├── Analizador
│   └── analizador.py
├── AnalizadorLexico
│   └── analizadorLexico.py
├── AnalizadorSintactico
│   └── analizadorSintactico.py
├── Funciones
│   └── funciones.py
└── Tk_ventana.py
~~~


## Tk_ventana.py

Interfaz grafica

![ventana](/1_Arbol_JFLAP/paso03.PNG)

Crear Archivos HTML

![ventana](/1_Arbol_JFLAP/paso13.PNG)
![ventana](/1_Arbol_JFLAP/paso15.PNG)

---

## analizador.py

![ventana](/1_Arbol_JFLAP/codigo01.PNG)

### A) Obtiene el listado de token de analizadorLexico.py
### B) Pasa los token al analizadorSintactico.py y obtiene informacin de gramaticas
### C) Ejecuta las instruccione en funciones.py
### D) Retorna la informacion Filtras a TK_ventana.py para mostrar en consola

---

## analizadorLexico.py

la siguiente funcion recive el texto y lo separa por caracteres
<br>
def evaluartexto(texto)
<br>
el cual busca en los siguientes listado similitudes y los alamcena
<br>
listadocaracteresbuscados = ['{','}',':','[',']',',','(',')',';','=','"',"'",'#','_','-','.']
<br>
listaabecedario = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z','Ñ','ñ']
<br>
y numeros
<br>

---

## analizadorSintactico.py

evalua cada token y si esta en los buscaos activa una gramatica para ver si esta en el lenguaje formal a obtener

![ventana](/1_Arbol_JFLAP/Arbol_1_Central.PNG)

<br>

![ventana](/1_Arbol_JFLAP/codigo02.PNG)
![ventana](/1_Arbol_JFLAP/codigo03.PNG)

---
<br><br><br><br><br><br><br><br>
<br><br><br><br><br><br><br><br>
ejemplo de gramatica

![ventana](/1_Arbol_JFLAP/codigo04.PNG)

<br><br><br><br><br><br><br><br>

## funciones.py
dependiendo la instruccion activaba la funcion  y devolvia un texto que se agregaba a la consola a Tk_ventan.py

![ventana](/1_Arbol_JFLAP/codigo05.PNG)
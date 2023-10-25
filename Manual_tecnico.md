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


# Automata Finito Determinsta (AFD)
## AFD Texto entre comillas

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
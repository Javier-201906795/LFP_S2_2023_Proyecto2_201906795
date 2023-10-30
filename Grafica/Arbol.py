from graphviz import *
from graphviz import Digraph


dot = None
cont = 0

def reiniciarvalores():
    global dot, cont
    cont = 0


def generagraficaarbol():
    global dot
    dot = Digraph('Grafica',filename='Grafica1', format='png')
    # dot.attr(rankdir='LR')

def configuraciones(configuraciones):
    global dot
    #dot.attr('node', shape='circle')
    fondocolor = configuraciones['fondo']
    letracolor = configuraciones['fuente']
    forma = configuraciones['forma']
    
    dot.attr(
            "node",
            style="filled",
            fillcolor=fondocolor,
            fontcolor=letracolor,
            shape=forma,
        )

def agregarnodo(label):
    global dot, cont
    cont += 1
    nodonombre = 'x' + str(cont) 
    dot.node(nodonombre,str(label))
    return nodonombre

def conectarnodo(nodo1,nodo2):
    global dot
    dot.edge(str(nodo1),str(nodo2))

def render():
    global dot
    dot.render('GraficaArbol', view=True)
    dot.save("GraficaArbol.dot")
    #dot -Tpng GraficaArbol.dot -o archivograph1.png
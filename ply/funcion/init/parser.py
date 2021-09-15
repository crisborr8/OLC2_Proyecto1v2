import ply.clases.clases as clase 
import ply.report.graficar as graph

start = 'init'

def p_init_vacio(t):
    'init   : '
    empty = clase.Nodo(graph.setHoja('empty'), None)
    t[0] = clase.Nodo(graph.setNodo('init', [empty.id]), None)

#---------------------------------------------------------------------
def p_init(t):
    'init   : instrucciones'

    t[0] = clase.Nodo(graph.setNodo('init', [t[1].id]), None)
    graph.saveGraph()

#---------------------------------------------------------------------
def p_instrucciones_l1(t):
    '''instrucciones    : instruccion'''

    t[0] = clase.Nodo(graph.setNodo('instrucciones', [t[1].id]), None)

#---------------------------------------------------------------------
def p_instrucciones_l2(t):
    'instrucciones    : instruccion instrucciones'

    t[0] = clase.Nodo(graph.setNodo('instrucciones', [t[1].id, t[2].id]), None)

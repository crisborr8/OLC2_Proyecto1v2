import ply.clases.clases as clase 
import ply.report.graficar as graph
import ply.funcion.init.ejecutar as ejec

start = 'init'

def p_init_vacio(t):
    'init   : '

    empty = clase.Nodo(graph.setHoja('empty'), None)
    t[0] = clase.Nodo(graph.setNodo('init', [empty.id]), None)
    graph.saveGraph()

#---------------------------------------------------------------------
def p_init(t):
    'init   : instrucciones'

    t[0] = clase.Nodo(graph.setNodo('init', [t[1].id]), None)
    graph.saveGraph()

    if len(t[1].stack) > 0:
        ejec.ejecutarStack(t[1].stack)

#---------------------------------------------------------------------
def p_instrucciones_l1(t):
    '''instrucciones    : instruccion'''

    new_stackable = []
    if len(t[1].stack) > 0:
        new_stackable.extend(t[1].stack)

    t[0] = clase.Nodo(graph.setNodo('instrucciones', [t[1].id]), new_stackable)

#---------------------------------------------------------------------
def p_instrucciones_l2(t):
    'instrucciones    : instruccion instrucciones'

    new_stackable = []
    if len(t[1].stack) > 0:
        new_stackable.extend(t[1].stack)
    if len(t[2].stack) > 0:
        new_stackable.extend(t[2].stack)

    t[0] = clase.Nodo(graph.setNodo('instrucciones', [t[1].id, t[2].id]), new_stackable)

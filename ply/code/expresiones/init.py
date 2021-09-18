import ply.clases.clases as clase 
import ply.report.graficar as graph
import ply.make.ejecutar as ejecutar

start = 'init'

def p_init_vacio(t):
    'init   : PUNTO_COMA'

    empty = clase.Nodo(graph.setHoja('empty'))
    t[0] = clase.Nodo(graph.setNodo('init', [empty.id]))
    graph.saveGraph()

#---------------------------------------------------------------------
def p_init(t):
    'init   : instrucciones_f PUNTO_COMA'
    
    t[0] = clase.Nodo(graph.setNodo('init', [t[1].id]))
    graph.saveGraph()

    ejecutar.init(t[1].stack)

#---------------------------------------------------------------------
def p_instrucciones_f_l1(t):
    '''instrucciones_f    : instruccion_f'''

    new_stackable = []
    if len(t[1].stack) > 0:
        new_stackable.extend(t[1].stack)

    t[0] = clase.Nodo(graph.setNodo('instrucciones_f', [t[1].id]), new_stackable)
#---------------------------------------------------------------------
def p_instrucciones_f_l2(t):
    'instrucciones_f    : instruccion_f instrucciones_f'

    new_stackable = []
    if len(t[1].stack) > 0:
        new_stackable.extend(t[1].stack)
    if len(t[2].stack) > 0:
        new_stackable.extend(t[2].stack)

    t[0] = clase.Nodo(graph.setNodo('instrucciones_f', [t[1].id, t[2].id]), new_stackable)

#---------------------------------------------------------------------
def p_instrucciones_f_l3(t):
    '''instruccion_f    : instrucciones'''

    new_stackable = []
    if len(t[1].stack) > 0:
        new_stackable.extend(t[1].stack)

    t[0] = clase.Nodo(graph.setNodo('instruccion_f', [t[1].id]), new_stackable)


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

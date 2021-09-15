import ply.clases.clases as clase 
import ply.report.graficar as graph
import ply.funcion.asignacion.asignacion as asig

#---------------------------------------------------------------------
def p_instruccion_asignacion(t):
    'instruccion    : asignacion'

    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), None)

#---------------------------------------------------------------------
def p_asignacion(t):
    
    '''asignacion  : ID SIMBOLO_IGUAL expresion PUNTO_COMA'''

    asig.setAsignacion([t[1], t[3]], [t.lineno(1), t.lexpos(1)])

    dato_1_1 = clase.Nodo(graph.setHoja(t[1]), None)
    dato_1_2 = clase.Nodo(graph.setNodo('ID', [dato_1_1.id]), None)
    dato_2 = clase.Nodo(graph.setHoja('='), None)
    dato_4 = clase.Nodo(graph.setHoja(';'), None)
    t[0] = clase.Nodo(graph.setNodo('asignacion', [dato_1_2.id, dato_2.id, t[3].id, dato_4.id]), "")

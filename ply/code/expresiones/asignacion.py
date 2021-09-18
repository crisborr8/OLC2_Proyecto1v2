import ply.clases.clases as clase 
import ply.report.graficar as graph

#---------------------------------------------------------------------
def p_instruccion_asignacion(t):
    '''instruccion  : asignacion'''
    
    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), [t[1].stack])

#---------------------------------------------------------------------
def p_asignacion(t):
    '''asignacion   : dato_id SIMBOLO_IGUAL expresion PUNTO_COMA'''
    
    children = []
    children.append(t[1].value)                             #0 - ID
    children.append(True)                                   #1 - Existe
    children.append(0)                                      #2 - Valor
    children.append("referencia")                           #3 - Referencia o por valor
    children.append(clase.texto[t[3].start: t[3].end])      #4 - Texto lexema
    children.append(t.lexpos(1))                            #5 - Fila lexema

    new_stack = clase.Stack('var', children)
    new_stack.setFila(t.lineno(1))

    dato_2 = clase.Nodo(graph.setHoja("="))
    dato_4 = clase.Nodo(graph.setHoja(";"))
    t[0] = clase.Nodo(graph.setNodo('asignacion', [t[1].id, dato_2.id, t[3].id, dato_4.id]), new_stack)
    
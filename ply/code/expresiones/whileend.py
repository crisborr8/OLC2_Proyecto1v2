import ply.clases.clases as clase 
import ply.report.graficar as graph

#---------------------------------------------------------------------
def p_instruccion_while(t):
    '''instruccion  : while'''
    
    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), [t[1].stack])
    
#---------------------------------------------------------------------
def p_while(t):
    '''while  : WHILE condicion instrucciones END PUNTO_COMA'''
    
    children = []
    children.append(clase.texto[t[2].start: t[2].end])      #0 - Texto condicion
    children.append(t.lexpos(2))                            #1 - Fila condicion
    children.append(t[3].stack)                             #2 - Texto instrucion

    new_stack = clase.Stack('while', children)
    new_stack.setFila(t.lineno(1))

    dato_1 = clase.Nodo(graph.setHoja("while"))
    dato_4 = clase.Nodo(graph.setHoja("end"))
    dato_5 = clase.Nodo(graph.setHoja(";"))
    t[0] = clase.Nodo(graph.setNodo('while', [dato_1.id, t[2].id, t[3].id, dato_4.id, dato_5.id]), new_stack)
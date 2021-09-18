import ply.clases.clases as clase 
import ply.report.graficar as graph

#---------------------------------------------------------------------
def p_instruccion_imprimir(t):
    '''instruccion  : imprimir'''
    
    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), [t[1].stack])

#---------------------------------------------------------------------
def p_imprimir_ln(t):
    '''imprimir   : PRINTLN IZQ_PARENTESIS contenido DER_PARENTESIS PUNTO_COMA'''
    
    children = []
    children.append("\n")                                   #0 - type print
    children.append(clase.texto[t[3].start: t[3].end])      #1 - Texto lexema
    children.append(t.lexpos(3))                            #5 - Fila lexema

    new_stack = clase.Stack('print', children)
    new_stack.setFila(t.lineno(1))
    
    dato_1 = clase.Nodo(graph.setHoja("println"))
    dato_2 = clase.Nodo(graph.setHoja("("))
    dato_4 = clase.Nodo(graph.setHoja(")"))
    dato_5 = clase.Nodo(graph.setHoja(";"))
    t[0] = clase.Nodo(graph.setNodo('imprimir', [dato_1.id, dato_2.id, t[3].id, dato_4.id, dato_5.id]), new_stack)

#---------------------------------------------------------------------
def p_imprimir_(t):
    '''imprimir   : PRINT IZQ_PARENTESIS contenido DER_PARENTESIS PUNTO_COMA'''
    
    children = []
    children.append("")                                     #0 - type print
    children.append(clase.texto[t[3].start: t[3].end])      #1 - Texto lexema
    children.append(t.lexpos(3))                            #5 - Fila lexema

    new_stack = clase.Stack('print', children)
    new_stack.setFila(t.lineno(1))

    dato_1 = clase.Nodo(graph.setHoja("print"))
    dato_2 = clase.Nodo(graph.setHoja("("))
    dato_4 = clase.Nodo(graph.setHoja(")"))
    dato_5 = clase.Nodo(graph.setHoja(";"))
    t[0] = clase.Nodo(graph.setNodo('imprimir', [dato_1.id, dato_2.id, t[3].id, dato_4.id, dato_5.id]), new_stack)

#---------------------------------------------------------------------
def p_imprimir_contenido(t):
    '''contenido   : expresion'''
    
    t[0] = clase.Nodo(graph.setNodo('contenido', [t[1].id]))
    t[0].setPos(t[1].getPos())
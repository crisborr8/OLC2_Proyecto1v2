import ply.clases.clases as clase 
import ply.report.graficar as graph

#---------------------------------------------------------------------
def p_instruccion_if(t):
    '''instruccion  : if'''
    
    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), [t[1].stack])

#---------------------------------------------------------------------
def p_if(t):
    '''if  : IF condicion instrucciones if_then END PUNTO_COMA'''
    
    children = []
    children.append(clase.texto[t[2].start: t[2].end])      #0 - Texto condicion
    children.append(t.lexpos(2))                            #1 - Fila condicion
    children.append(t[3].stack)                             #2 - Texto instrucion
    children.append(t[4].stack)                             #3 - Texto then

    new_stack = clase.Stack('if', children)
    new_stack.setFila(t.lineno(1))

    dato_1 = clase.Nodo(graph.setHoja("if"))
    dato_5 = clase.Nodo(graph.setHoja("end"))
    dato_6 = clase.Nodo(graph.setHoja(";"))
    t[0] = clase.Nodo(graph.setNodo('if', [dato_1.id, t[2].id, t[3].id, t[4].id, dato_5.id, dato_6.id]), new_stack)


#---------------------------------------------------------------------
def p_ifthen(t):
    '''if_then  : if_elseif
                | if_else'''
    
    t[0] = clase.Nodo(graph.setNodo('if_then', [t[1].id]), t[1].stack)

#---------------------------------------------------------------------
def p_ifelseif(t):
    '''if_elseif  : ELSE IF condicion instrucciones if_then'''

    children = []
    children.append(clase.texto[t[3].start: t[3].end])      #0 - Texto condicion
    children.append(t.lexpos(3))                            #1 - Fila condicion
    children.append(t[4].stack)                             #2 - Texto instrucion
    children.append(t[5].stack)                             #3 - Texto then

    new_stack = clase.Stack('if', children)
    new_stack.setFila(t.lineno(3))

    dato_1 = clase.Nodo(graph.setHoja("else"))
    dato_2 = clase.Nodo(graph.setHoja("if"))
    t[0] = clase.Nodo(graph.setNodo('if_then', [dato_1.id, dato_2.id, t[3].id, t[4].id, t[5].id]), [new_stack])

#---------------------------------------------------------------------
def p_ifelse(t):
    '''if_else  : ELSE instrucciones'''

    dato_1 = clase.Nodo(graph.setHoja("else"))
    t[0] = clase.Nodo(graph.setNodo('if_then', [dato_1.id, t[2].id]), t[2].stack)

#---------------------------------------------------------------------
def p_ifelse_empty(t):
    '''if_else  : '''
    
    new_stackable = []
    new_stackable.append(clase.Stack('empty'))

    dato_1 = clase.Nodo(graph.setHoja("empty"))
    t[0] = clase.Nodo(graph.setNodo('if_then', [dato_1.id]), new_stackable)
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
def p_condicion_arit(t):
    '''condicion    : expresion MENOR expresion
                    | expresion MAYOR expresion
                    | expresion IGUAL expresion
                    | expresion NOIGUAL expresion
                    | expresion MENOR_IGUAL expresion
                    | expresion MAYOR_IGUAL expresion'''

    op = t[2]
    if t[2] == '<': op = "&#60;"
    elif t[2] == '>': op = "&#62;"
    elif t[2] == '>=': op = "&#62;="
    elif t[2] == '<=': op = "&#60;="
    dato_2 = clase.Nodo(graph.setHoja(op))
    t[0] = clase.Nodo(graph.setNodo('condicion', [t[1].id, dato_2.id, t[3].id]))
    t[0].setPos([t[1].start, t[3].end])

#---------------------------------------------------------------------
def p_condicion_logic(t):
    '''condicion    : condicion OR condicion
                    | condicion AND condicion'''

    dato_2 = clase.Nodo(graph.setHoja(t[2]))
    t[0] = clase.Nodo(graph.setNodo('condicion', [t[1].id, dato_2.id, t[3].id]))
    t[0].setPos([t[1].start, t[3].end])
    
#---------------------------------------------------------------------
def p_condicion_not(t):
    '''condicion    : NOT condicion'''
                    
    dato_1 = clase.Nodo(graph.setHoja(t[1]))
    t[0] = clase.Nodo(graph.setNodo('condicion', [dato_1.id, t[2].id]))
    t[0].setPos([t[1].start, t[2].end])
    
#---------------------------------------------------------------------
def p_condicion_par(t):
    '''condicion    : IZQ_PARENTESIS condicion DER_PARENTESIS'''
                    
    dato_1 = clase.Nodo(graph.setHoja("("))
    dato_3 = clase.Nodo(graph.setHoja(")"))
    t[0] = clase.Nodo(graph.setNodo('condicion', [dato_1.id, t[2].id, dato_3.id]))
    t[0].setPos(t[2].getPos())
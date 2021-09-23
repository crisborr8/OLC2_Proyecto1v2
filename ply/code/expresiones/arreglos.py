import ply.clases.clases as clase 
import ply.report.graficar as graph

#---------------------------------------------------------------------
def p_instruccion_pushpop(t):
    '''instruccion  : pushpop'''
    
    t[0] = clase.Nodo(graph.setNodo('pushpop', [t[1].id]), [t[1].stack])


#---------------------------------------------------------------------
def p_pushpop_push(t):
    '''pushpop   : PUSH IZQ_PARENTESIS dato_id COMA expresion DER_PARENTESIS PUNTO_COMA'''
    
    children = []
    children.append(t[3].value)                             #0 - ID
    children.append(clase.texto[t[5].start: t[5].end])      #1 - Texto lexema
    children.append(t.lexpos(1))                            #2 - Fila lexema

    new_stack = clase.Stack('push', children)
    new_stack.setFila(t.lineno(1))

    dato_1 = clase.Nodo(graph.setHoja("push"))
    dato_2 = clase.Nodo(graph.setHoja("("))
    dato_4 = clase.Nodo(graph.setHoja(","))
    dato_6 = clase.Nodo(graph.setHoja(")"))
    dato_7 = clase.Nodo(graph.setHoja(";"))
    t[0] = clase.Nodo(graph.setNodo('PUSH', [dato_1.id, dato_2.id, t[3].id, dato_4.id, t[5].id, dato_6.id, dato_7.id]), new_stack)

#---------------------------------------------------------------------
def p_pushpop_pop(t):
    '''pushpop   : POP IZQ_PARENTESIS dato_id DER_PARENTESIS PUNTO_COMA'''
    
    children = []
    children.append(t[3].value)                             #0 - ID
    children.append(t.lexpos(1))                            #1 - Fila lexema

    new_stack = clase.Stack('pop', children)
    new_stack.setFila(t.lineno(1))

    dato_1 = clase.Nodo(graph.setHoja("pop"))
    dato_2 = clase.Nodo(graph.setHoja("("))
    dato_4 = clase.Nodo(graph.setHoja(")"))
    dato_5 = clase.Nodo(graph.setHoja(";"))
    t[0] = clase.Nodo(graph.setNodo('POP', [dato_1.id, dato_2.id, t[3].id, dato_4.id, dato_5.id]), new_stack)



#---------------------------------------------------------------------
def p_expresion_dato_id_arr(t):
    '''dato_id_array    : dato_id array_exp'''
                    
    t[0] = clase.Nodo(graph.setNodo('ID Array', [t[1].id, t[2].id]))
    t[0].setPos([t[1].start, t[2].end])


#---------------------------------------------------------------------
def p_asignacion_array(t):
    '''asignacion   : dato_id array_exp SIMBOLO_IGUAL expresion PUNTO_COMA'''
    
    children = []
    children.append(t[1].value)                             #0 - ID
    children.append(False)                                  #1 - Existe
    children.append(0)                                      #2 - Valor
    children.append("referencia")                           #3 - Referencia o por valor
    children.append(clase.texto[t[4].start: t[4].end])      #4 - Texto lexema
    children.append(t.lexpos(1))                            #5 - Fila lexema
    children.append(clase.texto[t[2].start: t[2].end])      #6 - Pos_array

    new_stack = clase.Stack('array', children)
    new_stack.setFila(t.lineno(1))

    dato_3 = clase.Nodo(graph.setHoja("="))
    dato_5 = clase.Nodo(graph.setHoja(";"))
    t[0] = clase.Nodo(graph.setNodo('asignacion', [t[1].id, t[2].id, dato_3.id, t[4].id, dato_5.id]), new_stack)

    
#---------------------------------------------------------------------
def p_expresion_arrayExp(t):
    '''array_exp    : IZQ_LLAVE expresion DER_LLAVE'''
                    
    dato_1 = clase.Nodo(graph.setHoja("["))
    dato_3 = clase.Nodo(graph.setHoja("]"))
    t[0] = clase.Nodo(graph.setNodo('array_expresion', [dato_1.id, t[2].id, dato_3.id]))
    
    start, end = t.lexspan(1)
    end = t.lexpos(3) + len(str(t[3]))
    t[0].setPos([start, end])


#---------------------------------------------------------------------
def p_expresion_arrayExp_BE(t):
    '''array_exp    : IZQ_LLAVE rango_arr DER_LLAVE'''
                    
    dato_1 = clase.Nodo(graph.setHoja("["))
    dato_3 = clase.Nodo(graph.setHoja("]"))
    t[0] = clase.Nodo(graph.setNodo('array_expresion', [dato_1.id, t[2].id, dato_3.id]))
    
    start, end = t.lexspan(1)
    end = t.lexpos(3) + len(str(t[3]))
    t[0].setPos([start, end])

#---------------------------------------------------------------------
def p_rango_array(t):
    '''rango_arr    : begin PUNTO_PUNTO end'''
                    
    dato_2 = clase.Nodo(graph.setHoja(":"))
    t[0] = clase.Nodo(graph.setNodo('rango array', [t[1].id, dato_2.id, t[3].id]))
    t[0].setPos([t[1].start, t[3].end])

#---------------------------------------------------------------------
def p_rango_begin(t):
    '''begin    : BEGIN'''
                    
    dato_1 = clase.Nodo(graph.setHoja('BEGIN'))
    t[0] = clase.Nodo(graph.setNodo('begin', [dato_1.id]), t.lineno(1))

    start, end = t.lexspan(1)
    end += len(str(t[1]))
    t[0].setPos([start, end])

#---------------------------------------------------------------------
def p_rango_begin_expresion(t):
    '''begin    : expresion'''
                    
    t[0] = clase.Nodo(graph.setNodo('begin', [t[1].id]), t.lineno(1))

    t[0].setPos(t[1].getPos())


#---------------------------------------------------------------------
def p_rango_beginEmpty(t):
    '''begin    : '''
    
    new_stackable = []
    new_stackable.append(clase.Stack('empty'))

    dato_1 = clase.Nodo(graph.setHoja("empty"))
    t[0] = clase.Nodo(graph.setNodo('begin', [dato_1.id]), new_stackable)

#---------------------------------------------------------------------
def p_rango_end(t):
    '''end  : END'''
                    
    dato_1 = clase.Nodo(graph.setHoja('END'))
    t[0] = clase.Nodo(graph.setNodo('end', [dato_1.id]), t.lineno(1))

    start, end = t.lexspan(1)
    end += len(str(t[1]))
    t[0].setPos([start, end])

#---------------------------------------------------------------------
def p_rango_end_expresion(t):
    '''end  : expresion'''
                    
    t[0] = clase.Nodo(graph.setNodo('end', [t[1].id]), t.lineno(1))

    t[0].setPos(t[1].getPos())

#---------------------------------------------------------------------
def p_rango_endEmpty(t):
    '''end  : '''
    
    new_stackable = []
    new_stackable.append(clase.Stack('empty'))

    dato_1 = clase.Nodo(graph.setHoja("empty"))
    t[0] = clase.Nodo(graph.setNodo('end', [dato_1.id]), new_stackable)

#---------------------------------------------------------------------
def p_expresion_arrayExp2(t):
    '''array_exp    : array_exp array_exp'''
                    
    t[0] = clase.Nodo(graph.setNodo('array_expresion', [t[1].id, t[2].id]))
    t[0].setPos([t[1].start, t[2].end])

#---------------------------------------------------------------------
def p_expresion_array(t):
    '''array    : IZQ_LLAVE contenido DER_LLAVE'''
                    
    dato_1 = clase.Nodo(graph.setHoja("["))
    dato_3 = clase.Nodo(graph.setHoja("]"))
    t[0] = clase.Nodo(graph.setNodo('array', [dato_1.id, t[2].id, dato_3.id]))
    
    start, end = t.lexspan(1)
    end = t.lexpos(3) + len(str(t[3]))
    t[0].setPos([start, end])
    
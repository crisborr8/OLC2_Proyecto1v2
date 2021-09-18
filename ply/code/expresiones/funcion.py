import ply.clases.clases as clase 
import ply.report.graficar as graph

#---------------------------------------------------------------------
def p_instruccion_funcion(t):
    '''instruccion_f  : funcion'''
    
    t[0] = clase.Nodo(graph.setNodo('instruccion_f', [t[1].id]), [t[1].stack])

#---------------------------------------------------------------------
def p_funcion_param(t):
    '''funcion  : FUNCION dato_id IZQ_PARENTESIS parametros DER_PARENTESIS instrucciones END PUNTO_COMA'''
    
    children_var = []
    children_var.append(t[2].value)      #0 - ID
    children_var.append(True)            #1 - Hay parametros
    children_var.append(clase.texto[t[4].start: t[4].end])      #2 - Texto parametros
    children_var.append(t.lexpos(4))     #3 - Fila lexema

    new_stack_var = clase.Stack('func', children_var)
    new_stack_var.setFila(t.lineno(2))

    children = []
    children.append(new_stack_var)      #0 - Var
    children.append(t[6].stack)         #1 - Instruccion
    children.append(t.lexpos(1))        #2 - Columna lexema

    new_stack = clase.Stack('funcion', children)
    new_stack.setFila(t.lineno(1))

    dato_1 = clase.Nodo(graph.setHoja("function"))
    dato_3 = clase.Nodo(graph.setHoja("("))
    dato_5 = clase.Nodo(graph.setHoja(")"))
    dato_7 = clase.Nodo(graph.setHoja("END"))
    dato_8 = clase.Nodo(graph.setHoja(";"))
    t[0] = clase.Nodo(graph.setNodo('funcion', [dato_1.id, t[2].id, dato_3.id, t[4].id, dato_5.id, t[6].id, dato_7.id, dato_8.id]), new_stack)

#---------------------------------------------------------------------
def p_funcion(t):
    '''funcion  : FUNCION dato_id IZQ_PARENTESIS DER_PARENTESIS instrucciones END PUNTO_COMA'''

    children_var = []
    children_var.append(t[2].value)      #0 - ID
    children_var.append(False)           #1 - Hay parametros

    new_stack_var = clase.Stack('func', children_var)
    new_stack_var.setFila(t.lineno(2))

    children = []
    children.append(new_stack_var)      #0 - Var
    children.append(t[5].stack)         #1 - Instruccion
    children.append(t.lexpos(1))        #2 - Columna lexema

    new_stack = clase.Stack('funcion', children)
    new_stack.setFila(t.lineno(1))

    dato_1 = clase.Nodo(graph.setHoja("function"))
    dato_3 = clase.Nodo(graph.setHoja("("))
    dato_4 = clase.Nodo(graph.setHoja(")"))
    dato_6 = clase.Nodo(graph.setHoja("END"))
    dato_7 = clase.Nodo(graph.setHoja(";"))
    t[0] = clase.Nodo(graph.setNodo('funcion', [dato_1.id, t[2].id, dato_3.id, dato_4.id, t[5].id, dato_6.id, dato_7.id]), new_stack)

#---------------------------------------------------------------------
def p_instruccion_callfuncion(t):
    '''instruccion  : callfuncion'''
    
    new_stack = clase.Stack('exp', [clase.texto[t[1].start: t[1].end]])
    new_stack.setFila(t.lineno(1))

    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), [new_stack])

#---------------------------------------------------------------------
def p_funcion_callfuncion(t):
    '''callfuncion    :  funcion_exp PUNTO_COMA
                      |  funcion_exp_param PUNTO_COMA'''
                    
    dato_2 = clase.Nodo(graph.setHoja(";"))
    t[0] = clase.Nodo(graph.setNodo('callfuncion', [t[1].id, dato_2.id]))
    t[0].setPos(t[1].getPos())

#---------------------------------------------------------------------
def p_funcion_exp(t):
    '''funcion_exp    :  dato_id IZQ_PARENTESIS DER_PARENTESIS'''
                    
    dato_2 = clase.Nodo(graph.setHoja("("))
    dato_3 = clase.Nodo(graph.setHoja(")"))
    t[0] = clase.Nodo(graph.setNodo('funcion_exp', [t[1].id, dato_2.id, dato_3.id]))

    start, end = t.lexspan(1)
    end = t.lexpos(3) + len(str(t[3]))
    t[0].setPos([start, end])

#---------------------------------------------------------------------
def p_funcion_exp_param(t):
    '''funcion_exp_param    :  dato_id IZQ_PARENTESIS contenido DER_PARENTESIS'''
                    
    dato_2 = clase.Nodo(graph.setHoja("("))
    dato_4 = clase.Nodo(graph.setHoja(")"))
    t[0] = clase.Nodo(graph.setNodo('funcion_exp_param', [t[1].id, dato_2.id, t[3].id, dato_4.id]))

    start, end = t.lexspan(1)
    end = t.lexpos(4) + len(str(t[4]))
    t[0].setPos([start, end])


#---------------------------------------------------------------------
def p_parametros(t):
    '''parametros   : dato_id'''

    t[0] = clase.Nodo(graph.setNodo('parametros', [t[1].id]))
    t[0].setPos(t[1].getPos())

#---------------------------------------------------------------------
def p_parametros_coma(t):
    '''parametros   : dato_id COMA parametros '''
    
    dato_2 = clase.Nodo(graph.setHoja(','))
    t[0] = clase.Nodo(graph.setNodo('parametros', [t[1].id, dato_2.id, t[3].id]))
    t[0].setPos([t[1].start, t[3].end])
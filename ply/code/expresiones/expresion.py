import ply.clases.clases as clase 
import ply.report.graficar as graph

#---------------------------------------------------------------------
def p_instruccion_return(t):
    '''instruccion  : RETURN expresion PUNTO_COMA'''
    
    dato_1 = clase.Nodo(graph.setHoja("return"))
    dato_3 = clase.Nodo(graph.setHoja(";"))

    new_stack = clase.Stack('ret', [clase.texto[t[2].start: t[2].end]])
    new_stack.setFila(t.lineno(2))

    t[0] = clase.Nodo(graph.setNodo('instruccion', [dato_1.id, t[2].id, dato_3.id]), [new_stack])

#---------------------------------------------------------------------
def p_instruccion_expresion(t):
    '''instruccion  : expresion'''
    
    new_stack = clase.Stack('exp', [clase.texto[t[1].start: t[1].end]])
    new_stack.setFila(t.lineno(1))

    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), [new_stack])

#---------------------------------------------------------------------
def p_expresion_par(t):
    '''expresion    : IZQ_PARENTESIS expresion DER_PARENTESIS'''
                    
    dato_1 = clase.Nodo(graph.setHoja("("))
    dato_3 = clase.Nodo(graph.setHoja(")"))
    t[0] = clase.Nodo(graph.setNodo('expresion', [dato_1.id, t[2].id, dato_3.id]))
    
    start, end = t.lexspan(1)
    end = t.lexpos(3) + len(str(t[3]))
    t[0].setPos([start, end])

#---------------------------------------------------------------------
def p_expresion_binario(t):
    '''expresion    : expresion SIMBOLO_SUMA expresion
                    | expresion SIMBOLO_RESTA expresion
                    | expresion SIMBOLO_DIVICION expresion
                    | expresion SIMBOLO_MULTIPLICACION expresion
                    | expresion SIMBOLO_POTENCIA expresion
                    | expresion SIMBOLO_MOD expresion'''
    
    dato_2 = clase.Nodo(graph.setHoja(t[2]))
    t[0] = clase.Nodo(graph.setNodo('expresion', [t[1].id, dato_2.id, t[3].id]))
    t[0].setPos([t[1].start, t[3].end])

#---------------------------------------------------------------------
def p_expresion_nativa_binaria(t):
    '''expresion    : LOG IZQ_PARENTESIS expresion COMA expresion DER_PARENTESIS
                    | TRUNC IZQ_PARENTESIS tipo COMA expresion DER_PARENTESIS
                    | PARSE IZQ_PARENTESIS tipo COMA expresion DER_PARENTESIS'''
    
    dato_1 = clase.Nodo(graph.setHoja(t[1]))
    dato_2 = clase.Nodo(graph.setHoja('('))
    dato_4 = clase.Nodo(graph.setHoja(','))
    dato_6 = clase.Nodo(graph.setHoja(')'))
    t[0] = clase.Nodo(graph.setNodo('expresion', [dato_1.id, dato_2.id, t[3].id, dato_4.id, t[5].id, dato_6.id]))

    start, end = t.lexspan(1)
    end = t.lexpos(6) + len(str(t[6]))
    t[0].setPos([start, end])

def p_expresion_tipo(t):
    '''tipo     : INT64
                | FLOAT64
                | NOTHING
                | STRING
                | CHAR
                | BOOL'''

    dato_1 = clase.Nodo(graph.setHoja(str(t[1])))
    t[0] = clase.Nodo(graph.setNodo('TIPO', [dato_1.id]), t.lineno(1))

    start, end = t.lexspan(1)
    end += len(str(t[1]))
    t[0].setPos([start, end])

#---------------------------------------------------------------------
def p_expresion_nativa(t):
    '''expresion    : LOG10 IZQ_PARENTESIS expresion DER_PARENTESIS
                    | SIN IZQ_PARENTESIS expresion DER_PARENTESIS
                    | COS IZQ_PARENTESIS expresion DER_PARENTESIS
                    | TAN IZQ_PARENTESIS expresion DER_PARENTESIS
                    | SQRT IZQ_PARENTESIS expresion DER_PARENTESIS
                    | UPPER IZQ_PARENTESIS expresion DER_PARENTESIS
                    | LOWER IZQ_PARENTESIS expresion DER_PARENTESIS
                    | STRING_FUNC IZQ_PARENTESIS expresion DER_PARENTESIS
                    | TYPEOF IZQ_PARENTESIS expresion DER_PARENTESIS
                    | FLOAT IZQ_PARENTESIS expresion DER_PARENTESIS'''
    
    dato_1 = clase.Nodo(graph.setHoja(t[1]))
    dato_2 = clase.Nodo(graph.setHoja('('))
    dato_4 = clase.Nodo(graph.setHoja(')'))
    t[0] = clase.Nodo(graph.setNodo('expresion', [dato_1.id, dato_2.id, t[3].id, dato_4.id]))

    start, end = t.lexspan(1)
    end = t.lexpos(4) + len(str(t[4]))
    t[0].setPos([start, end])

#---------------------------------------------------------------------
def p_expresion_negativo(t):
    'expresion  : SIMBOLO_RESTA expresion %prec NEGATIVO'

    dato_1 = clase.Nodo(graph.setHoja('-'))
    t[0] = clase.Nodo(graph.setNodo('expresion', [dato_1.id, t[2].id]))
    start, end = t.lexspan(1)
    t[0].setPos([start, t[2].end])

#---------------------------------------------------------------------
def p_expresion_numerico(t):
    '''expresion    : dato_numerico
                    | dato_booleano
                    | funcion_exp
                    | funcion_exp_param
                    | dato_id'''

    t[0] = clase.Nodo(graph.setNodo('expresion', [t[1].id]))
    t[0].setPos(t[1].getPos())

#---------------------------------------------------------------------
def p_expresion_dato_numerico(t):
    '''dato_numerico    : DATO_TIPO_FLOAT64
                        | DATO_TIPO_INT64
                        | DATO_TIPO_STRING
                        | DATO_TIPO_CHAR'''

    dato_1 = clase.Nodo(graph.setHoja(str(t[1])))
    t[0] = clase.Nodo(graph.setNodo('DATO', [dato_1.id]), t.lineno(1))

    start, end = t.lexspan(1)
    end += len(str(t[1]))
    t[0].setPos([start, end])


#---------------------------------------------------------------------
def p_expresion_dato_booleano(t):
    '''dato_booleano    : TRUE
                        | FALSE'''

    dato_1 = clase.Nodo(graph.setHoja(str(t[1])))
    t[0] = clase.Nodo(graph.setNodo('DATO', [dato_1.id]), t.lineno(1))

    start, end = t.lexspan(1)
    end += len(str(t[1]))
    t[0].setPos([start, end])


#---------------------------------------------------------------------
def p_expresion_dato_id(t):
    '''dato_id    : ID'''

    dato_1 = clase.Nodo(graph.setHoja(str(t[1])))
    t[0] = clase.Nodo(graph.setNodo('ID', [dato_1.id]), t.lineno(1))
    t[0].setValue(t[1])

    start, end = t.lexspan(1)
    end += len(str(t[1]))
    t[0].setPos([start, end])
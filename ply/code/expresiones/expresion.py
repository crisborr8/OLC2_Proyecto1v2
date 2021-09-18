import ply.clases.clases as clase 
import ply.report.graficar as graph

#---------------------------------------------------------------------
def p_instruccion_expresion(t):
    '''instruccion  : expresion'''
    
    print("esto leen en exp->>" + clase.texto[t[1].start: t[1].end])
    new_stack = clase.Stack('exp', [clase.texto[t[1].start: t[1].end]])
    new_stack.setFila(t.lineno(1))

    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), [new_stack])

#---------------------------------------------------------------------
def p_expresion_par(t):
    '''expresion    : IZQ_PARENTESIS expresion DER_PARENTESIS'''
                    
    dato_1 = clase.Nodo(graph.setHoja("("))
    dato_3 = clase.Nodo(graph.setHoja(")"))
    t[0] = clase.Nodo(graph.setNodo('expresion', [dato_1.id, t[2].id, dato_3.id]))
    t[0].setPos(t[2].getPos())

#---------------------------------------------------------------------
def p_expresion_binario(t):
    '''expresion    : expresion SIMBOLO_SUMA expresion
                    | expresion SIMBOLO_RESTA expresion
                    | expresion SIMBOLO_DIVICION expresion
                    | expresion SIMBOLO_MULTIPLICACION expresion'''
    
    dato_2 = clase.Nodo(graph.setHoja(t[2]))
    t[0] = clase.Nodo(graph.setNodo('expresion', [t[1].id, dato_2.id, t[3].id]))
    t[0].setPos([t[1].start, t[3].end])

#---------------------------------------------------------------------
def p_expresion_negativo(t):
    'expresion  : SIMBOLO_RESTA expresion %prec NEGATIVO'

    dato_1 = clase.Nodo(graph.setHoja('-'))
    t[0] = clase.Nodo(graph.setNodo('expresion', [dato_1.id, t[2].id]))
    t[0].setPos([t[1].start, t[2].end])

#---------------------------------------------------------------------
def p_expresion_numerico(t):
    '''expresion    : dato_numerico
                    | dato_id
                    | funcion_exp'''

    t[0] = clase.Nodo(graph.setNodo('expresion', [t[1].id]))
    t[0].setPos(t[1].getPos())

#---------------------------------------------------------------------
def p_expresion_dato_numerico(t):
    '''dato_numerico    : DATO_TIPO_FLOAT64
                        | DATO_TIPO_INT64
                        | DATO_TIPO_STRING'''

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
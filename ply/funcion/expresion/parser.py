import ply.clases.clases as clase 
import ply.report.reportes as rep
import ply.report.graficar as graph
import ply.funcion.operadores.aritmeticas as arit

#---------------------------------------------------------------------
def p_instruccion_expresion(t):
    '''instruccion  : expresion'''
    
    new_stackable = []
    if t[1].error == True:
        rep.setError(t[1].value, t[1].fila, t[1].colu)
    else:
        new_stackable.append(clase.Stack('print', [str(t[1].value) + "\n"]))

    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), new_stackable)

#---------------------------------------------------------------------
def p_expresion_binario(t):
    '''expresion    : expresion SIMBOLO_SUMA expresion
                    | expresion SIMBOLO_RESTA expresion
                    | expresion SIMBOLO_DIVICION expresion
                    | expresion SIMBOLO_MULTIPLICACION expresion'''
    
    res = []
    if t[1].error == True:
        res = t[1].getValue()
    elif t[3].error == True:
        res = t[3].getValue()
    else:
        res = arit.getResult([t[1].value, t.lineno(1), t.lexpos(1)], [t[3].value, t.lineno(3), t.lexpos(3)], t[2])

    dato_2 = clase.Nodo(graph.setHoja(t[2]))
    t[0] = clase.Nodo(graph.setNodo('expresion', [t[1].id, dato_2.id, t[3].id]))
    t[0].setValue(res)

#---------------------------------------------------------------------
def p_expresion_par(t):
    'expresion  : IZQ_PARENTESIS expresion DER_PARENTESIS'

    dato_1 = clase.Nodo(graph.setHoja('('))
    dato_3 = clase.Nodo(graph.setHoja(')'))
    t[0] = clase.Nodo(graph.setNodo('expresion', [dato_1.id, t[2].id, dato_3.id]))
    t[0].setValue(t[2].getValue())

#---------------------------------------------------------------------
def p_expresion_negativo(t):
    'expresion  : SIMBOLO_RESTA expresion %prec NEGATIVO'

    res = []
    if t[2].error == True:
        res = t[2].getValue()
    else:
        res = arit.setNegativo([t[2].value, t.lineno(2), t.lexpos(2)])

    dato_1 = clase.Nodo(graph.setHoja('-'))
    t[0] = clase.Nodo(graph.setNodo('expresion', [dato_1.id, t[2].id]))
    t[0].setValue(res)

#---------------------------------------------------------------------
def p_expresion_datos(t):
    '''expresion    : DATO_TIPO_FLOAT64
                    | DATO_TIPO_INT64
                    | DATO_TIPO_STRING'''

    dato_1 = clase.Nodo(graph.setHoja(t[1]))
    dato_2 = clase.Nodo(graph.setNodo('DATO', [dato_1.id]))
    t[0] = clase.Nodo(graph.setNodo('expresion', [dato_2.id]))
    t[0].setValue([False, t[1]])

#---------------------------------------------------------------------
def p_expresion_datos_id(t):
    '''expresion    : dato'''

    #codigo de busqueda de id
    new_var = clase.current_vars
    res = clase.Vars.getValue([t[1].value, t.lineno(1), t.lexpos(1)], new_var)
    
    dato_1 = clase.Nodo(graph.setNodo('DATO', [t[1].id]))
    t[0] = clase.Nodo(graph.setNodo('expresion', [dato_1.id]))
    t[0].setValue(res)

#---------------------------------------------------------------------
def p_expresion_id(t):
    '''dato  : ID'''

    dato_1 = clase.Nodo(graph.setHoja(t[1]))
    t[0] = clase.Nodo(graph.setNodo('ID', [dato_1.id]))
    t[0].setValue([False, t[1]])
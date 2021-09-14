import ply.clases.nodo as nodo
import ply.clases.variable as var
import ply.report.reportes as rep
import ply.report.graficar as graph
import ply.funcion.aritmeticas as arit

precedence = (
    ('left','SIMBOLO_SUMA','SIMBOLO_RESTA'),
    ('left','SIMBOLO_MULTIPLICACION','SIMBOLO_DIVICION'),
    ('right','NEGATIVO'),
    )
names = { }

#---------------------------------------------------------------------
def p_init(t):
    'init   : instrucciones'

    t[0] = nodo.Nodo(graph.setNodo('init', [t[1].id]), None)
    rep.resultado += t[1].res
    graph.viewGraph()

#---------------------------------------------------------------------
def p_vacio(t):
    'init   : '
    empty = nodo.Nodo(graph.setHoja('empty'), None)
    t[0] = nodo.Nodo(graph.setNodo('init', [empty.id]), None)

#---------------------------------------------------------------------
def p_instrucciones_l1(t):
    'instrucciones    : instruccion'
    
    t[0] = nodo.Nodo(graph.setNodo('instrucciones', [t[1].id]), str(t[1].res))

#---------------------------------------------------------------------
def p_instrucciones_l2(t):
    'instrucciones    : instruccion instrucciones'

    t[0] = nodo.Nodo(graph.setNodo('instrucciones', [t[1].id, t[2].id]), t[1].res + '\n' + t[2].res)

#---------------------------------------------------------------------
def p_instruccion(t):
    '''instruccion  : expresion PUNTO_COMA'''

    dato_2 = nodo.Nodo(graph.setHoja(';'), None)
    t[0] = nodo.Nodo(graph.setNodo('instruccion', [t[1].id, dato_2.id]), str(t[1].res))

#---------------------------------------------------------------------
def p_expresion_binario(t):
    '''expresion    : expresion SIMBOLO_SUMA expresion
                    | expresion SIMBOLO_RESTA expresion
                    | expresion SIMBOLO_DIVICION expresion
                    | expresion SIMBOLO_MULTIPLICACION expresion'''
    res = None
    if t[2] == '+': res = arit.Suma(t[1].res, t[3].res)
    elif t[2] == '-': res = arit.Resta(t[1].res, t[3].res) 
    elif t[2] == '/': res = arit.Divicion(t[1].res, t[3].res)
    elif t[2] == '*': res = arit.Multiplicacion(t[1].res, t[3].res)

    dato_2 = nodo.Nodo(graph.setHoja(t[2]), None)
    t[0] = nodo.Nodo(graph.setNodo('expresion', [t[1].id, dato_2.id, t[3].id]), res)

#---------------------------------------------------------------------
def p_expresion_par(t):
    'expresion  : IZQ_PARENTESIS expresion DER_PARENTESIS'

    dato_1 = nodo.Nodo(graph.setHoja('('), None)
    dato_3 = nodo.Nodo(graph.setHoja(')'), None)
    t[0] = nodo.Nodo(graph.setNodo('expresion', [dato_1.id, t[2].id, dato_3.id]), t[2].res)

#---------------------------------------------------------------------
def p_expresion_negativo(t):
    'expresion  : SIMBOLO_RESTA expresion %prec NEGATIVO'

    dato_1 = nodo.Nodo(graph.setHoja('-'), None)
    t[0] = nodo.Nodo(graph.setNodo('expresion', [dato_1.id, t[2].id]), -t[2].res)

#---------------------------------------------------------------------
def p_expresion_datos(t):
    '''expresion    : DATO_TIPO_FLOAT64
                    | DATO_TIPO_INT64
                    | DATO_TIPO_STRING'''

    dato_1 = nodo.Nodo(graph.setHoja(t[1]), None)
    dato_2 = nodo.Nodo(graph.setNodo('DATO', [dato_1.id]), None)
    t[0] = nodo.Nodo(graph.setNodo('expresion', [dato_2.id]), t[1])

#---------------------------------------------------------------------
def p_error(t):
    if t:
        rep.setError("Se esperaba " + t.type + " pero se obtuvo " + str(t.value), t.lexer.lineno, t.lexer.lexpos)
    else:
        rep.setError("Fin del archivo, se esperaba " + t.type + " pero se obtuvo " + str(t.value), t.lexer.lineno, t.lexer.lexpos)
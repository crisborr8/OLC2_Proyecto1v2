import ply.clases.clases as clase 
import ply.report.reportes as rep
import ply.report.graficar as graph
import ply.funcion.asignacion as asig
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

    t[0] = clase.Nodo(graph.setNodo('init', [t[1].id]), None)
    rep.resultado += t[1].res
    graph.saveGraph()

#---------------------------------------------------------------------
def p_vacio(t):
    'init   : '
    empty = clase.Nodo(graph.setHoja('empty'), None)
    t[0] = clase.Nodo(graph.setNodo('init', [empty.id]), None)

#---------------------------------------------------------------------
def p_instrucciones_l1(t):
    'instrucciones    : instruccion'

    t[0] = clase.Nodo(graph.setNodo('instrucciones', [t[1].id]), str(t[1].res))

#---------------------------------------------------------------------
def p_instrucciones_l2(t):
    'instrucciones    : instruccion instrucciones'

    t[0] = clase.Nodo(graph.setNodo('instrucciones', [t[1].id, t[2].id]), t[1].res + t[2].res)

#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
def p_instruccion_println(t):
    '''instruccion  : PRINTLN IZQ_PARENTESIS expresion DER_PARENTESIS PUNTO_COMA'''

    dato_1 = clase.Nodo(graph.setHoja('println'), None)
    dato_2 = clase.Nodo(graph.setHoja('('), None)
    dato_4 = clase.Nodo(graph.setHoja(')'), None)
    dato_5 = clase.Nodo(graph.setHoja(';'), None)

    if rep.line_error == False:
        t[0] = clase.Nodo(graph.setNodo('instruccion', [dato_1.id, dato_2.id, t[3].id, dato_4.id, dato_5.id]), str(t[3].res) + "\n")
    else:
        t[0] = clase.Nodo(graph.setNodo('instruccion', [dato_1.id, dato_2.id, t[3].id, dato_4.id, dato_5.id]), "")
    rep.line_error = False

#---------------------------------------------------------------------
def p_instruccion_print(t):
    '''instruccion  : PRINT IZQ_PARENTESIS expresion DER_PARENTESIS PUNTO_COMA'''

    dato_1 = clase.Nodo(graph.setHoja('print'), None)
    dato_2 = clase.Nodo(graph.setHoja('('), None)
    dato_4 = clase.Nodo(graph.setHoja(')'), None)
    dato_5 = clase.Nodo(graph.setHoja(';'), None)

    if rep.line_error == False:
        t[0] = clase.Nodo(graph.setNodo('instruccion', [dato_1.id, dato_2.id, t[3].id, dato_4.id, dato_5.id]), str(t[3].res))
    else:
        t[0] = clase.Nodo(graph.setNodo('instruccion', [dato_1.id, dato_2.id, t[3].id, dato_4.id, dato_5.id]), "")
    rep.line_error = False


#---------------------------------------------------------------------
def p_instruccion_asignacion(t):
    
    '''instruccion  : ID SIMBOLO_IGUAL expresion PUNTO_COMA'''

    asig.setAsignacion([t[1], t[3]], [t.lineno(1), t.lexpos(1)])
    print(t[1] + ": " + str(t[3].res))

    dato_1_1 = clase.Nodo(graph.setHoja(t[1]), None)
    dato_1_2 = clase.Nodo(graph.setNodo('ID', [dato_1_1.id]), None)
    dato_2 = clase.Nodo(graph.setHoja('='), None)
    dato_4 = clase.Nodo(graph.setHoja(';'), None)
    t[0] = clase.Nodo(graph.setNodo('instruccion', [dato_1_2.id, dato_2.id, t[3].id, dato_4.id]), "")
    rep.line_error = False

#---------------------------------------------------------------------
def p_instruccion_expresion(t):
    '''instruccion  : expresion'''

    print("es: " + str(t[1].res))
    if rep.line_error == False:
        t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), str(t[1].res) + '\n')
    else:
        t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), "")
    rep.line_error = False

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

    dato_2 = clase.Nodo(graph.setHoja(t[2]), None)
    t[0] = clase.Nodo(graph.setNodo('expresion', [t[1].id, dato_2.id, t[3].id]), res)

#---------------------------------------------------------------------
def p_expresion_par(t):
    'expresion  : IZQ_PARENTESIS expresion DER_PARENTESIS'

    dato_1 = clase.Nodo(graph.setHoja('('), None)
    dato_3 = clase.Nodo(graph.setHoja(')'), None)
    t[0] = clase.Nodo(graph.setNodo('expresion', [dato_1.id, t[2].id, dato_3.id]), t[2].res)

#---------------------------------------------------------------------
def p_expresion_negativo(t):
    'expresion  : SIMBOLO_RESTA expresion %prec NEGATIVO'

    dato_1 = clase.Nodo(graph.setHoja('-'), None)
    t[0] = clase.Nodo(graph.setNodo('expresion', [dato_1.id, t[2].id]), -t[2].res)

#---------------------------------------------------------------------
def p_expresion_datos(t):
    '''expresion    : DATO_TIPO_FLOAT64
                    | DATO_TIPO_INT64
                    | DATO_TIPO_STRING'''

    dato_1 = clase.Nodo(graph.setHoja(t[1]), None)
    dato_2 = clase.Nodo(graph.setNodo('DATO', [dato_1.id]), None)
    t[0] = clase.Nodo(graph.setNodo('expresion', [dato_2.id]), t[1])
    
#---------------------------------------------------------------------
def p_expresion_id(t):
    '''expresion    : ID'''
    dato_1_1 = clase.Nodo(graph.setHoja(t[1]), None)
    dato_1_2 = clase.Nodo(graph.setNodo('ID', [dato_1_1.id]), None)
    dato_2 = clase.Nodo(graph.setNodo('DATO', [dato_1_2.id]), None)

    res = asig.getAsignacionValor(t[1], clase.tipo_actual)
    if res[0] == 1:
        rep.setError("Error, dato " + t[1] + " no existe\n", t.lineno(1), t.lexpos(1))
        rep.resultado += "Error, dato " + t[1] + " no existe\n"
        rep.line_error = True
    t[0] = clase.Nodo(graph.setNodo('expresion', [dato_2.id]), res[1])

#---------------------------------------------------------------------
def p_error(t):
    rep.line_error = True
    if t:
        rep.setError("Se esperaba " + t.type + " pero se obtuvo " + str(t.value), t.lexer.lineno, t.lexer.lexpos)
    else:
        rep.setError("Fin del archivo, se esperaba ; ", t.lexer.lineno, t.lexer.lexpos)
import ply.clases.clases as clase 
import ply.report.reportes as rep
import ply.report.graficar as graph
import ply.funcion.asignacion.asignacion as asig
import ply.funcion.expresion.aritmeticas as arit

#---------------------------------------------------------------------
def p_instruccion_expresion(t):
    '''instruccion  : expresion'''

    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), None)
    rep.resultado += str(t[1].res) + '\n'

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
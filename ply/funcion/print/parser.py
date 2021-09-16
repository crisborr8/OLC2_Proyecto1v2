import ply.clases.clases as clase 
import ply.report.reportes as rep
import ply.report.graficar as graph


#---------------------------------------------------------------------
def p_instruccion_impresion(t):
    'instruccion    : impresion'

    new_stackable = []
    if t[1].error == True:
        rep.setError(t[1].value, t[1].fila, t[1].colu)
    else:
        new_stackable.append(clase.Stack('print', [str(t[1].value)]))

    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), new_stackable)

#---------------------------------------------------------------------
def p_impresion_println(t):
    '''impresion  : PRINTLN IZQ_PARENTESIS expresion DER_PARENTESIS PUNTO_COMA'''

    res = []
    if t[3].error == True:
        res = t[3].getValue()
    else:
        res = [False, str(t[3].value) + "\n"]

    dato_1 = clase.Nodo(graph.setHoja('println'))
    dato_2 = clase.Nodo(graph.setHoja('('))
    dato_4 = clase.Nodo(graph.setHoja(')'))
    dato_5 = clase.Nodo(graph.setHoja(';'))
    t[0] = clase.Nodo(graph.setNodo('impresion', [dato_1.id, dato_2.id, t[3].id, dato_4.id, dato_5.id]))
    t[0].setValue(res)

#---------------------------------------------------------------------
def p_impresion_print(t):
    '''impresion  : PRINT IZQ_PARENTESIS expresion DER_PARENTESIS PUNTO_COMA'''

    dato_1 = clase.Nodo(graph.setHoja('print'))
    dato_2 = clase.Nodo(graph.setHoja('('))
    dato_4 = clase.Nodo(graph.setHoja(')'))
    dato_5 = clase.Nodo(graph.setHoja(';'))
    t[0] = clase.Nodo(graph.setNodo('impresion', [dato_1.id, dato_2.id, t[3].id, dato_4.id, dato_5.id]))
    t[0].setValue(t[3].getValue())


import ply.clases.clases as clase 
import ply.report.reportes as rep
import ply.report.graficar as graph


#---------------------------------------------------------------------
def p_instruccion_impresion(t):
    'instruccion    : impresion'

    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), None)
    rep.resultado += t[1].res

#---------------------------------------------------------------------
def p_impresion_println(t):
    '''impresion  : PRINTLN IZQ_PARENTESIS expresion DER_PARENTESIS PUNTO_COMA'''

    dato_1 = clase.Nodo(graph.setHoja('println'), None)
    dato_2 = clase.Nodo(graph.setHoja('('), None)
    dato_4 = clase.Nodo(graph.setHoja(')'), None)
    dato_5 = clase.Nodo(graph.setHoja(';'), None)

    t[0] = clase.Nodo(graph.setNodo('impresion', [dato_1.id, dato_2.id, t[3].id, dato_4.id, dato_5.id]), str(t[3].res) + "\n")

#---------------------------------------------------------------------
def p_impresion_print(t):
    '''impresion  : PRINT IZQ_PARENTESIS expresion DER_PARENTESIS PUNTO_COMA'''

    dato_1 = clase.Nodo(graph.setHoja('print'), None)
    dato_2 = clase.Nodo(graph.setHoja('('), None)
    dato_4 = clase.Nodo(graph.setHoja(')'), None)
    dato_5 = clase.Nodo(graph.setHoja(';'), None)

    t[0] = clase.Nodo(graph.setNodo('impresion', [dato_1.id, dato_2.id, t[3].id, dato_4.id, dato_5.id]), str(t[3].res))


import ply.clases.clases as clase 
import ply.report.graficar as graph

#---------------------------------------------------------------------
def p_instruccion_sentenciaif(t):
    '''instruccion    : sentenciaif'''

    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), "")
    
#---------------------------------------------------------------------
def p_sentenciaif_if(t):
    '''sentenciaif    : IF condicion instrucciones if_then'''

    print("lo de if: " + str(t[2].res))
    dato_1 = clase.Nodo(graph.setHoja('if'), None)
    t[0] = clase.Nodo(graph.setNodo('sentenciaif', [dato_1.id, t[2].id, t[3].id, t[4].id]), "")

#---------------------------------------------------------------------
def p_sentenciaif_if_then(t):
    '''if_then  : if_elseif
                | if_else'''
    t[0] = clase.Nodo(graph.setNodo('if_then', [t[1].id]), None)

#---------------------------------------------------------------------
def p_sentenciaif_if_thenend(t):
    '''if_then  : END PUNTO_COMA'''
    dato_1 = clase.Nodo(graph.setHoja('end'), None)
    dato_2 = clase.Nodo(graph.setHoja(';'), None)
    t[0] = clase.Nodo(graph.setNodo('if_then', [dato_1.id, dato_2.id]), None)


#---------------------------------------------------------------------
def p_sentenciaif_if_elseif(t):
    '''if_elseif  : ELSE IF condicion instrucciones if_then'''

    dato_1 = clase.Nodo(graph.setHoja('else'), None)
    dato_2 = clase.Nodo(graph.setHoja('if'), None)
    t[0] = clase.Nodo(graph.setNodo('if_elseif', [dato_1.id, dato_2.id, t[3].id, t[4].id, t[5].id]), "")

#---------------------------------------------------------------------
def p_sentenciaif_if_else(t):
    '''if_else  : ELSE instrucciones END PUNTO_COMA'''

    dato_1 = clase.Nodo(graph.setHoja('else'), None)
    dato_3 = clase.Nodo(graph.setHoja('end'), None)
    dato_4 = clase.Nodo(graph.setHoja(';'), None)
    t[0] = clase.Nodo(graph.setNodo('if_else', [dato_1.id, t[2].id, dato_3.id, dato_4.id]), "")

#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
def p_condicion(t):
    '''condicion    : expresion MENOR expresion'''

    dato_2 = clase.Nodo(graph.setHoja('&#60;'), None)
    t[0] = clase.Nodo(graph.setNodo('condicion', [t[1].id, dato_2.id, t[3].id]), "")

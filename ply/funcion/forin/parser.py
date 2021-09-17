import ply.clases.clases as clase 
import ply.report.reportes as rep
import ply.report.graficar as graph

#---------------------------------------------------------------------
def p_instruccion_sentenciafor(t):
    '''instruccion  : sentenciafor'''

    new_stackable = []
    if t[1].error == True:
        rep.setError(t[1].value, t[1].fila, t[1].colu)
    else:
        new_stackable.append(clase.Stack('for', t[1].stack))

    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), new_stackable)

#---------------------------------------------------------------------
def p_sentenciafor_for(t):
    '''sentenciafor  : FOR dato IN rango instrucciones END PUNTO_COMA'''

    res = []
    childrens = []
    if t[4].error == False:
        childrens.append(clase.Stack('var', [t[2].value, 0]))
        childrens.append(t[4].value)
        childrens.append(t[5].stack)
    res = t[4].getValue()
    rep.setSimbolo(t[2].value[0], "var", "local - for", t.lineno(2), t.lexpos(2))

    dato_1 = clase.Nodo(graph.setHoja('for'))
    dato_3 = clase.Nodo(graph.setHoja('in'))
    dato_6 = clase.Nodo(graph.setHoja('end'))
    dato_7 = clase.Nodo(graph.setHoja(';'))
    t[0] = clase.Nodo(graph.setNodo('for', [dato_1.id, t[2].id, dato_3.id, t[4].id, t[5].id, dato_6.id, dato_7.id]), childrens)
    t[0].setValue(res)

#---------------------------------------------------------------------
def p_sentenciafor_rango(t):
    '''rango    : dato_numerico PUNTO_PUNTO dato_numerico'''

    rango = []
    for i in range(t[1].value,t[3].value + 1):
        rango.append(i)
    res = [False, rango]

    dato_2 = clase.Nodo(graph.setHoja(':'))
    t[0] = clase.Nodo(graph.setNodo('rango', [t[1].id, dato_2.id, t[3].id]), None)
    t[0].setValue(res)
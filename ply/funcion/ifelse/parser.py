import ply.clases.clases as clase 
import ply.report.graficar as graph
import ply.funcion.operadores.relacionales as rel

#---------------------------------------------------------------------
def p_instruccion_sentenciaif(t):
    '''instruccion    : sentenciaif'''

    new_stackable = []
    if t[1].error == True:
        rep.setError(t[1].value, t[1].fila, t[1].colu)
    else:
        new_stackable.append(clase.Stack('if', t[1].stack))

    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), new_stackable)
    
#---------------------------------------------------------------------
def p_sentenciaif_if(t):
    '''sentenciaif    : IF condicion instrucciones if_then'''

    childrens = []
    res = t[2].getValue()
    if t[2].error == True:
        childrens.append(False)
        childrens.append([])
        rep.setError(t[2].value, t[2].fila, t[2].colu)
    else:
        childrens.append(t[2].value)
        childrens.append(t[3].stack)
    childrens.append(t[4].stack)

    dato_1 = clase.Nodo(graph.setHoja('if'))
    t[0] = clase.Nodo(graph.setNodo('sentenciaif', [dato_1.id, t[2].id, t[3].id, t[4].id]), childrens)
    t[0].setValue(res)

#---------------------------------------------------------------------
def p_sentenciaif_if_thenend(t):
    '''if_then  : END PUNTO_COMA'''
    
    new_stackable = []
    new_stackable.append(clase.Stack('empty'))

    dato_1 = clase.Nodo(graph.setHoja('end'))
    dato_2 = clase.Nodo(graph.setHoja(';'))
    t[0] = clase.Nodo(graph.setNodo('if_then', [dato_1.id, dato_2.id]), new_stackable)

#---------------------------------------------------------------------
def p_sentenciaif_if_then(t):
    '''if_then  : if_elseif
                | if_else'''

    t[0] = clase.Nodo(graph.setNodo('if_then', [t[1].id]), t[1].stack)

#---------------------------------------------------------------------
def p_sentenciaif_if_elseif(t):
    '''if_elseif  : ELSE IF condicion instrucciones if_then'''

    childrens = []
    res = t[3].getValue()
    if t[3].error == True:
        childrens.append(False)
        childrens.append([])
        rep.setError(t[3].value, t[3].fila, t[3].colu)
    else:
        childrens.append(t[3].value)
        childrens.append(t[4].stack)
    childrens.append(t[5].stack)

    new_stackable = []
    new_stackable.append(clase.Stack('if', childrens))

    dato_1 = clase.Nodo(graph.setHoja('else'))
    dato_2 = clase.Nodo(graph.setHoja('if'))
    t[0] = clase.Nodo(graph.setNodo('if_elseif', [dato_1.id, dato_2.id, t[3].id, t[4].id, t[5].id]), new_stackable)
    t[0].setValue(res)

#---------------------------------------------------------------------
def p_sentenciaif_if_else(t):
    '''if_else  : ELSE instrucciones END PUNTO_COMA'''

    dato_1 = clase.Nodo(graph.setHoja('else'))
    dato_3 = clase.Nodo(graph.setHoja('end'))
    dato_4 = clase.Nodo(graph.setHoja(';'))
    t[0] = clase.Nodo(graph.setNodo('if_else', [dato_1.id, t[2].id, dato_3.id, dato_4.id]), t[2].stack)

#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
#---------------------------------------------------------------------
def p_condicio_arit(t):
    '''condicion    : expresion MENOR expresion
                    | expresion MAYOR expresion
                    | expresion IGUAL expresion
                    | expresion NOIGUAL expresion
                    | expresion MENOR_IGUAL expresion
                    | expresion MAYOR_IGUAL expresion'''
    
    res = []
    if t[1].error == True:
        res = t[1].getValue()
    elif t[3].error == True:
        res = t[3].getValue()
    else:
        res = rel.getResultArit([t[1].value, t.lineno(1), t.lexpos(1)], [t[3].value, t.lineno(3), t.lexpos(3)], t[2])

    dato_2 = clase.Nodo(graph.setHoja('&#60;'))
    t[0] = clase.Nodo(graph.setNodo('condicion', [t[1].id, dato_2.id, t[3].id]))
    t[0].setValue(res)

#---------------------------------------------------------------------
def p_condicio_logic(t):
    '''condicion    : condicion OR condicion
                    | condicion AND condicion'''
    
    res = []
    if t[1].error == True:
        res = t[1].getValue()
    elif t[3].error == True:
        res = t[3].getValue()
    else:
        res = rel.getResultLogic([t[1].value, t.lineno(1), t.lexpos(1)], [t[3].value, t.lineno(3), t.lexpos(3)], t[2])

    dato_2 = clase.Nodo(graph.setHoja(t[2]))
    t[0] = clase.Nodo(graph.setNodo('condicion', [t[1].id, dato_2.id, t[3].id]))
    t[0].setValue(res)
    
def p_condicio_not(t):
    '''condicion    : NOT condicion'''
    
    res = []
    if t[2].error == True:
        res = t[2].getValue()
    else:
        res = rel.getNot([t[2].value, t.lineno(2), t.lexpos(2)])

    dato_1 = clase.Nodo(graph.setHoja('!'))
    t[0] = clase.Nodo(graph.setNodo('condicion', [dato_1.id, t[2].id]))
    t[0].setValue(res)
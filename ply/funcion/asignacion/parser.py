import ply.clases.clases as clase 
import ply.report.reportes as rep
import ply.report.graficar as graph

#---------------------------------------------------------------------
def p_instruccion_asignacion(t):
    'instruccion    : asignacion'

    new_stackable = []
    if t[1].error == True:
        rep.setError(t[1].value, t[1].fila, t[1].colu)
    else:
        clase.current_vars.variables.append(t[1].value)
        rep.setSimbolo(t[1].value[0], "var", clase.current_vars.ambito, t.lineno(1), t.lexpos(1))
        new_stackable.append(clase.Stack('var', t[1].value))

    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), new_stackable)

#---------------------------------------------------------------------
def p_asignacion(t):
    
    '''asignacion  : dato SIMBOLO_IGUAL expresion PUNTO_COMA'''
    res = []
    if t[1].error == True:
        res = t[1].getValue()
    elif t[3].error == True:
        res = t[3].getValue()
    else:
        res = [False, [t[1].value, t[3].value]]

    dato_2 = clase.Nodo(graph.setHoja('='))
    dato_4 = clase.Nodo(graph.setHoja(';'))
    t[0] = clase.Nodo(graph.setNodo('asignacion', [t[1].id, dato_2.id, t[3].id, dato_4.id]))
    t[0].setValue(res)


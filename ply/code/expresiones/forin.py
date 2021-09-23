import ply.clases.clases as clase 
import ply.report.graficar as graph

#---------------------------------------------------------------------
def p_instruccion_forin(t):
    '''instruccion  : for'''
    
    t[0] = clase.Nodo(graph.setNodo('instruccion', [t[1].id]), [t[1].stack])

#---------------------------------------------------------------------
def p_for(t):
    '''for  : FOR dato_id IN rango instrucciones END PUNTO_COMA'''
    
    children_var = []
    children_var.append(t[2].value)      #0 - ID
    children_var.append(True)            #1 - Existe
    children_var.append(0)               #2 - Valor
    children_var.append("valor")         #3 - Referencia o por valor
    children_var.append(t[4].stack)      #4 - Texto lexema
    children_var.append(t.lexpos(1))     #5 - Fila lexema

    new_stack_var = clase.Stack('var_ext', children_var)
    new_stack_var.setFila(t.lineno(2))

    children = []
    children.append(new_stack_var)      #0 - Var
    children.append(t[5].stack)         #1 - Instruccion

    new_stack = clase.Stack('for', children)
    new_stack.setFila(t.lineno(1))

    dato_1 = clase.Nodo(graph.setHoja("for"))
    dato_3 = clase.Nodo(graph.setHoja("in"))
    dato_6 = clase.Nodo(graph.setHoja("end"))
    dato_7 = clase.Nodo(graph.setHoja(";"))
    t[0] = clase.Nodo(graph.setNodo('for', [dato_1.id, t[2].id, dato_3.id, t[4].id, t[5].id, dato_6.id, dato_7.id]), new_stack)
    
#---------------------------------------------------------------------
def p_rango(t):
    '''rango    : expresion PUNTO_PUNTO expresion'''

    children = []
    children.append(0)                                  #0 Type - rango
    children.append(clase.texto[t[1].start: t[1].end])  #1 Inicio
    children.append(clase.texto[t[3].start: t[3].end])  #2 Fin

    dato_2 = clase.Nodo(graph.setHoja(":"))
    t[0] = clase.Nodo(graph.setNodo('rango', [t[1].id, dato_2.id, t[3].id]), children)
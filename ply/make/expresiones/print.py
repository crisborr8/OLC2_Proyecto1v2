import ply.make.operaciones.aritmetica as arit
import ply.make.ejecutar as ejecutar
import ply.clases.clases as clase 

#---------------------------------------------------------------------
def p_instruccion_expresion(t):
    '''instruccion  : contenido'''
    print("valor->" + str(t[1].value))
    t[0] = t[1]

#---------------------------------------------------------------------
def p_imprimir_contenido(t):
    '''contenido   : expresion'''
    
    t[0] = t[1]

#---------------------------------------------------------------------
def p_imprimir_contenido_coma(t):
    '''contenido   : expresion COMA contenido'''
    
    if t[1].error:
        t[0] = t[1]
    elif t[3].error:
        t[0] = t[3]
    else:
        t[0] = clase.Result(str(t[1].value) + " " + str(t[3].value))


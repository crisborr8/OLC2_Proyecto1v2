import ply.make.operaciones.aritmetica as arit
import ply.make.ejecutar as ejecutar
import ply.clases.clases as clase 

#---------------------------------------------------------------------
def p_instruccion_expresion(t):
    '''instruccion  : expresion'''

    t[0] = t[1]

#---------------------------------------------------------------------
def p_expresion_binario(t):
    '''expresion    : expresion SIMBOLO_SUMA expresion
                    | expresion SIMBOLO_RESTA expresion
                    | expresion SIMBOLO_DIVICION expresion
                    | expresion SIMBOLO_MULTIPLICACION expresion'''

    if t[1].error:
        t[0] = t[1]
    elif t[3].error:
        t[0] = t[3]
    else:
        res = arit.getResult([t[1].value, t.lexpos(1)], [t[3].value, t.lexpos(3)], t[2])
        t[0] = clase.Result(res[1], res[0])
        if res[0]: 
            t[0].pos = res[2]

#---------------------------------------------------------------------
def p_expresion_numerico(t):
    '''expresion    : dato_numerico
                    | dato_id'''

    t[0] = t[1]
    
#---------------------------------------------------------------------
def p_expresion_par(t):
    '''expresion    : IZQ_PARENTESIS expresion DER_PARENTESIS'''

    t[0] = t[2]

#---------------------------------------------------------------------
def p_expresion_dato_numerico(t):
    '''dato_numerico    : DATO_TIPO_FLOAT64
                        | DATO_TIPO_INT64
                        | DATO_TIPO_STRING'''

    t[0] = clase.Result(t[1])

#---------------------------------------------------------------------
def p_expresion_dato_id(t):
    '''dato_id    : ID'''

    res = ejecutar.getId(ejecutar.current_stack, t[1])
    t[0] = clase.Result(res[1], res[0])

    if res[1]: clase.Result(t.lexpos(1))

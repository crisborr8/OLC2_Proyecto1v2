import ply.make.ejecutar as ejecutar
import ply.clases.clases as clase 

#---------------------------------------------------------------------
def p_instruccion_funcion(t):
    '''instruccion  : funcion_exp
                    | funcion_exp_param'''

    t[0] = t[1]

#---------------------------------------------------------------------
def p_funcion_dato(t):
    '''funcion_exp    :  dato_id IZQ_PARENTESIS DER_PARENTESIS'''

    res = ejecutar.getFuncion(ejecutar.current_stack, t[1])
    t[0] = clase.Result(res[1], res[0])

    if res[0]: t[0].pos = t.lexpos(1)

#---------------------------------------------------------------------
def p_funcion_dato_param(t):
    '''funcion_exp_param    :  dato_id IZQ_PARENTESIS parametros DER_PARENTESIS'''

    if t[3].error:
        t[0] = t[3]
    else:
        print("imprimiendo parametros de "+ t[1])
        print(t[3].value)
        res = ejecutar.getFuncionParam(ejecutar.current_stack, t[1], t[3].value)
        t[0] = clase.Result(res[1], res[0])

        if res[0]: t[0].pos = t.lexpos(1)

#---------------------------------------------------------------------
def p_parametros(t):
    '''parametros   : expresion'''

    t[0] = t[1]
    if not t[1].error:
        t[0].value = [t[1].value]

#---------------------------------------------------------------------
def p_parametros_coma(t):
    '''parametros   : expresion COMA parametros'''
    
    if t[1].error:
        t[0] = t[1]
    elif t[3].error:
        t[0] = t[3]
    else:
        t[0] = t[1]
        t[0].value = [t[1].value]
        t[0].value.extend(t[3].value)
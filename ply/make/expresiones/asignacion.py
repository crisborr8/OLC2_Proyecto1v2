import ply.make.ejecutar as ejecutar
import ply.clases.clases as clase 

#---------------------------------------------------------------------
def p_expresion_dato_id_arr(t):
    '''expresion_id    : dato_id array_exp'''

    res = ejecutar.getArray(ejecutar.current_stack, t[1], t[2].value)
    t[0] = clase.Result(res[1], res[0])

    if res[0]: t[0].pos = t.lexpos(1)

#---------------------------------------------------------------------
def p_expresion_dato(t):
    '''expresion_id    : dato_id'''

    res = ejecutar.getId(ejecutar.current_stack, t[1])
    t[0] = clase.Result(res[1], res[0])

    if res[0]: t[0].pos = t.lexpos(1)

#---------------------------------------------------------------------
def p_expresion_arrayExp(t):
    '''array_exp    : IZQ_LLAVE expresion DER_LLAVE'''
                    
    if t[2].error:
        t[0] = t[2]
    else:
        t[0] = clase.Result([t[2].value])

#---------------------------------------------------------------------
def p_expresion_arrayExp2(t):
    '''array_exp    : array_exp array_exp'''

    if t[1].error:
        t[0] = t[1]
    elif t[2].error:
        t[0] = t[2]
    else:
        t[0] = clase.Result(t[1].value)
        t[0].value.extend(t[2].value)


#---------------------------------------------------------------------
def p_expresion_array_param(t):
    '''array    : IZQ_LLAVE parametros DER_LLAVE'''

    t[0] = t[2]

    
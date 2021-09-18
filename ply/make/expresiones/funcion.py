import ply.make.ejecutar as ejecutar
import ply.clases.clases as clase 

#---------------------------------------------------------------------
def p_instruccion_funcion(t):
    '''instruccion  : funcion_exp PUNTO_COMA'''

    t[0] = t[1]

#---------------------------------------------------------------------
def p_funcion_dato(t):
    '''funcion_exp    :  dato_id IZQ_PARENTESIS DER_PARENTESIS'''

    print("a enviar: " + t[1])
    res = ejecutar.getFuncion(ejecutar.current_stack, t[1])
    t[0] = clase.Result(res[1], res[0])

    if res[0]: t[0].pos = t.lexpos(1)
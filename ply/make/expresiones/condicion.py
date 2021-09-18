import ply.make.operaciones.logica as logic
import ply.make.ejecutar as ejecutar
import ply.clases.clases as clase 

#---------------------------------------------------------------------
def p_instruccion_condicion(t):
    '''instruccion  : condicion'''

    t[0] = t[1]

#---------------------------------------------------------------------
def p_condicion_arit(t):
    '''condicion    : expresion MENOR expresion
                    | expresion MAYOR expresion
                    | expresion IGUAL expresion
                    | expresion NOIGUAL expresion
                    | expresion MENOR_IGUAL expresion
                    | expresion MAYOR_IGUAL expresion'''

    if t[1].error:
        t[0] = t[1]
    elif t[3].error:
        t[0] = t[3]
    else:
        res = logic.getResult([t[1].value, t.lexpos(1)], [t[3].value, t.lexpos(3)], t[2])
        t[0] = clase.Result(res[1], res[0])
        if res[0]: 
            t[0].pos = res[2]

#---------------------------------------------------------------------
def p_condicion_logic(t):
    '''condicion    : condicion OR condicion
                    | condicion AND condicion'''

    if t[1].error:
        t[0] = t[1]
    elif t[3].error:
        t[0] = t[3]
    else:
        res = logic.getResult([t[1].value, t.lexpos(1)], [t[3].value, t.lexpos(3)], t[2])
        t[0] = clase.Result(res[1], res[0])
        if res[0]: 
            t[0].pos = res[2]

#---------------------------------------------------------------------
def p_condicion_not(t):
    '''condicion    : NOT condicion'''

    if t[1].error:
        t[0] = t[1]
    else:
        res = logic.Not([t[1].value, t.lexpos(1)], t[2])
        t[0] = clase.Result(res[1], res[0])
        if res[0]: 
            t[0].pos = res[2]
    
#---------------------------------------------------------------------
def p_condicion_par(t):
    '''condicion    : IZQ_PARENTESIS condicion DER_PARENTESIS'''

    t[0] = t[2]
import ply.make.operaciones.aritmetica as arit
import ply.make.operaciones.nativas as nativ
import ply.make.ejecutar as ejecutar
import ply.clases.clases as clase 

#---------------------------------------------------------------------
def p_instruccion_expresion(t):
    '''instruccion  : expresion'''

    t[0] = t[1]

#---------------------------------------------------------------------
def p_expresion_par(t):
    '''expresion    : IZQ_PARENTESIS expresion DER_PARENTESIS'''

    t[0] = t[2]

#---------------------------------------------------------------------
def p_expresion_binario(t):
    '''expresion    : expresion SIMBOLO_SUMA expresion
                    | expresion SIMBOLO_RESTA expresion
                    | expresion SIMBOLO_DIVICION expresion
                    | expresion SIMBOLO_MULTIPLICACION expresion
                    | expresion SIMBOLO_POTENCIA expresion
                    | expresion SIMBOLO_MOD expresion'''

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
def p_expresion_nativa_binaria(t):
    '''expresion    : LOG IZQ_PARENTESIS expresion COMA expresion DER_PARENTESIS
                    | TRUNC IZQ_PARENTESIS tipo COMA expresion DER_PARENTESIS
                    | PARSE IZQ_PARENTESIS tipo COMA expresion DER_PARENTESIS'''

    if t[3].error:
        t[0] = t[3]
    elif t[5].error:
        t[0] = t[5]
    else:
        res = nativ.getResultBinari([t[3].value, t.lexpos(3)], [t[5].value, t.lexpos(5)], t[1])
        t[0] = clase.Result(res[1], res[0])
        if res[0]: 
            t[0].pos = res[2]

def p_expresion_tipo(t):
    '''tipo     : INT64
                | FLOAT64
                | NOTHING
                | STRING
                | CHAR
                | BOOL'''

    t[0] = clase.Result(t[1])

#---------------------------------------------------------------------
def p_expresion_nativa(t):
    '''expresion    : LOG10 IZQ_PARENTESIS expresion DER_PARENTESIS
                    | SIN IZQ_PARENTESIS expresion DER_PARENTESIS
                    | COS IZQ_PARENTESIS expresion DER_PARENTESIS
                    | TAN IZQ_PARENTESIS expresion DER_PARENTESIS
                    | SQRT IZQ_PARENTESIS expresion DER_PARENTESIS
                    | UPPER IZQ_PARENTESIS expresion DER_PARENTESIS
                    | LOWER IZQ_PARENTESIS expresion DER_PARENTESIS
                    | STRING_FUNC IZQ_PARENTESIS expresion DER_PARENTESIS
                    | TYPEOF IZQ_PARENTESIS expresion DER_PARENTESIS
                    | FLOAT IZQ_PARENTESIS expresion DER_PARENTESIS'''
    
    if t[3].error:
        t[0] = t[3]
    else:
        res = nativ.getResult([t[3].value, t.lexpos(3)], t[1])
        t[0] = clase.Result(res[1], res[0])
        if res[0]: 
            t[0].pos = res[2]
    
#---------------------------------------------------------------------
def p_expresion_numerico(t):
    '''expresion    : dato_numerico
                    | dato_booleano
                    | funcion_exp
                    | funcion_exp_param
                    | expresion_id
                    | array'''

    t[0] = t[1]
#---------------------------------------------------------------------
def p_expresion_negativo(t):
    'expresion  : SIMBOLO_RESTA expresion %prec NEGATIVO'

    if t[2].error:
        t[0] = t[2]
    else:
        res = arit.Negativo([t[2].value, t.lexpos(2)])
        t[0] = clase.Result(res[1], res[0])
        if res[0]: 
            t[0].pos = res[2]

#---------------------------------------------------------------------
def p_expresion_dato_booleano(t):
    '''dato_booleano    : TRUE
                        | FALSE'''

    if t[1] == "true":
        t[0] = clase.Result(True)
    else:
        t[0] = clase.Result(False) 
 
#---------------------------------------------------------------------
def p_expresion_dato_numerico(t):
    '''dato_numerico    : DATO_TIPO_FLOAT64
                        | DATO_TIPO_INT64'''

    t[0] = clase.Result(t[1])

#---------------------------------------------------------------------
def p_expresion_dato_string(t):
    '''dato_numerico    : DATO_TIPO_STRING
                        | DATO_TIPO_CHAR''' 
    
    t[0] = clase.Result(t[1][1:-1])



#---------------------------------------------------------------------
def p_expresion_dato_id(t):
    '''dato_id    : ID'''

    t[0] = t[1]
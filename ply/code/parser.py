precedence = (
    ('left','SIMBOLO_SUMA','SIMBOLO_RESTA'),
    ('left','SIMBOLO_MULTIPLICACION','SIMBOLO_DIVICION'),
    ('right','NEGATIVO'),
    )
#---------------------------------------------------------------------
#---------------------------------------------------------------------
names = { }
#---------------------------------------------------------------------
#---------------------------------------------------------------------
from ply.funcion.init.parser import *
from ply.funcion.print.parser import *
from ply.funcion.expresion.parser import *
from ply.funcion.asignacion.parser import *
from ply.funcion.ifelse.parser import *
#---------------------------------------------------------------------
#---------------------------------------------------------------------
def p_error(t):
    rep.line_error = True
    if t:
        rep.setError("Se esperaba " + t.type + " pero se obtuvo " + str(t.value), t.lexer.lineno, t.lexer.lexpos)
    else:
        rep.setError("Fin del archivo, se esperaba ; ", t.lexer.lineno, t.lexer.lexpos)
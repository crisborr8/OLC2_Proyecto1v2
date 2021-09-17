precedence = (
    ('left','AND','OR'),
    ('left','MENOR','MAYOR','MENOR_IGUAL','MAYOR_IGUAL','IGUAL','NOIGUAL'),
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
from ply.funcion.forin.parser import *
#---------------------------------------------------------------------
#---------------------------------------------------------------------
def p_error(t):
    rep.line_error = True
    if t:
        rep.setError("Error inesperado con " + t.type , t.lexer.lineno, t.lexer.lexpos)
    else:
        rep.setError("Error EOF")
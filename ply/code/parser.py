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
import ply.report.reportes as rep
from ply.code.expresiones.init import *
from ply.code.expresiones.asignacion import *
from ply.code.expresiones.expresion import *
from ply.code.expresiones.print import *
from ply.code.expresiones.ifelse import *
from ply.code.expresiones.forin import *
from ply.code.expresiones.whileend import *
from ply.code.expresiones.funcion import *
#---------------------------------------------------------------------
#---------------------------------------------------------------------
def p_error(t):
    if t:
        rep.setError("Error inesperado con " + t.type , t.lexer.lineno, t.lexer.lexpos)
    else:
        pass
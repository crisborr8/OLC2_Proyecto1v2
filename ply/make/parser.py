precedence = (
    ('left','AND','OR'),
    ('left','MENOR','MAYOR','MENOR_IGUAL','MAYOR_IGUAL','IGUAL','NOIGUAL'),
    ('left','SIMBOLO_SUMA','SIMBOLO_RESTA'),
    ('left','SIMBOLO_MULTIPLICACION','SIMBOLO_DIVICION'),
    ('left','SIMBOLO_POTENCIA','SIMBOLO_MOD'),
    ('right','NEGATIVO'),
    )
#---------------------------------------------------------------------
#---------------------------------------------------------------------
names = { }
#---------------------------------------------------------------------
#---------------------------------------------------------------------
import ply.report.reportes as rep
from ply.make.expresiones.init import *
from ply.make.expresiones.funcion import *
from ply.make.expresiones.expresion import *
from ply.make.expresiones.condicion import *
from ply.make.expresiones.arreglos import *
from ply.make.expresiones.print import *
#---------------------------------------------------------------------
#---------------------------------------------------------------------
def p_error(t):
    pass
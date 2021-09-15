from ply.code.lexer import *
import ply.ply.lex as lex
lexer = lex.lex()

from ply.code.parser import *
import ply.ply.yacc as yacc
parser = yacc.yacc()

import ply.report.reportes as rep
def init(texto):
    rep.initVariables()
    rep.txt = texto
    parser.parse(texto, tracking=True)

    rep.setReporte_Error()
    rep.setReporte_Simbolos()
    
    return rep.resultado
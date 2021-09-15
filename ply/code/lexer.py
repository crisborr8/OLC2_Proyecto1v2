import ply.report.reportes as rep

reserved = {
    'println'   : 'PRINTLN',
    'print'     : 'PRINT',
    'if'        : 'IF',
    'else'      : 'ELSE',
    'end'       : 'END'
}
tokens = [
    'TABULADOR', 'SALTO',
    'ID',
    'DATO_TIPO_FLOAT64', 'DATO_TIPO_INT64', 'DATO_TIPO_STRING',
    'SIMBOLO_SUMA', 'SIMBOLO_RESTA', 'SIMBOLO_DIVICION', 'SIMBOLO_MULTIPLICACION', 'SIMBOLO_IGUAL',
    'PUNTO_COMA', 'IZQ_PARENTESIS', 'DER_PARENTESIS', 
    'OR', 'NOT', 'AND',
    'MENOR', 'MAYOR', 'MENOR_IGUAL', 'MAYOR_IGUAL', 'IGUAL'
] + list(reserved.values())

t_TABULADOR                 = r'\t'
t_SALTO                     = r'\n'

t_SIMBOLO_SUMA              = r'\+'
t_SIMBOLO_RESTA             = r'-'
t_SIMBOLO_DIVICION          = r'/'
t_SIMBOLO_MULTIPLICACION    = r'\*'
t_SIMBOLO_IGUAL             = r'='

t_PUNTO_COMA                = r';'
t_IZQ_PARENTESIS            = r'\('
t_DER_PARENTESIS            = r'\)'

t_OR                        = r'\|\|'
t_NOT                       = r'!'
t_AND                       = r'&&'

t_MENOR                     = r'<'
t_MAYOR                     = r'>'
t_MENOR_IGUAL               = r'<='
t_MAYOR_IGUAL               = r'>='
t_IGUAL                     = r'=='

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID') 
    return t

def t_DATO_TIPO_FLOAT64(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
def t_DATO_TIPO_INT64(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_DATO_TIPO_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = str(t.value)[1:-1]
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
def t_eof(t):
    t.lexer.lineno = 1

t_ignore_COMENTARIO = r'\#((=(.|\n)*=\#)|.*)'
t_ignore_SALTO      = r'\ |\r'

def t_error(t):
    if t:
        rep.setError("Caracter ilegal " + t.value[0], t.lexer.lineno, t.lexer.lexpos)
        t.lexer.skip(1)
    else:
        rep.setError("EOF", t.lexer.lineno, t.lexer.lexpos)

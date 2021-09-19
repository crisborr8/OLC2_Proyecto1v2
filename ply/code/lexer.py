import ply.report.reportes as rep

reserved = {
    'println'   : 'PRINTLN',
    'print'     : 'PRINT',
    'if'        : 'IF',
    'else'      : 'ELSE',
    'end'       : 'END',
    'for'       : 'FOR',
    'in'        : 'IN',
    'while'     : 'WHILE',
    'function'  : 'FUNCION',
    'log10'     : 'LOG10',
    'log'       : 'LOG',
    'sin'       : 'SIN',
    'cos'       : 'COS',
    'tan'       : 'TAN',
    'sqrt'      : 'SQRT',
    'uppercase' : 'UPPER',
    'lowercase' : 'LOWER',
    'true'      : 'TRUE',
    'false'     : 'FALSE',
    'return'    : 'RETURN',

    'parse'     : 'PARSE',
    'trunc'     : 'TRUNC',
    'float'     : 'FLOAT',
    'typeof'    : 'TYPEOF',
    'string'    : 'STRING_FUNC',

    'Int64'     : 'INT64',
    'Float64'   : 'FLOAT64',
    'Bool'      : 'BOOL',
    'Char'      : 'CHAR',
    'String'    : 'STRING',
    'nothing'   : 'NOTHING'
}
tokens = [
    'TABULADOR', 'SALTO',
    'ID',
    'DATO_TIPO_FLOAT64', 'DATO_TIPO_INT64', 'DATO_TIPO_STRING', 'DATO_TIPO_CHAR',
    'SIMBOLO_SUMA', 'SIMBOLO_RESTA', 'SIMBOLO_DIVICION', 'SIMBOLO_MULTIPLICACION', 'SIMBOLO_IGUAL',
    'SIMBOLO_POTENCIA', 'SIMBOLO_MOD',
    'COMA', 'PUNTO_COMA', 'PUNTO_PUNTO', 'IZQ_PARENTESIS', 'DER_PARENTESIS', 
    'OR', 'NOT', 'AND',
    'MENOR', 'MAYOR', 'MENOR_IGUAL', 'MAYOR_IGUAL', 'IGUAL', 'NOIGUAL'
] + list(reserved.values())

t_TABULADOR                 = r'\t'
t_SALTO                     = r'\n'

t_SIMBOLO_SUMA              = r'\+'
t_SIMBOLO_RESTA             = r'-'
t_SIMBOLO_DIVICION          = r'/'
t_SIMBOLO_MULTIPLICACION    = r'\*'
t_SIMBOLO_POTENCIA          = r'\^'
t_SIMBOLO_MOD               = r'%'
t_SIMBOLO_IGUAL             = r'='

t_COMA                      = r','
t_PUNTO_COMA                = r';'
t_PUNTO_PUNTO               = r':'
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
t_NOIGUAL                   = r'!='

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
    t.value = str(t.value)
    return t
def t_DATO_TIPO_CHAR(t):
    r'\'([^\\\n]|(\\.))\''
    t.value = str(t.value)
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

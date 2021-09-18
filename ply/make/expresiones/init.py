import ply.clases.clases as clase 

start = 'init'

#---------------------------------------------------------------------
def p_init(t):
    'init   : instruccion'
    clase.res = t[1]

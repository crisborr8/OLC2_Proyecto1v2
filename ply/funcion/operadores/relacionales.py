import ply.report.reportes as rep

def getResultArit(t1, t2, op):
    if op == '>': return Mayor(t1, t2)
    elif op == '<': return Menor(t1, t2)
    elif op == '==': return Igual(t1, t2)
    elif op == '!=': return Noigual(t1, t2)
    elif op == '<=': return Mayor_igual(t1, t2)
    elif op == '>=': return Menor_igual(t1, t2)

def Mayor(t_1, t_2):
    t1 = t_1[0]
    t2 = t_2[0]
    if t1 > t2: return [False, True]
    return [False, False]
    
def Menor(t_1, t_2):
    t1 = t_1[0]
    t2 = t_2[0]
    if t1 < t2: return [False, True]
    return [False, False]

def Igual(t_1, t_2):
    t1 = t_1[0]
    t2 = t_2[0]
    if t1 == t2: return [False, True]
    return [False, False]
    
def Noigual(t_1, t_2):
    t1 = t_1[0]
    t2 = t_2[0]
    if t1 != t2: return [False, True]
    return [False, False]
    
def Menor_igual(t_1, t_2):
    t1 = t_1[0]
    t2 = t_2[0]
    if t1 != t2: return [False, True]
    return [False, False]
    
def Mayor_igual(t_1, t_2):
    t1 = t_1[0]
    t2 = t_2[0]
    if t1 != t2: return [False, True]
    return [False, False]

#-----------------------------------------------------
def getResultLogic(t1, t2, op):
    if op == '||': return Or(t1, t2)
    elif op == '&&': return And(t1, t2)

def Or(t_1, t_2):
    t1 = t_1[0]
    t2 = t_2[0]
    if t1 or t2: return [False, True]
    return [False, False]

def And(t_1, t_2):
    t1 = t_1[0]
    t2 = t_2[0]
    if t1 and t2: return [False, True]
    return [False, False]

def getNot(t_1):
    t1 = t_1[0]
    if not t1: return [False, True]
    return [False, False]

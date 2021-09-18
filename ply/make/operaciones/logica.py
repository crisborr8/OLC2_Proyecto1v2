
def getResult(t1, t2, op):
    if op == '<': return Menor(t1, t2) 
    elif op == '>': return Mayor(t1, t2)
    elif op == '==': return Igual(t1, t2)
    elif op == '<=': return Menorigual(t1, t2)
    elif op == '>=': return Mayorigual(t1, t2)

def Not(t1, t2):
    t1_val = t1[0]
    if t1_val == True or t1_val == False:
        return [False, not t1_val]
    return [True, "Error, " + t1_val + " debe ser tipo booleano",  t1[1]]
    
def Menor(t1, t2):
    t1_val = t1[0]
    t2_val = t2[0]
    print(t1_val)
    print(t2_val)
    if t1_val < t2_val:
        return [False, True]
    return [False, False]
    
def Mayor(t1, t2):
    t1_val = t1[0]
    t2_val = t2[0]
    if t1_val > t2_val:
        return [False, True]
    return [False, False]
    
def Igual(t1, t2):
    t1_val = t1[0]
    t2_val = t2[0]
    if t1_val == t2_val:
        return [False, True]
    return [False, False]
    
def Menorigual(t1, t2):
    t1_val = t1[0]
    t2_val = t2[0]
    if t1_val <= t2_val:
        return [False, True]
    return [False, False]
    
def Mayorigual(t1, t2):
    t1_val = t1[0]
    t2_val = t2[0]
    if t1_val >= t2_val:
        return [False, True]
    return [False, False]
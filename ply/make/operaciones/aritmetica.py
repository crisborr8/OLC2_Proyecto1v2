
def getResult(t1, t2, op):
    if op == '+': return Suma(t1, t2) 
    elif op == '-': return Resta(t1, t2)
    elif op == '/': return Divicion(t1, t2)
    elif op == '*': return Multiplicacion(t1, t2)
    elif op == '^': return Potencia(t1, t2)
    elif op == '%': return Mod(t1, t2)

def Negativo(t1):
    t1_val = t1[0]
    if isinstance(t1_val, str):
        return [True, "Error, " + str(t1_val) + " debe ser numerico\n", t1[1]]
    return [False, -t1_val]

def Suma(t1, t2):
    t1_val = t1[0]
    t2_val = t2[0]
    if isinstance(t1_val, str) or isinstance(t2_val, str):
        return [False, str(t1_val) + str(t2_val)]
    return [False, t1_val + t2_val]
    
def Resta(t1, t2):
    t1_val = t1[0]
    t2_val = t2[0]
    if isinstance(t1_val, str):
        return [True, "Error, " + str(t1_val) + " debe ser numerico\n", t1[1]]
    if isinstance(t2_val, str):
        return [True, "Error, " + str(t2_val) + " debe ser numerico\n", t2[1]]
    return [False, t1_val - t2_val]

def Divicion(t1, t2):
    t1_val = t1[0]
    t2_val = t2[0]
    if isinstance(t1_val, str):
        return [True, "Error, " + str(t1_val) + " debe ser numerico\n", t1[1]]
    if isinstance(t2_val, str):
        return [True, "Error, " + str(t2_val) + " debe ser numerico\n", t2[1]]
    if t2_val == 0:
        return [True, "Error, no se puede dividir entre 0\n", t2[1]]
    return [False, t1_val / t2_val]

def Multiplicacion(t1, t2):
    t1_val = t1[0]
    t2_val = t2[0]
    if isinstance(t1_val, str) or isinstance(t2_val, str):
        return [False, str(t1_val) + str(t2_val)]
    return [False, t1_val * t2_val]

def Potencia(t1, t2):
    t1_val = t1[0]
    t2_val = t2[0]
    if isinstance(t2_val, str):
        return [True, "Error, " + str(t2_val) + " debe ser numerico\n", t2[1]]
    if isinstance(t2_val, float):
        return [True, "Error, " + str(t2_val) + " debe ser entero\n", t2[1]]
    if isinstance(t1_val, str):
        t_origin = t1_val
        for i in range(1, t2_val):
            t1_val = t1_val + t_origin
        return [False, t1_val]
    if isinstance(t1_val, float):
        return [True, "Error, " + str(t1_val) + " debe ser entero\n", t1[1]]
    return [False, t1_val ** t2_val]

def Mod(t1, t2):
    t1_val = t1[0]
    t2_val = t2[0]
    if isinstance(t1_val, str):
        return [True, "Error, " + str(t1_val) + " debe ser numerico\n", t1[1]]
    if isinstance(t2_val, str):
        return [True, "Error, " + str(t2_val) + " debe ser numerico\n", t2[1]]
    if t2_val == 0:
        return [True, "Error, no se puede dividir entre 0\n", t2[1]]
    return [False, t1_val % t2_val]

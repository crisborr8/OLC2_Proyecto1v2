import math

def getResultBinari(t1, t2, op):
    if op == 'log': return Log(t1, t2) 
    elif op == 'parse': return Parse(t1, t2) 
    elif op == 'trunc': return Parse(t1, t2) 

def Log(t1, t2):
    t1_val = t1[0]
    t2_val = t2[0]
    if isinstance(t1_val, str):
        return [True, "Error, " + str(t1_val) + " debe ser numerico\n", t1[1]]
    if isinstance(t2_val, str):
        return [True, "Error, " + str(t2_val) + " debe ser numerico\n", t2[1]]
    if t1_val == 1:
        return [True, "Error, la base debe ser distinto a 1\n", t1[1]]
    if t1_val <= 0:
        return [True, "Error, base debe ser mayor a 0\n", t1[1]]
    if t2_val <= 0:
        return [True, "Error, valor debe ser mayor a 0\n", t2[1]]
    return [False, math.log(t2_val, t1_val)]
    
def Parse(t1, t2):
    t1_val = t1[0]
    t2_val = t2[0]
    if t1_val == 'Int64':
        try:
            return [False, int(t2_val)]
        except X:
            return [True, "Error, " + str(t2_val) + " no se puede pasar a Int64\n", t2[1]]
    if t1_val == 'Float64':
        try:
            return [False, float(t2_val)]
        except X:
            return [True, "Error, " + str(t2_val) + " no se puede pasar a Float64\n", t2[1]]
    if t1_val == 'Bool':
        try:
            return [False, bool(t2_val)]
        except X:
            return [True, "Error, " + str(t2_val) + " no se puede pasar a Bool\n", t2[1]]
    if t1_val == 'String':
        try:
            return [False, str(t2_val)]
        except X:
            return [True, "Error, " + str(t2_val) + " no se puede pasar a String\n", t2[1]]
    if t1_val == 'Char':
        try:
            return [False, chr(t2_val)]
        except X:
            return [True, "Error, " + str(t2_val) + " no se puede pasar a Char\n", t2[1]]

#---------------------------------------------------------------------------------

def getResult(t1, op):
    if op == 'log10': return Log10(t1) 
    elif op == 'sin': return Sin(t1)
    elif op == 'cos': return Cos(t1)
    elif op == 'tan': return Tan(t1)
    elif op == 'sqrt': return Sqrt(t1)
    elif op == 'uppercase': return Upper(t1)
    elif op == 'lowercase': return Lower(t1)
    elif op == 'string': return String(t1)
    elif op == 'typeof': return Typeof(t1)
    elif op == 'float': return Float(t1)

def Log10(t1):
    t1_val = t1[0]
    if isinstance(t1_val, str):
        return [True, "Error, base debe ser numerico\n", t1[1]]
    if t1_val <= 0:
        return [True, "Error, base debe ser mayor a 0\n", t1[1]]
    return [False, math.log10(t1_val)]

def Sin(t1):
    t1_val = t1[0]
    if isinstance(t1_val, str):
        return [True, "Error, " + str(t1_val) + " debe ser numerico\n", t1[1]]
    return [False, math.sin(t1_val)]

def Cos(t1):
    t1_val = t1[0]
    if isinstance(t1_val, str):
        return [True, "Error, " + str(t1_val) + " debe ser numerico\n", t1[1]]
    return [False, math.cos(t1_val)]

def Tan(t1):
    t1_val = t1[0]
    if isinstance(t1_val, str):
        return [True, "Error, " + str(t1_val) + " debe ser numerico\n", t1[1]]
    return [False, math.tan(t1_val)]

def Sqrt(t1):
    t1_val = t1[0]
    if isinstance(t1_val, str):
        return [True, "Error, " + str(t1_val) + " debe ser numerico\n", t1[1]]
    if t1_val < 0:
        return [True, "Error, " + str(t1_val) + " debe mayor o igual a 0\n", t1[1]]
    return [False, math.sqrt(t1_val)]

def Upper(t1):
    t1_val = t1[0]
    if isinstance(t1_val, str):
        return [False, t1_val.upper()]
    return [True, "Error, " + str(t1_val) + " debe ser string\n", t1[1]]

def Lower(t1):
    t1_val = t1[0]
    if isinstance(t1_val, str):
        return [False, t1_val.lower()]
    return [True, "Error, " + str(t1_val) + " debe ser string\n", t1[1]]

def String(t1):
    t1_val = t1[0]
    return [False, str(t1_val)]

def Typeof(t1):
    t1_val = t1[0]
    if isinstance(t1_val, str):
        if len(t1_val) == 1: return [False, "Char"]
        return [False, "String"]
    if isinstance(t1_val, bool):
        return [False, "Bool"]
    if isinstance(t1_val, int):
        return [False, "Int64"]
    if isinstance(t1_val, float):
        return [False, "Float64"]
    return [False, "None"]

def Float(t1):
    t1_val = t1[0]
    try:
        return [False, float(t1_val)]
    except X:
        return [True, "Error, " + str(t1_val) + " no se puede pasar a Float64\n", t1[1]]

from typing_extensions import Concatenate
import ply.report.reportes as rep

#-------------------------------------------------------------------
def setNegativo(t):
    t1 = t[0]
    if isinstance(t1, str): 
        return [True, t1 + " debe ser tipo numérico", t[1], t[2]]
    return [False, -t1]

#-------------------------------------------------------------------
def getResult(t1, t2, op):
    if op == '+': return Suma(t1, t2)
    elif op == '-': return Resta(t1, t2)
    elif op == '/': return Divicion(t1, t2)
    elif op == '*': return Multiplicacion(t1, t2)

#-------------------------------------------------------------------
#-------------------------------------------------------------------
#-------------------------------------------------------------------
def Suma(t_1, t_2):
    t1 = t_1[0]
    t2 = t_2[0]
    if isinstance(t1, str) or isinstance(t2, str):
        return [False, str(t1) + str(t2)]
    return [False, t1 + t2]

#-------------------------------------------------------------------
def Resta(t_1, t_2):
    t1 = t_1[0]
    t2 = t_2[0]
    if isinstance(t1, str):
        return [True, "Error, " + str(t1) + " debe ser numérico\n", t_1[1], t_1[2]]
    elif isinstance(t2, str):
        return [True, "Error, " + str(t2) + " debe ser numérico\n", t_2[1], t_2[2]]
    return [False, t1 - t2]

#-------------------------------------------------------------------
def Divicion(t_1, t_2):
    t1 = t_1[0]
    t2 = t_2[0]
    if isinstance(t1, str):
        return [True, "Error, " + str(t1) + " debe ser numérico\n", t_1[1], t_1[2]]
    elif isinstance(t2, str):
        return [True, "Error, " + str(t2) + " debe ser numérico\n", t_2[1], t_2[2]]
    if t2 == 0:
        return [True, "Error, no se puede dividir con 0\n", t_2[1], t_2[2]]
    return [False, t1 / t2]

#-------------------------------------------------------------------
def Multiplicacion(t_1, t_2):
    t1 = t_1[0]
    t2 = t_2[0]
    if isinstance(t1, str) or isinstance(t2, str):
        return [False, str(t1) + str(t2)]
    return [False, t1 * t2]
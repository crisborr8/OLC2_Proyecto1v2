from typing_extensions import Concatenate
import ply.report.reportes as rep

def Suma(t1, t2):
    if isinstance(t1, str) or isinstance(t2, str):
        return str(t1) + str(t2)
    return t1 + t2

def Resta(t1, t2):
    if isinstance(t1, str):
        rep.resultado += "Error, " + str(t1) + " debe ser numérico\n"
        rep.line_error = True
        return 0
    elif isinstance(t2, str):
        rep.resultado += "Error, " + str(t2) + " debe ser numérico\n"
        rep.line_error = True
        return 0
    return t1 - t2

def Divicion(t1, t2):
    if isinstance(t1, str):
        rep.resultado += "Error, " + str(t1) + " debe ser numérico\n"
        rep.line_error = True
        return 0
    elif isinstance(t2, str):
        rep.resultado += "Error, " + str(t2) + " debe ser numérico\n"
        rep.line_error = True
        return 0
    if t2 == 0:
        rep.resultado += "Error, " + str(t2) + " debe ser distinto de cero\n"
        rep.line_error = True
        return 0
    return t1 / t2

def Multiplicacion(t1, t2):
    if isinstance(t1, str) or isinstance(t2, str):
        return str(t1) + str(t2)
    return t1 * t2
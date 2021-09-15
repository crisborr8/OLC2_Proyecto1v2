import ply.clases.clases as c
import ply.report.reportes as rep


def setAsignacion(T, pos):
    newVar = c.Variable(T[0], T[1].res, T[1].res)
    c.ambito_actual.variables.append(newVar)
    rep.setSimbolo(newVar.name, newVar.tipo, c.ambito_actual.name, pos[0], pos[1])

def getAsignacionValor(name, type):
    aux_ambito = c.ambito_actual
    while aux_ambito != None:
        for var in aux_ambito.variables:
            if var.name == name:
                return [0, var.value]
        if type != "local":
            aux_ambito = aux_ambito.padre
    return [1, 0]
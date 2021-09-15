##############################################################################################
##############################################################################################
class Nodo:
    def __init__(self, id, res):
        self.id = id
        self.res = res

##############################################################################################
##############################################################################################

class Funcion:
    def __init__(self, name, fila, columna, variables = [], padre = None):
        self.name = name
        self.fila = fila
        self.columna = columna
        self.variables = variables
        self.padre = padre
    def getPos(self):
        return [self.fila, self.columna]

tipo_actual = "Global"
ambito_actual = Funcion("Global", 0, 0)

def initGlobal():
    global ambito_actual, tipo_actual
    tipo_actual = "Global"
    ambito_actual = Funcion("Global", 0, 0)

##############################################################################################
##############################################################################################
class Variable:
    
    def __init__(self, name, tipo, value):
        self.name = name
        self.tipo = str(type(tipo))
        self.value = value

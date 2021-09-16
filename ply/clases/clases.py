##############################################################################################
##############################################################################################
class Nodo:
    def __init__(self, id, stack = None, error = False, value = None, fila = 0, colu = 0):
        self.id = id
        self.stack = stack
        self.error = error
        self.value = value
        self.fila = fila
        self.colu = colu

    def setPosicion(self, fila = 0, colu = 0):
        self.fila = fila
        self.colu = colu
    
    def setValue(self, res):
        self.error = res[0]
        self.value = res[1]
        if self.error:
            self.setPosicion(res[2], res[3])
    
    def getValue(self):
        return [self.error, self.value, self.fila, self.colu]

##############################################################################################
##############################################################################################
class Vars:
    def __init__(self, ambito = "Global", variables = [], father = None):
        self.ambito = ambito
        self.variables = variables
        self.father = father

    def getValue(data, new_var):
        name = data[0]
        if new_var == None:
            return [True, "Error, variable " + name + " no encontrada", data[1], data[2]]
        for var in new_var.variables:
            if var[0] == name:
                return [False, var[1]]
        return getValue(data, new_var.father)

current_vars = Vars()

class Stack:
    def __init__(self, stack_type, childrens = [], direct_father = None):
        self.stack_type = stack_type
        self.childrens = childrens
        self.direct_father = direct_father
    
    def setFather(self, direct_father):
        self.direct_father = direct_father
    
    def getFather(self):
        return self.direct_father
    
    def getStack_type(self):
        return self.stack_type
    
    def getChildrens(self):
        return self.childrens

##############################################################################################
##############################################################################################
def initVars():
    global current_vars
    current_vars = Vars("Global", [], None)
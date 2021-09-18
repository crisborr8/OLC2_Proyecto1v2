##############################################################################################
##############################################################################################
class Nodo:
    def __init__(self, id, stack = None):
        self.id = id
        self.stack = stack
    
    def setPos(self, pos):
        self.start = pos[0]
        self.end = pos[1]

    def getPos(self):
        return [self.start, self.end]

    def setValue(self, value):
        self.value = value

##############################################################################################
##############################################################################################
class Stack:
    def __init__(self, type, children = [], father = None):
        self.type = type
        self.father = father
        self.children = children
    
    def setFila(self, fila):
        self.fila = fila

##############################################################################################
##############################################################################################
class Result:
    def __init__(self, value, error = False):
        self.value = value
        self.error = error
    
    def setPos(self, pos):
        self.pos = pos
    

##############################################################################################
##############################################################################################
texto = ""
res = Result(False, 0)
current_stack = Stack(None)
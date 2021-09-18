#----------------------------------------------------------
from ply.code.lexer import *
import ply.ply.lex as lex
lexer = lex.lex()

#----------------------------------------------------------
from ply.make.parser import *
import ply.ply.yacc as yacc
exp_parser = yacc.yacc()

#----------------------------------------------------------
import ply.report.reportes as rep
current_stack = None

#----------------------------------------------------------
def init(stack):
    rep.resultado = ejecutarStack(stack, None)

#----------------------------------------------------------

def ejecutarStack(stack, father):
    global current_stack

    for child in stack:
        child.father = father
        
    respond = ""
    current_stack = stack

    for inst in stack:
        if inst.type == 'exp':   #---------------------------------------------------------------------
            exp_parser.parse(inst.children[0], tracking=True)
            if clase.res.error:
                rep.setError(clase.res.value, inst.fila, clase.res.pos)
            else:
                respond += str(clase.res.value) + '\n'
        elif inst.type == 'print': #---------------------------------------------------------------------
            exp_parser.parse(inst.children[1], tracking=True)
            if clase.res.error:
                rep.setError(clase.res.value, inst.fila, inst.children[2] + clase.res.pos)
            else:
                respond += str(clase.res.value) + inst.children[0]
        elif inst.type == 'var': #---------------------------------------------------------------------
            exp_parser.parse(inst.children[4], tracking=True)
            if clase.res.error:
                inst.children[1] = False
                rep.setError(clase.res.value, inst.fila, clase.res.pos)
            else:
                inst.children[1] = True
                inst.children[2] = clase.res.value

                ambito = "Global"
                if inst.father != None: ambito = "Local " + inst.type
                rep.setSimbolo(inst.children[0], inst.type, ambito, inst.fila, inst.children[5])
        elif inst.type == "if": #---------------------------------------------------------------------
            print("if con texto->" + inst.children[0])
            exp_parser.parse(inst.children[0], tracking=True)
            if clase.res.error:
                rep.setError(clase.res.value, inst.fila, inst.children[1] + clase.res.pos)
            else:
                if clase.res.value == True:
                    respond += ejecutarStack(inst.children[2], inst)
                else:
                    respond += ejecutarStack(inst.children[3], inst)
    return respond

def getId(stack, id):
    for var in stack:
        if var.type == 'var':
            if id == var.children[0] and var.children[1]:
                return [False, var.children[2]]

    if stack.father != None:
        return getId(stack.father, id)
    return [True, "Error, Id no encontrado"]
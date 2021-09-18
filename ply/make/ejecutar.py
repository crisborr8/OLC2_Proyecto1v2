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
    rep.resultado = ejecutarStack(stack)

#----------------------------------------------------------

def ejecutarStack(stack, father = None, ambito = "Global"):
    global current_stack

    for child in stack:
        child.father = father
        
    respond = ""

    for inst in stack:
        current_stack = stack
        #-----------------------------------------------------------------------------------------
        if inst.type == 'exp':
            exp_parser.parse(inst.children[0], tracking=True)
            if clase.res.error:
                rep.setError(clase.res.value, inst.fila, clase.res.pos)
            else:
                respond += str(clase.res.value) + '\n'
        #-----------------------------------------------------------------------------------------
        elif inst.type == 'print':
            exp_parser.parse(inst.children[1], tracking=True)
            if clase.res.error:
                rep.setError(clase.res.value, inst.fila, inst.children[2] + clase.res.pos)
            else:
                respond += str(clase.res.value) + inst.children[0]
        #-----------------------------------------------------------------------------------------
        elif inst.type == 'var':
            exp_parser.parse(inst.children[4], tracking=True)
            if clase.res.error:
                inst.children[1] = False
                rep.setError(clase.res.value, inst.fila, clase.res.pos)
            else:
                inst.children[1] = True
                inst.children[2] = clase.res.value

                rep.setSimbolo(inst.children[0], inst.type, ambito, inst.fila, inst.children[5])
        #-----------------------------------------------------------------------------------------
        elif inst.type == "if":
            exp_parser.parse(inst.children[0], tracking=True)
            if clase.res.error:
                rep.setError(clase.res.value, inst.fila, inst.children[1] + clase.res.pos)
            else:
                if clase.res.value == True:
                    respond += ejecutarStack(inst.children[2], stack, ambito + " - Local If")
                else:
                    respond += ejecutarStack(inst.children[3], stack, ambito + " - Local If")
        #-----------------------------------------------------------------------------------------
        elif inst.type == "for":
            rango_res = []
            if inst.children[0].children[4][0] == 0:
                rango_res = getRango(inst.children[0].children[4])

            if not rango_res[0]:
                inst.children[1].extend([inst.children[0]])
                rep.setSimbolo(inst.children[0].children[0], "var", ambito + " - Local For", inst.children[0].fila, inst.children[0].children[5])
                for var in rango_res[1]:
                    current_stack = stack
                    inst.children[0].children[2] = var
                    respond += ejecutarStack(inst.children[1], stack, ambito + " - Local For")
        #-----------------------------------------------------------------------------------------
    return respond

def getId(stack, id):
    for var in stack:
        if var.type == 'var':
            if id == var.children[0] and var.children[1]:
                return [False, var.children[2]]
        elif var.type == 'var_ext':
            if id == var.children[0] and var.children[1]:
                return [False, var.children[2]]
    if stack[0].father != None:
        return getId(stack[0].father, id)
    return [True, "Error, Id no encontrado"]

def getRango(rango):
    start = 0
    end = 0
    exp_parser.parse(rango[1], tracking=True)
    if clase.res.error:
        rep.setError(clase.res.value, inst.fila, clase.res.pos)
        return [True, 0]
    else:
        start = clase.res.value
        exp_parser.parse(rango[2], tracking=True)
        if clase.res.error:
            rep.setError(clase.res.value, inst.fila, clase.res.pos)
            return [True, 0]
        else:
            end = clase.res.value
            rango = []
            for i in range(start, end + 1):
                rango.append(i)
            return [False, rango]

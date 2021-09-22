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
respond = ""

#----------------------------------------------------------

def init(stack):
    global respond
    respond = ""
    print("iniciando ejecucion")
    ejecutarStack(stack)
    print("Respuesta: " + respond)
    rep.resultado = respond

#----------------------------------------------------------

def ejecutarStack(stack, father = None, ambito = "Global"):
    global current_stack, respond

    for child in stack:
        child.father = father

    return_res = [[False, None], False]  #[return, respond] break
    i = 0

    for inst in stack:
        current_stack = stack
        #-----------------------------------------------------------------------------------------
        if inst.type == 'exp':
            print("exp buscando -> " +inst.children[0])
            exp_parser.parse(inst.children[0], tracking=True)
            if clase.res.error:
                rep.setError(clase.res.value, inst.fila, clase.res.pos)
            else:
                pass
                #respond += str(clase.res.value) + '\n'
                #print("exp respond con: " + str(clase.res.value) + "\n")
        #-----------------------------------------------------------------------------------------
        elif inst.type == 'print':
            exp_parser.parse(inst.children[1], tracking=True)
            if clase.res.error:
                rep.setError(clase.res.value, inst.fila, inst.children[2])
            else:
                respond += str(clase.res.value) + inst.children[0]
        #-----------------------------------------------------------------------------------------
        elif inst.type == 'var':
            exp_parser.parse(inst.children[4], tracking=True)
            if clase.res.error:
                inst.children[1] = False
                rep.setError(clase.res.value, inst.fila, clase.res.pos)
            else:
                new_var = True
                _current_stack = stack
                while stack != None:
                    for var in stack:
                        if var.type == 'var':
                            if inst.children[0] == var.children[0] and var.children[1]:
                                var.children[2] =  clase.res.value
                                new_var = False
                    stack = stack[0].father
                stack = _current_stack

                inst.children[1] = True
                inst.children[2] = clase.res.value

                if new_var:
                    rep.setSimbolo(inst.children[0], inst.type, ambito, inst.fila, inst.children[5])
        #-----------------------------------------------------------------------------------------
        elif inst.type == 'array':
            exp_parser.parse(inst.children[4], tracking=True)
            if clase.res.error:
                inst.children[1] = False
                rep.setError(clase.res.value, inst.fila, clase.res.pos)
            else:
                modificado = False
                _current_stack = stack
                while stack != None:
                    for var in stack:
                        if var.type == 'var':
                            if inst.children[0] == var.children[0] and var.children[1]:
                                params_texts = inst.children[6].split('[')
                                del params_texts[0]
                                Params = []
                                new_val = clase.res.value
                                pos_val = 0
                                for txt in params_texts:
                                    exp_parser.parse(txt.strip()[:-1], tracking=True)
                                    if clase.res.error:
                                        modificado = True
                                        pos_val = clase.res.pos
                                        break
                                    Params.append(clase.res.value)

                                if modificado:
                                    rep.setError("Error, ubicacion del array no valida", inst.fila, pos_val)
                                else:
                                    res = setValueArray(var.children[2], Params, new_val)
                                    if res[0]:
                                        rep.setError("Error, ubicacion del array no valida", inst.fila, pos_val)
                                    else:
                                        var.children[2] = res[1]

                                modificado = True
                        if modificado: break
                    if modificado: break
                    stack = stack[0].father
                stack = _current_stack
                
        #-----------------------------------------------------------------------------------------
        elif inst.type == "if":
            exp_parser.parse(inst.children[0], tracking=True)
            if clase.res.error:
                rep.setError(clase.res.value, inst.fila, inst.children[1])
            else:
                print("en el if con -> " + str(clase.res.value))
                if clase.res.value == True:
                    return_res = ejecutarStack(inst.children[2], stack, ambito + " - Local If")
                else:
                    return_res = ejecutarStack(inst.children[3], stack, ambito + " - Local If")
                print(str(return_res))
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
                    return_res = ejecutarStack(inst.children[1], stack, ambito + " - Local For")
                    if return_res[1] or return_res[0][0]:
                        return_res[1] = False
                        break
        #-----------------------------------------------------------------------------------------
        elif inst.type == "while":
            while True:
                exp_parser.parse(inst.children[0], tracking=True)
                if clase.res.error:
                    rep.setError(clase.res.value, inst.fila, inst.children[1])
                    break
                else:
                    if clase.res.value == True:
                        return_res = ejecutarStack(inst.children[2], stack, ambito + " - Local While")
                        if return_res[1] or return_res[0][0]:
                            return_res[1] = False
                            break
                    else:
                        break
        #-----------------------------------------------------------------------------------------
        elif inst.type == "ret":
            exp_parser.parse(inst.children[0], tracking=True)
            if clase.res.error:
                rep.setError(clase.res.value, inst.fila, clase.res.pos)
            else:
                return_res[0] = [True, clase.res.value]
            
        #-----------------------------------------------------------------------------------------
        elif inst.type == "funcion":
            param_res = []
            rep.setSimbolo(inst.children[0].children[0], inst.type, ambito, inst.fila, inst.children[2])

            if inst.children[0].children[1] == True:
                param_res = getParams(inst.children[0].children[2])
                for param in param_res:
                    rep.setSimbolo(param.children[0], "var", ambito + " - Local Funcion ", inst.fila, inst.children[2])
                param_res.extend(inst.children[1])
                inst.children[1] = param_res

            #respond += ejecutarStack(inst.children[1], stack, ambito + " - Local Funcion " + inst.children[0].children[0])
                    
        #-----------------------------------------------------------------------------------------
        i += 1
        if return_res[1] or return_res[0][0]:
            return return_res
        #-----------------------------------------------------------------------------------------
    return return_res

def getId(stack, id):
    for var in stack:
        if var.type == 'array' or var.type == 'var' or var.type == 'var_ext':
            if id == var.children[0] and var.children[1]:
                return [False, var.children[2]]
    if stack[0].father != None:
        return getId(stack[0].father, id)
    return [True, "Error, Id '" + id + "' no encontrado"]

    
def getArray(stack, id, Params):
    for var in stack:
        if var.type == 'var' or var.type == 'var_ext':
            if id == var.children[0] and var.children[1]:
                return getValueArray(var.children[2], Params)
    if stack[0].father != None:
        return getId(stack[0].father, id)
    return [True, "Error, Id '" + id + "' no encontrado"]

def getValueArray(array, Params):
    try:
        while len(Params) > 0:
            array = array[Params[0]]
            del Params[0]
        return [False, array]
    except:
        return [True, "Error, ubicacion de array no encontrado"]

        
def setValueArray(array, Params, value):
    try:
        if len(Params) > 0:
            i = Params[0]
            arr = array[i]
            del Params[0]
            res = setValueArray(arr, Params, value)
            if res[0]:
                return res
            else:
                array[i] = res[1]
                return [False, array]
        return [False, value]
    except:
        return [True, "Error, ubicacion de array no encontrado"]

def getFuncion(stack, id):
    for var in stack:
        if var.type == 'funcion':
            var_ = var.children[0]
            if id == var_.children[0]:
                if var_.children[1]:
                    return [True, "Error, La funcion '" + id + "' necesita parametros"]
                else:
                    res =  ejecutarStack(var.children[1], stack, "Global - Local Funcion " + id + "()")[0]                     
                    res[0] = clase.res.error
                    if res[0]:
                        res[1] = clase.res.value
                    return res
    if stack[0].father != None:
        return getFuncion(stack[0].father, id)
    return [True, "Error, Id '" + id + "' no encontrado"]

def getFuncionParam(stack, id, params):
    print("parametros: " + str(params))
    for var in stack:
        if var.type == 'funcion':
            var_ = var.children[0]
            if id == var_.children[0]:
                if var_.children[1]:
                    param_res = getParams(var_.children[2])
                    if len(param_res) != len(params):
                        return [True, "Error, La funcion " + id + " necesita " + str(len(param_res)) + " parametros"]
                    else:
                        i = 0
                        old_params = []
                        for value in params:
                            old_params.append(var.children[1][i].children[2])
                            var.children[1][i].children[2] = value
                            i = i + 1
                        print("****** original params: " + str(old_params))
                        print("****** actual params: " + str(params))
                        print("-----> Iniciando ejecucion con " + str(params))
                        res = ejecutarStack(var.children[1], stack, "Global - Local Funcion " + id + "("+var_.children[2]+")")[0]                     
                        res[0] = clase.res.error
                        if res[0]:
                            res[1] = clase.res.value
                        i = 0
                        print("respuesta ---> " + str(res))
                        print("****** now params params: " + str(old_params))
                        params = []
                        for value in old_params:
                            params.append(var.children[1][i].children[2])
                            var.children[1][i].children[2] = value
                            i = i + 1
                        print("-----> Ejecucion finalizada, regresando a " + str(params))
                        return res
                else:
                    return [True, "Error, La funcion '" + id + "' NO necesita parametros"]
    if stack[0].father != None:
        return getFuncionParam(stack[0].father, id, params)
    return [True, "Error, Id '" + id + "' no encontrado"]


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

def getParams(params):
    var = []
    print(params)
    params = params.split(',')
    for pr in params:
        children = []
        children.append(pr.strip())    #0 - ID
        children.append(True)          #1 - Existe
        children.append(0)             #2 - Valor
        children.append("valor")       #3 - Referencia o por valor

        new_stack_var = clase.Stack('var_ext', children)
        var.extend([new_stack_var])
    return var
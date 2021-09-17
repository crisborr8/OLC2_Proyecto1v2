import ply.report.reportes as rep

def ejecutarStack(stack, father = None):
    for instruccion in stack:
        instruccion.father = father
        if instruccion.stack_type == 'print':
            rep.resultado += instruccion.childrens[0]
        elif instruccion.stack_type == 'if':
            if instruccion.childrens[0]:
                ejecutarStack(instruccion.childrens[1], instruccion)
            else:
                ejecutarStack(instruccion.childrens[2], instruccion)
        elif instruccion.stack_type == 'for':
            ins_for = instruccion.childrens
            for var in ins_for[1]:
                instruccion.childrens[0].childrens[1] = var
                print(instruccion.childrens[0].childrens[0] + " -> " + str(instruccion.childrens[0].childrens[1]))
                ejecutarStack(instruccion.childrens[2], instruccion)

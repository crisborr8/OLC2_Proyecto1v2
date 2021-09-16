import ply.report.reportes as rep

def ejecutarStack(stack):
    for instruccion in stack:
        if instruccion.stack_type == 'print':
            rep.resultado += instruccion.childrens[0]
        elif instruccion.stack_type == 'if':
            if instruccion.childrens[0]:
                ejecutarStack(instruccion.childrens[1])
            else:
                ejecutarStack(instruccion.childrens[2])

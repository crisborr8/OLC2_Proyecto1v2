from datetime import datetime
import ply.report.graficar as graph

resultado = ""
errores = ""
c_errores = 0
txt = ""

def initVariables():
    global resultado, errores, c_errores
    c_errores = 0
    resultado = ""
    errores = "<html><head><style>table {  font-family: arial, sans-serif;  border-collapse: collapse;"
    errores += "width: 100%;}td, th {  border: 1px solid #dddddd;  text-align: left;  padding: 8px;}"
    errores += "tr:nth-child(even) {  background-color: #dddddd;}</style></head><body><table>\n"
    errores += "<tr><th>No</th><th>Descripcion</th><th>Linea</th><th>Columna</th><th>Fecha y hora</th></tr>\n"
    graph.initGraph()

def getTime():
    return  datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def setError(des, lin, col):
    global errores, c_errores, txt
    n_col = txt.rfind('\n', 0, col) + 1
    col = col - n_col + 1 
    c_errores += 1
    errores += "<tr><th>"+str(c_errores)+"</th>"
    errores += "<th>"+des+"</th>"
    errores += "<th>"+str(lin)+"</th>"
    errores += "<th>"+str(col)+"</th>"
    errores += "<th>"+getTime()+"</th></tr>\n"

def setReportes():
    global errores
    errores += "</table></body></html>"

    file_name = "templates/reporte_errores.html"
    f = open(file_name, 'w+')
    f.write(errores)
    f.close()
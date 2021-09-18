from datetime import datetime
import ply.clases.clases as clase 
import ply.report.graficar as graph

line_error = False
resultado = ""
errores = ""
simbolos = ""
c_errores = 0

def initVariables(texto):
    global resultado, errores, c_errores, simbolos, line_error
    line_error = False
    c_errores = 0
    resultado = ""
    clase.texto = texto

    errores = "<html><head><style>table {  font-family: arial, sans-serif;  border-collapse: collapse;"
    errores += "width: 100%;}td, th {  border: 1px solid #dddddd;  text-align: left;  padding: 8px;}"
    errores += "tr:nth-child(even) {  background-color: #dddddd;}</style></head><body><table>\n"
    errores += "<tr><th>No</th><th>Descripcion</th><th>Linea</th><th>Columna</th><th>Fecha y hora</th></tr>\n"
    
    simbolos = "<html><head><style>table {  font-family: arial, sans-serif;  border-collapse: collapse;"
    simbolos += "width: 100%;}td, th {  border: 1px solid #dddddd;  text-align: left;  padding: 8px;}"
    simbolos += "tr:nth-child(even) {  background-color: #dddddd;}</style></head><body><table>\n"
    simbolos += "<tr><th>Nombre</th><th>Tipo</th><th>Ambito</th><th>Fila</th><th>Columna</th></tr>\n"

    graph.initGraph()

def getTime():
    return  datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def getCol(col):
    n_col = clase.texto.rfind('\n', 0, col) + 1
    return col - n_col + 1 

def setError(des, lin, col):
    global errores, c_errores
    c_errores += 1
    errores += "<tr><th>"+str(c_errores)+"</th>"
    errores += "<th>"+des+"</th>"
    errores += "<th>"+str(lin)+"</th>"
    errores += "<th>"+str(col + 1)+"</th>"
    errores += "<th>"+getTime()+"</th></tr>\n"

def setSimbolo(nombre, tipo, ambito, lin, col):
    global simbolos
    simbolos += "<tr><th>"+nombre+"</th>"
    simbolos += "<th>"+tipo+"</th>"
    simbolos += "<th>"+ambito+"</th>"
    simbolos += "<th>"+str(lin)+"</th>"
    simbolos += "<th>"+str(getCol(col))+"</th>"

def setReporte_Error():
    global errores
    errores += "</table></body></html>"

    file_name = "templates/reporte_errores.html"
    f = open(file_name, 'w+')
    f.write(errores)
    f.close()

def setReporte_Simbolos():
    global simbolos
    simbolos += "</table></body></html>"

    file_name = "templates/reporte_simbolos.html"
    f = open(file_name, 'w+')
    f.write(simbolos)
    f.close()
from flask import Flask, render_template, request, send_from_directory
from ply.main import init
import os

app = Flask(__name__)

texto = ""

@app.route('/')
def index():
    return render_template('index.html', checkInit=".")

@app.route('/submitCompilar', methods=['POST'])
def submitCompilar():
    if request.method == 'POST':
        global texto
        texto = request.form['textInput']
        return render_template('index.html',Input=texto, Output=init(texto), checkCompi=".")
        
@app.route('/submitReporteErrores', methods=['POST'])
def submitReporteErrores():
    if request.method == 'POST':
        global texto
        return render_template('reporte_errores.html')

@app.route('/submitReporteAST', methods=['POST'])
def submitReporteAST():
    if request.method == 'POST':
        global texto
        os.system('dot -Tpdf ply/report/input.dot > templates/AST.pdf')
        return send_from_directory("templates", 'AST.pdf')

@app.route('/submitReporteTabla', methods=['POST'])
def submitReporteTabla():
    if request.method == 'POST':
        global texto
        return render_template('reporte_simbolos.html')

if __name__ == '__main__':
    app.debug = True 
    app.run()
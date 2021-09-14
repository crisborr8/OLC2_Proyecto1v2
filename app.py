from flask import Flask, render_template, request
from ply.main import init

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

if __name__ == '__main__':
    app.debug = True 
    app.run()
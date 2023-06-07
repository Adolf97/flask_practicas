from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def mainPage():
    return '<h1>Página principal</h1>'


@app.route('/hello')
@app.route('/hello/<name>')
@app.route('/hello/<name>/<int:age>')
def helloPage(name=None, age=None):
    if name == None and age == None:
        return '<h1>Hola! Bienvenido a mi página con Flask!</h1>'
    elif age == None:
        return f'<h1>Hola, {name}! Bienvenido a mi página</h1>'
    else:
        return f'<h1>Hola, {name}! Bienvenido a mi página web.<br>Tu edad es de {age} años.</h1>'


@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'
    # Se usa el escape, para ejecutar código como texto plano. Con esto evitamos ataques externos
    #  de códigos maliciosos

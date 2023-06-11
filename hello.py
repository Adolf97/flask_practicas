from flask import Flask, render_template
from markupsafe import escape
from datetime import datetime

app = Flask(__name__)


@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')
# app.add_template_filter(today, 'today')


@app.add_template_global
def repeat(s, n):
    return s * n
# app.add_template_global(repeat, 'repeat')


@app.route('/')
@app.route('/index')
def mainPage():
    name = 'adolfo'
    friends = ['Adolfo', 'Carlos', 'Cristian', 'Jorge']
    date = datetime.now()
    return render_template(
        'index.html',
        name=name,
        friends=friends,
        date=date
    )


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

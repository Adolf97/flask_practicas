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
@app.route('/hello/<name>/<int:age>/<email>')
def helloPage(name=None, age=None, email=None):
    my_data = {
        'name': name,
        'age': age,
        'email': email
    }
    return render_template('hello.html', data=my_data)


@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'
    # Se usa el escape, para ejecutar código como texto plano. Con esto evitamos ataques externos
    #  de códigos maliciosos

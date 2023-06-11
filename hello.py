from flask import Flask, render_template, url_for, request
from markupsafe import escape
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev'
)


@app.add_template_filter
def today(date):
    return date.strftime('%d-%m-%Y')
# app.add_template_filter(today, 'today')


@app.add_template_global
def repeat(s, n):
    return s * n
# app.add_template_global(repeat, 'repeat')


@app.route('/')
def mainPage():
    print(url_for('mainPage'))
    print(url_for('helloPage'))
    print(url_for('code', code='print("Hola")'))
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


class RegisterForm(FlaskForm):
    username = StringField("Nombre de usuario: ")
    password = PasswordField("Contraseña: ")
    submit = SubmitField("Registrar")


@app.route('/auth/registro', methods=['GET', 'POST'])
def registro():
    form = RegisterForm()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if len(username) >= 4 and len(username) <= 25 and len(password) >= 8 and len(password) <= 25:
            return f'Nombre de usuario: {username} <br >Contraseña: {password}'
        else:
            error = """
            El nombre de usuaio debe ser mayor a 4 caracteres y menor a 25 caracteres.
            La contraseña debe ser mayor a 8 caracteres y menor a 25 caracteres.
            """
            return render_template('auth/register.html', form=form, error=error)
    return render_template('auth/register.html', form=form)

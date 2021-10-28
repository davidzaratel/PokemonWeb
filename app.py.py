from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('¿Cual es tu nombre?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class FirstValForm(FlaskForm):
    primerValor = StringField('Ingresa el primer valor:', validators=[DataRequired()])
    segundoValor = StringField('Ingresa el segundo valor:', validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
        name = None
        form = NameForm()
        if form.validate_on_submit():
            name = form.name.data
            form.name.data = ''
        return render_template('registro.html', form=form, name=name)


@app.route('/calculadora', methods=['GET', 'POST'])
def calculadora():
        # primero = None
        # segundo = None
        resultado = None
        primerValor = None
        segundoValor = None
        form = FirstValForm()
        if form.validate_on_submit():
            primerValor = form.primerValor.data
            segundoValor = form.segundoValor.data
            resultado = int(primerValor) + int(segundoValor)
            form.primerValor.data = ''
            form.segundoValor.data = ''

        # resultado = primerValor + segundoValor
        return render_template('calculadora.html', form=form, resultado=resultado)

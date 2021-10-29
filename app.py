# from _typeshed import NoneType
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

bootstrap = Bootstrap(app)
moment = Moment(app)


class PokeForm(FlaskForm):
    name = StringField('También puedes intentar ingresar un número random de entre 1 y 1118 para ver un pokemon aleatorio', validators=[DataRequired()])
    submit = SubmitField('Buscar')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500




@app.route('/')
def index():
    return render_template('index.html')

def pokeAttributes(name):

    try:
        poke = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}").json()
    except:
        poke = requests.get(f"https://pokeapi.co/api/v2/pokemon/1").json()

    imgPoke = "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/1200px-Pok%C3%A9_Ball_icon.svg.png" if poke["sprites"]["front_default"] == None else poke["sprites"]["front_default"]

    # [nombre, altura, peso, experiencia base, número de habilidades, número de movimientos, imagen]
    attributes = [poke["name"], poke["height"], poke["weight"], poke["base_experience"], len(poke["abilities"]), len(poke["moves"]), imgPoke]

    return attributes

@app.route('/pokeinfo', methods=['GET', 'POST'])
def pokeinfo():
    pokeData = None
    form = PokeForm()
    if form.validate_on_submit():
        userInput = str(form.name.data)

        # Validamos que la entrada del usuario sea válida
        if(userInput.isalpha() or userInput.isnumeric()):
            pokeData = pokeAttributes(userInput.lower())
        else:
            pokeData = pokeAttributes("1")
        
        form.name.data = ''

    return render_template('pokeinfo.html', form=form, pokeData=pokeData)

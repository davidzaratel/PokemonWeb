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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

import requests
from bs4 import BeautifulSoup

URL = "https://animangapedia.fandom.com/es/wiki/Lista_de_pel%C3%ADculas_de_Pok%C3%A9mon"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="content")

table = results.find_all("table", class_="wikitable")

info = table[0].find("tbody")
movies = info.find_all("tr")

multipleLines = ""
singleLine = ""
movieString = ""
for i in range(2,len(movies)):
  multipleLines = movies[i].text
  singleLine = multipleLines.replace(".\n\n",". ")
  singleLine = singleLine.replace("\n\n",", lanzada el ")
  singleLine = singleLine.replace("\n", "")
  movieString += singleLine + '\n'





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

@app.route('/movies')
def movies():
        return render_template('movies.html', movieString=movieString)

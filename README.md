# PokemonWeb

Página web creada por David Zárate y Daniel Maldonado usando Flask con la que se puede consultar información sobre los pokemones, a través de llamadas a la api https://pokeapi.co/, y sus películas, usando web scraping.

## Instalación

Para instalar ejecutar esta web, instale las siguientes dependencias:
```
pip install flask
pip install flask-bootstrap
pip install flask-moment
pip install flask-wtf
python3 -m pip install requests
python3 -m pip install beautifulsoup4
```

Use el siguiente comando para generar el ejecutable de Flask:
```
export FLASK_APP=app.py
```

Por último, para ejecutar la app, ejecute el siguiente comando:
```
flask run
```

Y listo, ya puede abrir el http://127.0.0.1:5000/ y disfrutar de la PokeWeb.

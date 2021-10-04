introduction au développement web avec Flask
https://openschool.art/pad/p/capsule001

# activer l'environement python
 python -m venv venv
 source venv/bin/activate

# installer flask
pip install flask

# creation du ficher server.py
touch server.py

# variable global + lancement
export FLASK_APP=server.py
flask run

# mode debug
python server.py

# template jinja2
dossier templates

# assets
static avec une route
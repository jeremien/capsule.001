introduction au développement web avec Flask


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
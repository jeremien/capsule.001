import os
from flask import Flask
from flask import (
                    render_template,
                    send_from_directory,
                    json,
                    jsonify,
                    request
                  )
from flask.wrappers import Request 

app = Flask(__name__)
app.debug = True

data = [
        {'firstname': 'joe', 
        'lastname':'éponge'},
        {'firstname': 'julie', 
        'lastname':'jacob'},
       ]

def open_file(file, type):
  with app.open_resource(f'data/{file}') as d:
    if type == 'json':
      return json.load(d)
    else:
      return d.read()

@app.route('/')
def home():
  return render_template('home.html', content='salut')

@app.route('/hello/<name>')
def page(name):
  return f'hello {name}'

@app.route('/data')
def users():
  html = '<body>\n'
  for d in data:
    for k in d.values():
      html += '<li>' + k + '</li>'
  html += '</body>'
  print(html)
  return html

@app.route('/dataplus')
def usersplus():
  return render_template('users.html', data=data)

@app.route('/api')
def api():
  d = open_file('data.json', type='json')
  return jsonify(d)
  # return jsonify(data)

@app.route('/txt')
def text():
  d = open_file('data.txt', type='texte')
  return d

@app.route('/form', methods=['GET', 'POST'])
def form():
  
  if request.method == 'GET':
    print('GET')
    return render_template('form.html')
  
  if request.method == 'POST':
    print('POST')
    txt_file = os.path.join("data","data.txt")
    nom = request.form['nom']
    with open(txt_file, 'w') as file:
      file.write(nom)
    return render_template('home.html', content='nom enregistré')

@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)

if __name__ == "__main__":
  app.run(debug=True)
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True

data = [
        {'firstname': 'joe', 
        'lastname':'éponge'},
        {'firstname': 'julie', 
        'lastname':'jacob'},
       ]

@app.route('/')
def home():
  return "ceci est la page d'accueil"

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

if __name__ == "__main__":
  app.run(debug=True)
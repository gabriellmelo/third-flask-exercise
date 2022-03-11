from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return '<h1>Olá Mundo!</h1>'

@app.route('/unifran')
def unifran():
  return '<h2>Universidade de Franca</h2>'

@app.route('/dashboard/<name>')
def dashboard(name):
  return f' Olá, {name}'

app.run(host='0.0.0.0', port=8080)
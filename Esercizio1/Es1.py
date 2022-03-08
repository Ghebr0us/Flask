#effettuare un sito che permetta di effettuare il login
#l'utente inserisce lo username e la password
#se lo username è admin e la password èxxx123## il sito ci saluta con un messaggio di benvenuto
#altrimenti ci da un messaggio di errore
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def log1():
    return render_template("style1.html")

@app.route('/login', methods=['GET'])
def log2():
  us = request.args['username']
  pw = request.args['Password']
  if us == 'admin' and pw == 'xxx123##':
    return render_template("wel.html",user =us)
  else:
    return  '<h1>Errore</h1>'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
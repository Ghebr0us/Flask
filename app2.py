#esercizio: realizzare un server web che visualizzi l'ora,e colori lo sfondo in base all'orario: un colore per la mattina, uno per il pomeriggio, uno per la sera e una per la notte.
from flask import Flask, render_template 
app = Flask(__name__)
from datetime import datetime

@app.route('/', methods=['GET'])
def time():
    minuti = datetime.now().minute
    if minuti%2 == 0:
      col = 'green'
    else:
      col = 'red'
    return render_template('index2.html',colore =col,min = minuti)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)